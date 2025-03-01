from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from lwca.handlers.projects_handler import handle_create_project, handle_get_projects, handle_delete_project, handle_get_project, handle_update_project

blueprint = Blueprint('projects', __name__)

@blueprint.route('/api/v1/projects', methods=['POST'])
@jwt_required()
def create_project():
    """
    Create a new project.
    ---
    tags:
      - Projects
    description: Creates a new project. Requires a valid JWT token.
    security:
      - JWT: []
    parameters:
      - in: body
        name: project_data
        description: Project details.
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              example: My Project
            description:
              type: string
              example: A description of my project.
    responses:
      201:
        description: Project created successfully.
        schema:
          type: object
          properties:
            message:
              type: string
              example: Project created successfully.
      400:
        description: Bad request.
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Invalid input."
      401:
        description: Unauthorized.
        schema:
          type: object
          properties:
            message:
              type: string
              example: Missing Authorization Header
      500:
        description: Internal server error.
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Failed to create project"
    """
    if request.method == 'POST':
        payload = request.json
        message, error_code = handle_create_project(payload)
        return jsonify(message), error_code
    
@blueprint.route('/api/v1/projects/', methods=['GET'])
@jwt_required()
def get_projects():
    """
    Get all projects.
    ---
    tags:
      - Projects
    description: Returns a list of all projects. Requires a valid JWT token.
    security:
      - JWT: []
    responses:
      200:
        description: A list of projects.
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
              name:
                type: string
                example: My Project
              description:
                type: string
                example: A description of my project.
      401:
        description: Unauthorized.
        schema:
          type: object
          properties:
            message:
              type: string
              example: Missing Authorization Header
      500:
        description: Internal server error.
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Failed to retrieve projects"
    """
    if request.method == 'GET':
        projects_list, error_code = handle_get_projects()
        return jsonify(projects_list), error_code

@blueprint.route('/api/v1/project/<int:project_id>', methods=['GET'])
@jwt_required()
def get_project(project_id):
    """
    Get a specific project by ID.
    ---
    tags:
      - Projects
    description: Returns a project by its ID. Requires a valid JWT token.
    security:
      - JWT: []
    parameters:
      - in: path
        name: project_id
        description: ID of the project to retrieve.
        required: true
        type: integer
    responses:
      200:
        description: The requested project.
        schema:
          type: object
          properties:
            id:
              type: integer
              example: 1
            name:
              type: string
              example: My Project
            description:
              type: string
              example: A description of my project.
      401:
        description: Unauthorized.
        schema:
          type: object
          properties:
            message:
              type: string
              example: Missing Authorization Header
      404:
        description: Project not found.
        schema:
          type: object
          properties:
            message:
              type: string
              example: Project not found
      500:
        description: Internal server error.
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Failed to retrieve project"
    """
    if request.method == 'GET':
        project, error_code = handle_get_project(project_id)
        return jsonify(project), error_code

@blueprint.route('/api/v1/project/<int:project_id>', methods=['DELETE'])
@jwt_required()
def delete_project(project_id):
    """
    Delete a project by ID.
    ---
    tags:
      - Projects
    description: Deletes a project by its ID. Requires a valid JWT token.
    security:
      - JWT: []
    parameters:
      - in: path
        name: project_id
        description: ID of the project to delete.
        required: true
        type: integer
    responses:
      200:
        description: Project deleted successfully.
        schema:
          type: object
          properties:
            message:
              type: string
              example: Project deleted successfully.
      401:
        description: Unauthorized.
        schema:
          type: object
          properties:
            message:
              type: string
              example: Missing Authorization Header
      404:
        description: Project not found.
        schema:
          type: object
          properties:
            message:
              type: string
              example: Project not found
      500:
        description: Internal server error.
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Failed to delete project"
    """
    if request.method == 'DELETE':
        message, error_code = handle_delete_project(project_id)
        return jsonify(message), error_code


@blueprint.route('/api/v1/project/<int:project_id>', methods=['PATCH'])
@jwt_required()
def update_project(project_id):
    """
    Update a project by ID.
    ---
    tags:
      - Projects
    description: Updates a project by its ID.
    security:
      - JWT: []
    parameters:
      - in: path
        name: project_id
        description: ID of the project to update.
        required: true
        type: integer
      - in: body
        name: project_data
        description: Project details to update.
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              example: Updated Project Name
            description:
              type: string
              example: Updated project description.
    responses:
      200:
        description: Project updated successfully.
        schema:
          type: object
          properties:
            message:
              type: string
              example: Project updated successfully.
      400:
        description: Bad request.
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Invalid input."
      404:
        description: Project not found.
        schema:
          type: object
          properties:
            message:
              type: string
              example: Project not found
      500:
        description: Internal server error.
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Failed to update project"
    """
    if request.method == 'PATCH':
        payload = request.json
        message, error_code = handle_update_project(project_id, payload)
        return jsonify(message), error_code