from celery import current_app, shared_task

from lwca.models.project import Project

from lwca.services.repository_parser.repo_parser import handle_project_clone_repository, handle_repository_upload_to_s3

@shared_task(ignore_result=False)
def handle_analysis(project_id):
    project = Project.query.filter_by(id=project_id).first()
    if project is None:
        return {'message': 'project not found'}, 404
    project.analysis_status = 'running'
    
    # first we clone the repository
    repository_folder_path = handle_project_clone_repository(project.repository_url)
    
    # Then we upload it to S3 (localstack)
    uploaded_repo_name = handle_repository_upload_to_s3(repository_folder_path)