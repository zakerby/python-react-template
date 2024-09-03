import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from http import HTTPStatus
from lwca.handlers.projects_handler import (
    handle_create_project,
    handle_get_projects,
    handle_get_project,
    handle_delete_project,
    handle_update_project
)
from lwca.handlers.constants import (
    PROJECT_NAME_MISSING,
    NO_PAYLOAD_PROVIDED,
    PROJECT_DELETED
)
from lwca.models.project import Project

@pytest.fixture
def app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'test_secret_key'
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def app_context(app):
    with app.app_context():
        yield

@patch('lwca.handlers.projects_handler.get_jwt_identity')
@patch('lwca.handlers.projects_handler.Project')
def test_handle_create_project(mock_project, mock_get_jwt_identity, app_context):
    mock_get_jwt_identity.return_value = 1

    # Test no payload
    response, status = handle_create_project(None)
    assert status == HTTPStatus.BAD_REQUEST
    assert response['message'] == NO_PAYLOAD_PROVIDED

    # Test missing name
    response, status = handle_create_project({'toto': 'test'})
    assert status == HTTPStatus.BAD_REQUEST
    assert response['message'] == PROJECT_NAME_MISSING

    # Test error saving project
    mock_project.side_effect = Exception('Database error')
    response, status = handle_create_project({'name': 'test'})
    assert status == HTTPStatus.INTERNAL_SERVER_ERROR
    assert 'Database error' in response['message']

    # Test successful project creation
    mock_project.side_effect = None
    mock_project_instance = MagicMock()
    mock_project.return_value = mock_project_instance
    mock_project_instance.to_dict.return_value = {'id': 1, 'name': 'test'}
    response, status = handle_create_project({'name': 'test'})
    assert status == HTTPStatus.CREATED
    assert response['message'] == 'Project created'
    assert response['project']['name'] == 'test'

@patch('lwca.handlers.projects_handler.get_jwt_identity')
@patch('lwca.handlers.projects_handler.Project')
def test_handle_get_projects(mock_project, mock_get_jwt_identity, app_context):
    mock_get_jwt_identity.return_value = 1
    

    # Test retrieving all projects
    first_mock_project = MagicMock()
    first_mock_project.id = 1
    first_mock_project.name = 'test1'
    
    second_mock_project = MagicMock()
    second_mock_project.id = 2
    second_mock_project.name = 'test2'
    
    mock_project.query.filter_by.return_value.all.return_value = [
        first_mock_project,
        second_mock_project
    ]
    response, status = handle_get_projects()
    assert status == HTTPStatus.OK
    assert len(response) == 2
    assert response[0]['name'] == 'test1'
    assert response[1]['name'] == 'test2'

@patch('lwca.handlers.projects_handler.get_jwt_identity')
@patch('lwca.handlers.projects_handler.Project')
def test_handle_get_project(mock_project, mock_get_jwt_identity, app_context):
    mock_get_jwt_identity.return_value = 1

    # Test project not found
    mock_project.query.filter_by.return_value.first.return_value = None
    response, status = handle_get_project(1)
    assert status == HTTPStatus.NOT_FOUND
    assert response['message'] == 'Project not found'

    # Test successful project retrieval
    mock_project_instance = MagicMock()
    mock_project_instance.id = 1
    mock_project_instance.name = 'test'
    mock_project.query.filter_by.return_value.first.return_value = mock_project_instance
    
    response, status = handle_get_project(1)
    assert status == HTTPStatus.OK
    assert response['name'] == 'test'

@patch('lwca.handlers.projects_handler.get_jwt_identity')
@patch('lwca.handlers.projects_handler.Project')
def test_handle_delete_project(mock_project, mock_get_jwt_identity, app_context):
    mock_get_jwt_identity.return_value = 1

    # Test project not found
    mock_project.query.filter_by.return_value.first.return_value = None
    response, status = handle_delete_project(1)
    assert status == HTTPStatus.NOT_FOUND
    assert response['message'] == 'Project not found'

    # Test error deleting project
    mock_project_instance = MagicMock()
    mock_project_instance.delete.side_effect = Exception('Database error')
    mock_project.query.filter_by.return_value.first.return_value = mock_project_instance
    response, status = handle_delete_project(1)
    assert status == HTTPStatus.INTERNAL_SERVER_ERROR
    assert 'Database error' in response['message']

    # Test successful project deletion
    mock_project_instance.delete.side_effect = None
    response, status = handle_delete_project(1)
    assert status == HTTPStatus.OK
    assert response['message'] == PROJECT_DELETED

@patch('lwca.handlers.projects_handler.get_jwt_identity')
@patch('lwca.handlers.projects_handler.Project')
def test_handle_update_project(mock_project, mock_get_jwt_identity, app_context):
    mock_get_jwt_identity.return_value = 1

    # Test project not found
    mock_project.query.filter_by.return_value.first.return_value = None
    response, status = handle_update_project(1, {'name': 'updated'})
    assert status == HTTPStatus.NOT_FOUND
    assert response['message'] == 'Project not found'

    # Test no payload
    mock_project_instance = MagicMock()
    mock_project.query.filter_by.return_value.first.return_value = mock_project_instance
    response, status = handle_update_project(1, None)
    assert status == HTTPStatus.BAD_REQUEST
    assert response['message'] == NO_PAYLOAD_PROVIDED

    # Test error updating project
    mock_project_instance.save.side_effect = Exception('Database error')
    response, status = handle_update_project(1, {'name': 'updated'})
    assert status == HTTPStatus.INTERNAL_SERVER_ERROR
    assert 'Database error' in response['message']

    # Test successful project update
    mock_project_instance.save.side_effect = None
    mock_project_instance.to_dict.return_value = {'id': 1, 'name': 'updated'}
    response, status = handle_update_project(1, {'name': 'updated'})
    assert status == HTTPStatus.OK
    assert response['message'] == 'Project updated'
    assert response['project']['name'] == 'updated'