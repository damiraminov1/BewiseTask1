import json

from flask import request
from sqlalchemy import desc

from app import db
from app.models import QuizzQuestion
from app.main import bp
from app.serializers import QuizzCategorySerializer, QuizzQuestionSerializer
from app.services import JServiceAPI


@bp.route(
    "/quizzes/",
    methods=[
        "POST",
    ],
)
def get_quizzes_route():
    user_data: dict = json.loads(request.data.decode("utf-8"))
    count: int = user_data.get("question_num")
    questions: list[dict] = list(dict())

    while True:
        try:
            questions: list = JServiceAPI.get_random_quizz_questions(count)
            for question_data in questions:
                # if question already exists in Database
                if (
                    db.session.query(QuizzQuestion)
                    .filter(QuizzQuestion.id == question_data["id"])
                    .one_or_none()
                ):
                    raise ValueError("Database already has this question.")
            break
        except ConnectionError or ValueError:
            continue

    last_question = (
        db.session.query(QuizzQuestion)
        .order_by(desc(QuizzQuestion.local_uploaded_at))
        .first()
    )

    for question_data in questions:
        category_data: dict = question_data.pop("category")

        question = QuizzQuestionSerializer().load(question_data)
        category = QuizzCategorySerializer().load(category_data)

        question.category = category

        db.session.add_all(
            (
                question,
                category,
            )
        )
        db.session.commit()
    return QuizzQuestionSerializer().dumps(last_question), 200
