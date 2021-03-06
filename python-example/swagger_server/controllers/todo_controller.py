import connexion
from flask import current_app, request
from werkzeug.exceptions import BadRequest

from swagger_server.database.models.todo import TodoModel
from swagger_server.models.paginated_response_data import (
    PaginatedResponseData,
)  # noqa: E501
from swagger_server.models.todo import Todo  # noqa: E501
from swagger_server.util import log


@log
def create_todo(body):  # noqa: E501
    """Create a new to-do

    Create a to-do # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    current_app.logger.debug(f"Client IP ADDRESS: {request.remote_addr}")
    if connexion.request.is_json:
        body = Todo.from_dict(connexion.request.get_json())  # noqa: E501
        TodoModel.from_obj(body).save()
        return None, 200
    else:
        raise BadRequest("missing body")


@log
def delete_todo_by_id(todoId):  # noqa: E501
    """Delete existing to-do by Id

    Delete a to-do object if exists # noqa: E501

    :param todoId: 
    :type todoId: str

    :rtype: Todo
    """
    return TodoModel.delete_by_id(todoId)


@log
def get_todo_by_id(todoId):  # noqa: E501
    """Retrieve to-do by Id

    Return a to-do object if exists # noqa: E501

    :param todoId: 
    :type todoId: str

    :rtype: Todo
    """
    return TodoModel.get_by_id(todoId)


@log
def get_todo_list(status=None, page=None, size=None):  # noqa: E501
    """Retrieve list of to-do

    Return a paginated list of to-do objects # noqa: E501

    :param status: filter result on to-do status
    :type status: str
    :param page: Page number
    :type page: int
    :param size: Number of records to return per page
    :type size: int

    :rtype: PaginatedResponseData
    """
    return TodoModel.get_all(page, size, status)


@log
def update_todo_by_id(todoId, body):  # noqa: E501
    """Update existing to-do by Id

    Update a to-do object if exists # noqa: E501

    :param todoId: 
    :type todoId: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Todo.from_dict(connexion.request.get_json())  # noqa: E501
        return TodoModel.update_by_id(todoId, body), 200
    else:
        raise BadRequest("missing body")
