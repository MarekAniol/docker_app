# Error messages
BAD_REQUEST_ERROR = "Bad request error."
UNAUTHORIZED_ERROR = "Unauthorize error."
FORBIDDEN_ERROR = "Forbidden error."
NOT_FOUND_ERROR = "Not found error."
CONFLICT_ERROR = "Conflict error."
INTERNAL_SERVER_ERROR = "Internal server error."
SERVICE_UNAVAILABLE_ERROR = "Service unavailable error."
UNABLE_TO_SAVE_ERROR = "Unable to save {} to the database. The data is invalid due to incorrect."
NO_JSON_DATA = "No JSON data in request."
ID_NOT_FOUND = "{} id not found."
RECORD_CANNOT_BE_NULL = "Record cannot be null. Missing: {}."

#DBAPIError messages
INTERFACE_ERROR = "Connection problem with the database interface."
DATABASE_ERROR = "Database operation failed due to an internal database error."
DATA_ERROR = "Data processing error, such as numeric value out of range."
OPERATIONAL_ERROR = "Database operational error, possibly a disconnect or resource not available."
INTEGRITY_ERROR = "Integrity constraint violation, such as a foreign key constraint fails."
INTERNAL_ERROR = "An internal error occurred in the database, such as a transaction sync failure."
PROGRAMMING_ERROR = "Programming error, such as a syntax error in the SQL statement or table not found."
NOTSUPPORTED_ERROR = "Attempted to use a database feature that is not supported."

error_messages = {
    "InterfaceError": INTERFACE_ERROR,
    "DatabaseError": DATABASE_ERROR,
    "DataError": DATA_ERROR,
    "OperationalError": OPERATIONAL_ERROR,
    "IntegrityError": INTEGRITY_ERROR,
    "InternalError": INTERNAL_ERROR,
    "ProgrammingError": PROGRAMMING_ERROR,
    "NotSupportedError": NOTSUPPORTED_ERROR
}


# Success messages
SUCCESS_MESSAGE = "Operation completed successfully."
SUCCESSFUL_ADDED_MESSAGE = "New {} has been successfully added."
SUCCESSFUL_GET_MESSAGE = "Got date successfully."
SUCCESSFUL_DELETE_MESSAGE = "{} deleted successfully."
SUCCESSFUL_UPDATE_MESSAGE = "{} updated successfully."

# Log messages
LOG_ERROR = "Error message: {}, Error type: {}" 


