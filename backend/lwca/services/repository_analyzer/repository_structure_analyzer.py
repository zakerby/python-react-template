import json

from pathlib import Path
from collections import deque


def get_repo_structure(repository_path):
    return bfs_folder_search(4000, repository_path)


def bfs_folder_search(text_length_limit=4000, repository_path="./code_repo"):
    """
        Description:
            Perform a breadth-first search on the directory structure of a repository
        Parameters:
            - text_length_limit: the maximum length of the JSON string to return
            - repository_path: the path to the repository to analyze
        Return: 
            - the structure as a JSON string
    """
    if not Path(repository_path).is_dir():
        return "Invalid directory path"

    root = Path(repository_path).resolve()
    file_structure = {str(root): {}}
    queue = deque([(root, file_structure[str(root)])])

    while queue:
        current_dir, parent_node = queue.popleft()
        try:
            for path in current_dir.iterdir():
                if path.is_dir():
                    if str(path.name) == ".git":
                        continue
                    parent_node[str(path.name)] = {"files": []}
                    queue.append((path, parent_node[str(path.name)]))
                else:
                    if "files" not in parent_node:
                        parent_node["files"] = []
                    parent_node["files"].append(str(path.name))

                # Check if we've exceeded the text length limit
                file_structure_text = json.dumps(file_structure)
                if len(file_structure_text) >= text_length_limit:
                    return file_structure_text
        except PermissionError:
            # This can happen in directories the user doesn't have permission to read.
            continue

    return json.dumps(file_structure)
