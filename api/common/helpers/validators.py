from flask import jsonify
from static.messages import RECORD_CANNOT_BE_NULL, ID_MISMATCH_ERROR_MESSAGE
from common.errors.custom_errors import ValidationError


def validate_required_fields(data, required_fields):
    missing_fields = [field for field in required_fields if data.get(field) is None]
    if missing_fields:
        entity_type = " and ".join(missing_fields)
        raise ValidationError(entity_type=entity_type, message=RECORD_CANNOT_BE_NULL, status_code=400)
        
    
def validate_matching_ids(id, model, id_field):
    model_id = model.get(id_field)
    if id != model_id:
        raise ValidationError(message=ID_MISMATCH_ERROR_MESSAGE, status_code=400)
    