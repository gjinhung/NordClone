from .db import db, environment, SCHEMA, add_prefix_for_prod
from werkzeug.security import generate_password_hash, check_password_hash


class Password(db.Model):
    __tablename__ = "passwords"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    website = db.Column(db.String(255), nullable=True, unique=False)
    emailUser = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("tours.id")))
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)

    user = db.relationship("User", back_populates="passwords")

    def to_dict(self):
        return {
            "id": self.id,
            "reviewer_id": self.reviewer_id,
            # "tour_id": self.tour_id,
            "guide_id": self.guide_id,
            "communication_rating": self.communication_rating,
            "knowledgeability_rating": self.knowledgeability_rating,
            "professionalism_rating": self.professionalism_rating,
            "rating": self.rating,
            "review_body": self.review_body,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {"id": self.id, "username": self.username, "email": self.email}
