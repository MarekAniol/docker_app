import logging


db_logger = logging.getLogger("app.database")
db_logger.setLevel(logging.WARNING)
app_logger = logging.getLogger("app.general")
app_logger.setLevel(logging.INFO)
