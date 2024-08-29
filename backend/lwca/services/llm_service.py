from flask import current_app

from langchain_community.llms.ollama import Ollama


def get_llm_model(model_name=None) -> Ollama:
    """
        Get the LLM model instance from Ollama instance
    """
    if model_name is None:
        model_name = current_app.config.get('OLLAMA_DEFAULT_MODEL')
        
    ollama_base_url = current_app.config.get('OLLAMA_URL')
    
    return Ollama(model=model_name, base_url=ollama_base_url)
