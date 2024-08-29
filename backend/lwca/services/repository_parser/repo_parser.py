# repo_parser: a module dedicated to 
#   - handling the cloning of Git repository
#   - generating knowledge from the repository
#  
import uuid
import shutil
from git import Repo
import localstack_client.session

from lwca.services.repository_analyzer.readme_analyzer import get_readme
from lwca.services.repository_analyzer.repository_structure_analyzer import get_repo_structure

from lwca.logging import log_info, log_error

REPOSITORY_BUCKET = 'repo-bucket'

def s3_client():
    return localstack_client.session.Session().client('s3')


def handle_project_clone_repository(repository_url: str):
    """
        Description:
            Handle the cloning of a repository
        Args:
            - repository_url: The URL of the repository to clone
        Returns:
            - The path to the cloned repository
        """
    repo_folder_name = f'/tmp/repo' + str(uuid.uuid4())
    try:
        Repo.clone_from(repository_url, repo_folder_name)
        log_info('Repository cloned successfully')
        return repo_folder_name
    except Exception as exc:
        log_error('Error while cloning the repository: ', exc)
        raise exc
    
def handle_repository_upload_to_s3(repository_folder_path: str) -> str:
    """
        Description:
            Handle the uploading of a repository to S3
        Args:
            - repo_folder_name: The path to the repository to upload
        Returns:
            - The URL of the uploaded repository
    """
    # First we zip the repository folder
    zipped_repo_path = f'{repository_folder_path}.zip'
    # We zip the repository folder
    shutil.make_archive(zipped_repo_path, 'zip', repository_folder_path)    
    # Then we upload the zipped folder to S3
    s3_client().put_object(Bucket=REPOSITORY_BUCKET,
                            Key=zipped_repo_path,
                            Body=zipped_repo_path)
    # We return the identifier of the uploaded repository
    return zipped_repo_path

def clone_repository(repo_url: str) -> str:
    """
        Description:
            Clone a git repository and return the path to the cloned repository
        Args:
            - repo_url: The URL of the repository to clone and analyze
        Returns:
            - A string containing the information extracted from the repository
    """
    log_info(f"Cloning the repository: {repo_url} ...")
    repo_folder_name = handle_project_clone_repository(repo_url)
    log_info('Summarizing the repository...')

    log_info('Analyzing the README file...')
    readme_info = get_readme(repo_folder_name)
    if readme_info is not None:
        readme_info = f"The README.md file is as follow: {readme_info} \n\n"

    log_info('Parsing the repository...')

    repository_structure = get_repo_structure(repo_folder_name)
    if repository_structure is not None:
        repository_structure = f"The repository structure is as follow: {repository_structure} \n\n"

    return f"{readme_info}{repository_structure}"