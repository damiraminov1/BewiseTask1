from app import ma

from app.models import QuizzQuestion, QuizzCategory


class QuizzQuestionSerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = QuizzQuestion
        include_relationships = True
        load_instance = True
        unknown = "exclude"


class QuizzCategorySerializer(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = QuizzCategory
        include_relationships = True
        load_instance = True
        unknown = "exclude"
