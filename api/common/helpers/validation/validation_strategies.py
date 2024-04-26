from abc import ABC, abstractmethod
from static.messages import ID_NOT_FOUND, RECORD_CANNOT_BE_NULL, ID_MISMATCH_ERROR_MESSAGE
from common.errors.custom_errors import JsonEmptyDataError, ValidationError
from common.logs import loggers as log


class ValidationStrategy(ABC):
    @abstractmethod
    def validate(self, data):
        log.db_logger.error("Error: %s",str(data))

class ValidateRequiredFields(ValidationStrategy):
    def __init__(self, required_fields):
        self.required_fields = required_fields

    def validate(self, data):
        if not isinstance(data, dict):
            raise TypeError("Expected a dictionary")
        missing_fields = [field for field in self.required_fields if data.get(field) is None]
        if missing_fields:
            entity_type = " and ".join(missing_fields)
            raise ValidationError(
                entity_type=entity_type,
                message=RECORD_CANNOT_BE_NULL,
                status_code=400
            )

class ValidateMatchingIDs(ValidationStrategy):
    def __init__(self, id_field):
        self.id_field = id_field

    def validate(self, data):
        model_id = data.get(self.id_field)
        if self.id_field != model_id:
            raise ValidationError(message=ID_MISMATCH_ERROR_MESSAGE, status_code=400)

class ValidatePresentID(ValidationStrategy):
    def __init__(self, id_field, entity_type):
        self.id_field = id_field
        self.entity_type = entity_type

    def validate(self, data):
        if self.id_field not in data or data[self.id_field] is None:
            raise ValidationError(
                entity_type=self.entity_type,
                message=ID_NOT_FOUND,
                status_code=404
            )

class ValidateExistingRecord(ValidationStrategy):
    def __init__(self, entity_type):
        self.entity_type = entity_type

    def validate(self, data):
        if not data:
            raise ValidationError(
                entity_type=self.entity_type,
                message=ID_NOT_FOUND,
                status_code=404
            )

class ValidatePresentJsonObject(ValidationStrategy):
    def validate(self, data):
        if not data:
            raise JsonEmptyDataError()
