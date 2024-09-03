from flask_jwt_extended import get_jwt_identity
from http import HTTPStatus

from lwca.models.project import Project

from lwca.logging import log_info, log_error

from lwca.handlers.constants import (
    PROJECT_CREATED,
    ERROR_SAVING_PROJECT,
    NAME_OR_REPOSITORY_URL_MISSING,
    PROJECT_NOT_FOUND,
    PROJECT_DELETED,
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
        if name is not None:
            try:
                current_user_id = get_jwt_identity()
                project = Project(name=name, user_id=current_user_id)
                project.save()
                log_info(f'Project {project.name} created by user {current_user_id}')
                return {'message': PROJECT_CREATED, 'project': project.to_dict()}, HTTPStatus.CREATED
            except Exception as e:
                log_error(f'Error saving project: {str(e)}')
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
        try:
            project.delete()
            log_info(f'Project {project.name} deleted by user {current_user_id}')
            return {'message': PROJECT_DELETED}, HTTPStatus.OK
        except Exception as e:
            log_error(f'Error deleting project: {str(e)}')
            return {'message': str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR
    else:
        return {'message': PROJECT_NOT_FOUND}, HTTPStatus.NOT_FOUND
    
def handle_update_project(project_id, data):
    """
        Handle the update of a project
        Description:
            - The function updates a project in the database
    """
    current_user_id = get_jwt_identity()
    project = Project.query.filter_by(id=project_id, user_id=current_user_id).first()
    if project is not None:
        if data is not None:        
            project.name = data.get('name', project.name)
            project.repository_url = data.get('repository_url', project.repository_url)
            project.analysis_status = data.get('analysis_status', project.analysis_status)
            project.analysis_results = data.get('analysis_results', project.analysis_results)
            try:
                project.save()
                return {'message': 'Project updated', 'project': project.to_dict()}, HTTPStatus.OK
            except Exception as e:
                return {'message': str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR
        return {'message': NO_PAYLOAD_PROVIDED}, HTTPStatus.BAD_REQUEST
    else:
        return {'message': PROJECT_NOT_FOUND}, HTTPStatus.NOT_FOUND