import shutil
import uuid

import localstack_client.session

BUCKET = 'repo-bucket'


def s3_client():
    return localstack_client.session.Session().client('s3')


def save_folder_to_file_storage(folder_path: str):
    """
    """
    zip_file_name = 'zipped_folder' + str(uuid.uuid4())
    shutil.make_archive(zip_file_name, 'zip', folder_path)

    s3_client().upload_file(zip_file_name, BUCKET, zip_file_name)

