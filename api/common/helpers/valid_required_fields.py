from static.messages import RECORD_CANNOT_BE_NULL
from common.errors.custom_errors import ValidationError


def validate_required_fields(data, required_fields):
    missing_fields = [field for field in required_fields if data.get(field) is None]
    if missing_fields:
        entity_type = " and ".join(missing_fields)
        raise ValidationError(entity_type=entity_type, message=RECORD_CANNOT_BE_NULL)