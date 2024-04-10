from common.models.db_models import Customer, db
from common.errors.custom_error_handlers import ValidationError , JsonDataError
from common.logs import loggers as log
from common.helpers.entity_types import EntityType as type
from common.helpers import successful_handlers as sh
from flask import abort


def add_customer(customer_data):
    if not customer_data:
        log.db_logger.error
        raise JsonDataError()
    
    new_customer = Customer(
            customer_id=customer_data['customer_id'],
            company_name=customer_data['company_name'],
            contact_name=customer_data.get('contact_name'),
            contact_title=customer_data.get('contact_title'),
            address=customer_data.get('address'),
            city=customer_data.get('city'),
            region=customer_data.get('region'),
            postal_code=customer_data.get('postal_code'),
            country=customer_data.get('country'),
            phone=customer_data.get('phone'),
            fax=customer_data.get('fax'),
            login=customer_data.get('login'),
            password_hash=customer_data.get('password_hash'),
            role_id=customer_data.get('role_id')
        )
    db.session.add(new_customer)
    try:
        db.session.commit()
        return sh.db_commit_success(type.CUSTOMER), 201 
    except Exception as e:
        db.session.rollback()
        raise ValidationError (entity_type=type.CUSTOMER, errors=str(e))