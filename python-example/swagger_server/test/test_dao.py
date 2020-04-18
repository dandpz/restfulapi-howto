from datetime import datetime
import random

import werkzeug
from sqlalchemy import text

from swagger_server.database import db
from swagger_server.database.models.todo import TodoModel, Status
from swagger_server.test import BaseTestCase


class TestDaoController(BaseTestCase):
    def _insert_record(self) -> int:
        _id = random.randint(1, 15)
        sql = text(
            f"""
                        INSERT INTO todo 
                        VALUES ({_id}, 'test-{_id}', 'some text', '{str(datetime.now().strftime('%Y-%m-%d'))}', 'done');
                        """
        )
        db.session.execute(sql)
        return _id

    def setUp(self):
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_save_todo_create_a_record_inside_db(self):
        test_todo = TodoModel(
            name="test_name",
            description="some desc",
            due_date=datetime.utcnow(),
            status=Status("to do"),
        )
        test_todo.save()
        raw = text("select * from todo where name = '{}'".format("test_name"))
        result = db.session.execute(raw)
        results = []
        for r in result:
            results.append(r)
            self.assertTrue(r["name"] == "test_name")
        self.assertTrue(len(results) == 1)

    def test_retrieve_todo_list(self):
        for i in range(5):
            sql = text(
                f"""
                INSERT INTO todo 
                VALUES ({i + 1}, 'test-{i}', 'some text', '{str(datetime.now().strftime('%Y-%m-%d'))}', 'done');
                """
            )
            db.session.execute(sql)

        res = TodoModel.get_all().resources
        self.assertEqual(len(res), 5)

    def test_get_by_id_exists(self):
        _id = self._insert_record()
        res = TodoModel.get_by_id(_id)
        self.assertEqual(res.id, _id)

    def test_get_by_id_raises(self):
        with self.assertRaises(werkzeug.exceptions.NotFound):
            TodoModel.get_by_id(str(1))

    def test_delete_by_id_exists(self):
        _id = self._insert_record()
        res = TodoModel.delete_by_id(_id)
        self.assertEqual(res.id, _id)

    def test_delete_by_id_raises(self):
        with self.assertRaises(werkzeug.exceptions.NotFound):
            TodoModel.delete_by_id(str(1))

    def test_update_by_id_exists(self):
        _id = self._insert_record()
        res = TodoModel.update_by_id(
            _id,
            TodoModel(
                name="test_name",
                description="some desc",
                due_date=datetime.utcnow(),
                status=Status("to do"),
            ),
        )
        self.assertIs(res, None)

    def test_update_by_id_raises(self):
        with self.assertRaises(werkzeug.exceptions.NotFound):
            TodoModel.update_by_id(str(1), {})


if __name__ == "__main__":
    import unittest

    unittest.main()
