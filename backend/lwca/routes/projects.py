from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from flasgger import swag_from

from lwca.handlers.projects_handler import handle_create_project, handle_get_projects, handle_delete_project, handle_get_project, handle_update_project

blueprint = Blueprint('projects', __name__)

@blueprint.route('/api/v1/projects', methods=['POST'])
@jwt_required()
@swag_from('../docs/projects/create_project.yml')
def create_project():
    """
    Create a new project.
    ---
    """
    if request.method == 'POST':
        payload = request.json
        message, error_code = handle_create_project(payload)
        return jsonify(message), error_code
    
@blueprint.route('/api/v1/projects/', methods=['GET'])
@jwt_required()
@swag_from('../docs/projects/get_projects.yml')
def get_projects():
    """
    Get all projects.
    ---
    """
    if request.method == 'GET':
        projects_list, error_code = handle_get_projects()
        return jsonify(projects_list), error_code

@blueprint.route('/api/v1/project/<int:project_id>', methods=['GET'])
@jwt_required()
@swag_from('../docs/projects/get_project.yml')
def get_project(project_id):
    """
    Get a specific project by ID.
    ---
    """
    if request.method == 'GET':
        project, error_code = handle_get_project(project_id)
        return jsonify(project), error_code

@blueprint.route('/api/v1/project/<int:project_id>', methods=['DELETE'])
@jwt_required()
@swag_from('../docs/projects/delete_project.yml')
def delete_project(project_id):
    """
    Delete a project by ID.
    ---
    """
    if request.method == 'DELETE':
        message, error_code = handle_delete_project(project_id)
        return jsonify(message), error_code


@blueprint.route('/api/v1/project/<int:project_id>', methods=['PUT'])
@jwt_required()
@swag_from('../docs/projects/update_project.yml')
def update_project(project_id):
    """
    Update a project by ID.
    ---
    """
    if request.method == 'PUT':
        payload = request.json
        message, error_code = handle_update_project(project_id, payload)
        return jsonify(message), error_code