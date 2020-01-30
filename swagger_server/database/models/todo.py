import enum

from swagger_server.database import db
from swagger_server.models import Todo, PaginatedResponseData


class Status(enum.Enum):
    done = "done"
    late = "late"
    in_progress = "in progress"
    to_do = "to do"


class TodoModel(db.Model):
    __tablename__ = "todo"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(256), nullable=True)
    due_date = db.Column(db.Date, nullable=True)
    status = db.Column(db.Enum(Status), nullable=False)

    def to_obj(self) -> Todo:
        return Todo(
            id=self.id,
            name=self.name,
            description=self.description,
            due_date=self.due_date,
            status=self.status,
        )

    def __repr__(self):
        return "<Todo %r>" % self.name

    @classmethod
    def from_obj(cls, obj: Todo) -> "TodoModel":
        return cls(
            id=obj.id,
            name=obj.name,
            description=obj.description,
            due_date=obj.due_date,
            status=obj.status,
        )

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all(
            cls,
            page: int = 1,
            size: int = 20,
            status: dict = None
    ):
        query = cls.query.filter_by(**status).paginate(page, size, False)
        total = query.total
        items = query.items
        return PaginatedResponseData(
            page=page,
            size=size,
            total=total,
            count=len(items),
            resources=[i.to_obj() for i in items],
        )

    @classmethod
    def get_by_id(cls, _id: str) -> Todo:
        res = cls.query.filter_by(id=_id).first_or_404()
        return res.to_obj()

    @classmethod
    def update_by_id(cls, _id: str, body: Todo):
        _ = cls.query.filter_by(id=_id).first_or_404()
        cls.from_obj(body).save()

    @classmethod
    def delete_by_id(cls, _id: str):
        res = cls.query.filter_by(id=_id).first_or_404()
        db.session.delete(res)
        db.session.commit()
        return res.to_obj()
