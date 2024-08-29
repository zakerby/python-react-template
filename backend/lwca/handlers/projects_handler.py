import random

from flask_jwt_extended import get_jwt_identity
from http import HTTPStatus

from lwca.models.project import Project
from lwca.services.llm_service import get_llm_model
from lwca.services.repository_parser.repo_parser import clone_repository

from lwca.logging import log_info

from lwca.handlers.constants import (
    PROJECT_CREATED,
    ERROR_SAVING_PROJECT,
    NAME_OR_REPOSITORY_URL_MISSING,
    PROJECT_NOT_FOUND,
    PROJECT_DELETED,
    ERROR_DURING_ANALYSIS,
    NO_FILES_OR_REPOSITORY_URL_PROVIDED,
    NO_QUERY_PROVIDED,
    NO_PAYLOAD_PROVIDED
)

def handle_create_project(data):
    """
        Handle the creation of a project
        Description:
            - The function check if the payload contains the keys 'name' and 'repository_url'
            - If the payload is correct, it creates a new project in the database
    """
    if data is not None:
        name = data.get('name')
        repository_url = data.get('repository_url')
        if name is not None and repository_url is not None:
            try:
                current_user_id = get_jwt_identity()
                project = Project(name=name, repository_url=repository_url, analysis_status='pending', user_id=current_user_id)
                project.save()
                return {'message': PROJECT_CREATED, 'project': project.to_dict()}, HTTPStatus.CREATED
            except Exception as e:
                return {'message': ERROR_SAVING_PROJECT.format(str(e))}, HTTPStatus.INTERNAL_SERVER_ERROR
        else:
            return {'message': NAME_OR_REPOSITORY_URL_MISSING}, HTTPStatus.BAD_REQUEST
    else:
        return {'message': NO_PAYLOAD_PROVIDED}, HTTPStatus.BAD_REQUEST

def handle_get_projects():
    """
        Handle the retrieval of all projects
        Description:
            - The function retrieves all projects from the database
    """
    current_user_id = get_jwt_identity()
    projects = Project.query.filter_by(user_id=current_user_id).all()
    projects_list = []
    for project in projects:
        projects_list.append({
            'id': project.id,
            'name': project.name,
            'repository_url': project.repository_url,
            'analysis_status': project.analysis_status,
            'analysis_results': project.analysis_results
        })
    return projects_list, HTTPStatus.OK

def handle_get_project(project_id):
    """
        Handle the retrieval of a project
        Description:
            - The function retrieves a project from the database
    """
    current_user_id = get_jwt_identity()
    
    project = Project.query.filter_by(id=project_id, user_id=current_user_id).first()
    if project is not None:
        return {
            'id': project.id,
            'name': project.name,
            'repository_url': project.repository_url,
            'analysis_status': project.analysis_status,
            'analysis_results': project.analysis_results
        }, HTTPStatus.OK
    else:
        return {'message': PROJECT_NOT_FOUND}, HTTPStatus.NOT_FOUND

def handle_delete_project(project_id):
    """
        Handle the deletion of a project
        Description:
            - The function deletes a project from the database
    """
    current_user_id = get_jwt_identity()
    project = Project.query.filter_by(id=project_id, user_id=current_user_id).first()
    if project is not None:
        project.delete()
        return {'message': PROJECT_DELETED}, HTTPStatus.OK
    else:
        return {'message': PROJECT_NOT_FOUND}, HTTPStatus.NOT_FOUND

def handle_project_analysis(project_id):
    """
        Execute a repository analysis
        Parameters:
            - data (dict): JSON payload.
                           This payload must contains a key 'repo_url' with the URL of the repository to analyze.
    """
    project = Project.query.filter_by(id=project_id).first()
    if project is not None:
        repo_url = project.repository_url
        if repo_url is not None:
            # first check if the repository has already been cloned and analyzed with the current commit
            try:
                repository_infos = clone_repository(repo_url)
                return {'repository_infos': repository_infos}, HTTPStatus.OK
            except Exception as e:
                return {'message': ERROR_DURING_ANALYSIS.format(str(e))}, HTTPStatus.INTERNAL_SERVER_ERROR
        else:
            return {'message': NO_FILES_OR_REPOSITORY_URL_PROVIDED}, HTTPStatus.BAD_REQUEST
    else:
        return {'message': PROJECT_NOT_FOUND}, HTTPStatus.NOT_FOUND

def handle_project_analysis_logs(project_id):
    """
        Get the logs of the analysis of a project
    """
    project = Project.query.filter_by(id=project_id).first()
    if project is not None:
        return {'logs': project.analysis_logs}, HTTPStatus.OK
    else:
        return {'message': PROJECT_NOT_FOUND}, HTTPStatus.NOT_FOUND

def handle_query_llm(project_id, data):
    """
        Send a query to the LLM model
    """
    project = Project.query.filter_by(id=project_id).first()
    if data is not None:
        query = data.get('query')
        if query is not None:
            try:
                response_message = get_llm_model().invoke(query)
                message = {
                    # random id for now
                    'id': random.randint(0, 1000),
                    'project_id': project.id,
                    'message': response_message,
                    'user': {
                        'id': -1,
                        'name': 'Robot'
                    }
                }
                return {'message': message}, HTTPStatus.OK
            except Exception as e:
                return {'message': str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR
        else:
            return {'message': NO_QUERY_PROVIDED}, HTTPStatus.BAD_REQUEST
    else:
        return {'message': NO_PAYLOAD_PROVIDED}, HTTPStatus.BAD_REQUEST