from datetime import datetime
from email.policy import default
from api.models.db import db

class Classic(db.Model):
    __tablename__ = 'classics'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    category = db.Column(db.String(100))
    description = db.Column(db.String(250))
    image = db.Column(db.String(250),default='Image URL')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    profile_id = db.Column(db.Integer, db.ForeignKey('profiles.id'))

    def __repr__(self):
      return f"Classic('{self.id}', '{self.name}'"

    def serialize(self):
      classic = {c.name: getattr(self, c.name) for c in self.__table__.columns}
      return classic