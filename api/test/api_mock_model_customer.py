import requests

url = 'http://localhost:5000/customer'
data = {
    "customer_id": "sdsdsss",
    "company_name": "Test Testser",
    "contact_name": "Marsco Polo",
    "contact_title": "Owner/Marketing Assistant",
    "address": "Keskuskatu 45",
    "city": "Helsinki",
    "postal_code": "21240",
    "country": "Finland",
    "phone": "90-224 8858",
    "fax": "90-224 8858",
    "login": None,
    "password_hash": None,
    "role_id": None
}

response = requests.post(url, json=data)
print(response.text) 