from enum import Enum, unique

@unique
class EntityType(Enum):
    RECORD = "record"
    CUSTOMER = "customer"
    SUPPLIER = "supplier"
    EMPLOYEE = "employee"
    ORDER = "order"
    PRODUCT = "product"
    CATEGORY = "category"
    REGION = "region"
    SHIPPER = "shipper"
    TERRITORIES = "territories"

    def __str__(self):
        return self.value

@unique
class HttpMethodType(Enum):
    GET = "GET"
    POST = "POST"
    DELETE = "DELETE"
    PUT = "PUT"

    def __str__(self):
        return self.value
