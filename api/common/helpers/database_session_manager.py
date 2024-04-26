from sqlalchemy.exc import DBAPIError

class DatabaseSessionManager:
    def __init__(self, db):
        self.db = db

    def commit(self):
        try:
            self.db.session.commit()
        except DBAPIError as e:
            self.db.session.rollback()
            raise e

    def delete(self, record):
        try:
            self.db.session.delete(record)
            self.commit()
        except DBAPIError as e:
            self.db.session.rollback()
            raise e
