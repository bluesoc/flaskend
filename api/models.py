from datetime import datetime
from api.database import db


# Table Models
class Roles(db.Model):
    def __init__(self, description=None):
        self.description = description

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    description = db.Column(db.String, nullable=False)


class Claims(db.Model):
    def __init__(self, description=None, active=True):
        self.description = description
        self.active = active

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    description = db.Column(db.String, nullable=False)
    active = db.Column(db.Boolean, default=True, nullable=False)


class Users(db.Model):
    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"), nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)


class UserClaims(db.Model):
    __tablename__ = "user_claims"

    def __init__(self, user_id=None, claim_id=None):
        self.user_id = user_id
        self.claim_id = claim_id

    user_id = db.Column(db.Integer, db.ForeignKey(
        "users.id"), primary_key=True, nullable=False)
    claim_id = db.Column(db.Integer, db.ForeignKey(
        "claims.id"),  primary_key=True, nullable=False)
