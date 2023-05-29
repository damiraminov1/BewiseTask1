from app import db


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())


class QuizzQuestion(Base):
    question = db.Column(db.String)
    answer = db.Column(db.String)
    value = db.Column(db.Integer)
    airdate = db.Column(db.DateTime)
    game_id = db.Column(db.Integer)
    invalid_count = db.Column(db.Integer)
    local_uploaded_at = db.Column(db.DateTime, default=db.func.now())

    category_id = db.Column(db.Integer, db.ForeignKey("quizz_category.id"))
    category = db.relationship(
        "QuizzCategory", backref=db.backref("questions", lazy=True)
    )

    def __repr__(self):
        return f"<QuizzQuestion {self.question}>"


class QuizzCategory(Base):
    title = db.Column(db.String)
    clues_count = db.Column(db.Integer)

    def __repr__(self):
        return f"QuizzCategory {self.title}"
