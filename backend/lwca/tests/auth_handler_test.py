import pytest
import datetime
from unittest.mock import patch, MagicMock
from flask import Flask, jsonify
from http import HTTPStatus
from lwca.handlers.auth_handler import handle_login_user, handle_register_user, handle_jwt_refresh
from lwca.models.user import User

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

@patch('lwca.handlers.auth_handler.User')
@patch('lwca.handlers.auth_handler.create_access_token')
def test_handle_login_user(mock_create_access_token, mock_user, app_context):
    # Test no payload
    response, status = handle_login_user(None)
    assert status == HTTPStatus.BAD_REQUEST
    assert response['message'] == 'No payload provided'

    # Test missing username or password
    response, status = handle_login_user({'username': 'test'})
    assert status == HTTPStatus.BAD_REQUEST
    assert response['message'] == 'Username or password missing'

    # Test user not found
    mock_user.query.filter_by.return_value.first.return_value = None
    response, status = handle_login_user({'username': 'test', 'password': 'test'})
    assert status == HTTPStatus.NOT_FOUND
    assert response['message'] == 'User not found'

    # Test incorrect password
    mock_user_instance = MagicMock()
    mock_user_instance.check_password.return_value = False
    mock_user.query.filter_by.return_value.first.return_value = mock_user_instance
    response, status = handle_login_user({'username': 'test', 'password': 'test'})
    assert status == HTTPStatus.UNAUTHORIZED
    assert response['message'] == 'Incorrect password'

    # Test successful login
    mock_user_instance.check_password.return_value = True
    mock_user_instance.to_dict.return_value = {'id': 1, 'username': 'test'}
    mock_create_access_token.return_value = 'test_token'
    response, status = handle_login_user({'username': 'test', 'password': 'test'})
    assert status == HTTPStatus.OK
    assert response['access_token'] == 'test_token'
    assert response['user']['username'] == 'test'

@patch('lwca.handlers.auth_handler.User')
@patch('lwca.handlers.auth_handler.create_access_token')
def test_handle_register_user(mock_create_access_token, mock_user, app_context):
    # Test no payload
    response, status = handle_register_user(None)
    assert status == HTTPStatus.BAD_REQUEST
    assert response['message'] == 'No payload provided'

    # Test passwords do not match
    response, status = handle_register_user({'username': 'test', 'email': 'test@test.com', 'password': 'test', 'confirm_password': 'test1'})
    assert status == HTTPStatus.BAD_REQUEST
    assert response['message'] == 'Passwords do not match'

    # Test missing username or password
    response, status = handle_register_user({'username': 'test', 'email': 'test@test.com', 'password': 'test'})
    assert status == HTTPStatus.BAD_REQUEST
    assert response['message'] == 'Passwords do not match'

    # Test user already exists
    mock_user.query.filter_by.return_value.first.return_value = MagicMock()
    response, status = handle_register_user({'username': 'test', 'email': 'test@test.com', 'password': 'test', 'confirm_password': 'test'})
    assert status == HTTPStatus.CONFLICT
    assert response['message'] == 'User already exists'

    # Test error creating user
    mock_user.query.filter_by.return_value.first.return_value = None
    mock_user.side_effect = Exception('Database error')
    response, status = handle_register_user({'username': 'test', 'email': 'test@test.com', 'password': 'test', 'confirm_password': 'test'})
    assert status == HTTPStatus.INTERNAL_SERVER_ERROR
    assert 'Error creating user' in response['message']

    # Test successful registration
    mock_user.side_effect = None
    mock_user_instance = MagicMock()
    mock_user.return_value = mock_user_instance
    mock_user_instance.to_dict.return_value = {'id': 1, 'username': 'test'}
    mock_create_access_token.return_value = 'test_token'
    response, status = handle_register_user({'username': 'test', 'email': 'test@test.com', 'password': 'test', 'confirm_password': 'test'})
    assert status == HTTPStatus.OK
    assert response['access_token'] == 'test_token'
    assert response['user']['username'] == 'test'

@patch('lwca.handlers.auth_handler.get_jwt')
@patch('lwca.handlers.auth_handler.get_jwt_identity')
@patch('lwca.handlers.auth_handler.set_access_cookies')
@patch('lwca.handlers.auth_handler.create_access_token')
def test_handle_jwt_refresh(mock_create_access_token, mock_set_access_cookies, mock_get_jwt_identity, mock_get_jwt, app_context):
    # Mock JWT token data
    mock_get_jwt.return_value = {'exp': datetime.datetime.now(datetime.timezone.utc).timestamp() + 60}
    mock_get_jwt_identity.return_value = 1
    mock_create_access_token.return_value = 'new_token'
    response = jsonify({'message': 'test'})
    
    # Test token refresh
    response = handle_jwt_refresh(response)
    mock_set_access_cookies.assert_called_once_with(response, 'new_token')
    assert response.json['message'] == 'test'