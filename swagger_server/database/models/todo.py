import enum

from swagger_server.database import db
from swagger_server.models import Todo


class Status(enum.Enum):
    done = "done"
    late = "late"
    in_progress = "in progress"
    to_do = "to do"


class TodoModel(db.Model):
    __tablename__ = "todo"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.string(256), nullable=True)
    due_date = db.Column(db.Date, nullable=True)
    status = db.Column(db.Enum(Status), nullable=False)

    def to_dict(self) -> Todo:
        pass

    def __repr__(self):
        return '<Todo %r>' % self.name
