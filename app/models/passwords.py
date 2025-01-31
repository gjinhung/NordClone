from .db import db, environment, SCHEMA, add_prefix_for_prod


class Password(db.Model):
    __tablename__ = "passwords"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    website = db.Column(db.String(255), nullable=True, unique=False)
    emailUser = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("tours.id")))
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=True, unique=False)

    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False)

    user = db.relationship("User", back_populates="passwords")

    def to_dict(self):
        return {
            "id": self.id,
            "website": self.website,
            "emailUser": self.emailUser,
            "user_id": self.user_id,
            "password": self.password,
            "name": self.name,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
