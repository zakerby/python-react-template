from flask import current_app as app

def log_info(message):
    app.logger.info(message)

def log_error(message):
    app.logger.error(message)