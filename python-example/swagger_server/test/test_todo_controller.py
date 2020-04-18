# coding: utf-8


from flask import json
from six import BytesIO

from swagger_server.models.paginated_response_data import (
    PaginatedResponseData,
)  # noqa: E501
from swagger_server.models.todo import Todo  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTodoController(BaseTestCase):
    """TodoController integration test stubs"""

    def test_create_todo(self):
        """Test case for create_todo

        Create a new to-do
        """
        body = Todo()
        response = self.client.open(
            "/v1/todo",
            method="POST",
            data=json.dumps(body),
            content_type="application/json",
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_delete_todo_by_id(self):
        """Test case for delete_todo_by_id

        Delete existing to-do by Id
        """
        response = self.client.open(
            "/v1/todo/{todoId}".format(todoId="todoId_example"), method="DELETE"
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_get_todo_by_id(self):
        """Test case for get_todo_by_id

        Retrieve to-do by Id
        """
        response = self.client.open(
            "/v1/todo/{todoId}".format(todoId="todoId_example"), method="GET"
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_get_todo_list(self):
        """Test case for get_todo_list

        Retrieve list of to-do
        """
        query_string = [("status", "status_example"), ("page", 1), ("size", 20)]
        response = self.client.open("/v1/todo", method="GET", query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))

    def test_update_todo_by_id(self):
        """Test case for update_todo_by_id

        Update existing to-do by Id
        """
        body = Todo()
        response = self.client.open(
            "/v1/todo/{todoId}".format(todoId="todoId_example"),
            method="PUT",
            data=json.dumps(body),
            content_type="application/json",
        )
        self.assert200(response, "Response body is : " + response.data.decode("utf-8"))


if __name__ == "__main__":
    import unittest

    unittest.main()
