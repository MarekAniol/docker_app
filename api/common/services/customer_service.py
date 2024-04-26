from common.helpers.database_session_manager import DatabaseSessionManager
from common.helpers.validation.data_validator import data_validator
from common.helpers.validation.validation_strategies import (
    ValidateExistingRecord,
    ValidateMatchingIDs,
    ValidatePresentJsonObject,
    ValidateRequiredFields,
)
from common.models.db_models import Customer, db
from common.errors.custom_error_handlers import ValidationError, JsonEmptyDataError
from common.helpers.entity_types import EntityType, HttpMethodType
from common.helpers import successful_handlers as sh


def add_customer(customer_data: Customer):
    if not customer_data:
        raise JsonEmptyDataError()

    data_validator.set_strategy(ValidateRequiredFields(["customer_id", "company_name"]))
    data_validator.validate(customer_data)

    new_customer = Customer(
        customer_id=customer_data["customer_id"],
        company_name=customer_data["company_name"],
        contact_name=customer_data.get("contact_name"),
        contact_title=customer_data.get("contact_title"),
        address=customer_data.get("address"),
        city=customer_data.get("city"),
        region=customer_data.get("region"),
        postal_code=customer_data.get("postal_code"),
        country=customer_data.get("country"),
        phone=customer_data.get("phone"),
        fax=customer_data.get("fax"),
        login=customer_data.get("login"),
        password_hash=customer_data.get("password_hash"),
        role_id=customer_data.get("role_id"),
    )

    try:
        db.session.add(new_customer)
        db.session.commit()
        return sh.db_commit_success(HttpMethodType.POST, EntityType.CUSTOMER)
    except ValidationError as e:
        db.session.rollback()
        raise ValidationError(entity_type=EntityType.CUSTOMER) from e


def delete_customer(customer_id):
    customer = Customer.query.get(customer_id)
    data_validator.set_strategy(ValidateExistingRecord(EntityType.CUSTOMER))
    data_validator.validate(customer)

    db_manager = DatabaseSessionManager(db)
    db_manager.delete(customer)
    db_manager.commit()

    return sh.db_commit_success(HttpMethodType.DELETE, EntityType.CUSTOMER)


def update_customer_by_id(customer_id, customer_data):
    customer = Customer.query.get(customer_id)

    data_validator.set_strategy(ValidatePresentJsonObject())
    data_validator.validate(customer_data)
    data_validator.set_strategy(ValidateRequiredFields(["customer_id", "company_name"]))
    data_validator.validate(customer_data)
    data_validator.set_strategy(ValidateMatchingIDs("customer_id"))
    data_validator.validate(customer_id, customer_data)

    customer.company_name = customer_data.get("company_name", customer.company_name)
    customer.contact_name = customer_data.get("contact_name", customer.contact_name)
    customer.contact_title = customer_data.get("contact_title", customer.contact_title)
    customer.address = customer_data.get("address", customer.address)
    customer.city = customer_data.get("city", customer.city)
    customer.region = customer_data.get("region", customer.region)
    customer.postal_code = customer_data.get("postal_code", customer.postal_code)
    customer.country = customer_data.get("country", customer.country)
    customer.phone = customer_data.get("phone", customer.phone)
    customer.fax = customer_data.get("fax", customer.fax)
    customer.login = customer_data.get("login", customer.login)
    customer.password_hash = customer_data.get("password_hash", customer.password_hash)
    customer.role_id = customer_data.get("role_id", customer.role_id)

    db_manager = DatabaseSessionManager(db)
    db_manager.commit()

    return sh.db_commit_success(EntityType.CUSTOMER, HttpMethodType.PUT)
