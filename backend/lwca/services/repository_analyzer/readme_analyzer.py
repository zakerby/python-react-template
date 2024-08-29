import os

from lwca.logging import log_info, log_error

from lwca.services.llm_service import get_llm_model

system_prompt = """
    You are an expert developer and programmer. 
    Please infer the programming languages from the README.
    You are asked to summarize the README file of the code repository in detail.
    Provide enough information about the code repository.
    Please also mention the framework used in the code repository.
"""

def get_readme(repo_path):
    """Get the README file from the repository"""
    log_info(f"Getting the README file {repo_path}")
    readme_path = find_readme(repo_path)
    if readme_path is None:
        return None

    summary = summarize_readme(readme_path)
    log_info(f"Summary of the README file: {summary}")
    return summary

def find_readme(repo_path):
    for filename in os.listdir(repo_path):
        if filename.lower().startswith('readme'):
            readme_path = os.path.join(repo_path, filename)
            log_info(f"README found in folder: {repo_path}")
            return readme_path 
    log_info('README not found in the repository')
    return None
        
def summarize_readme(readme_path):
    """
        Using LLM, make a summary of the README file
    """
    if readme_path:
        log_info(f"Summarizing the README file: {readme_path}")
        try:
            with open(readme_path, 'r') as readme_file:
                readme_content = readme_file.read()
                log_info(f"Content of the README file: {readme_content}")
                user_prompt = f"Here is the README content: ${readme_content}"
                response = get_llm_model().invoke(f"{system_prompt} {user_prompt}")
                log_info(f"Response from the LLM model: {response}")
        except FileNotFoundError as fnf_error:
            log_error(f"File not found: {readme_path}")
            raise fnf_error
        except IOError as io_error:
            log_error(f"An I/O error occured while reading the README file: {readme_path}")
            raise io_error
        except Exception as e:
            log_error(f"Error while summarizing the README file: {readme_path}", e)
            raise e
