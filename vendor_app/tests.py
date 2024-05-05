import django
from django.test import TestCase
from datetime import datetime

import os
import uuid

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vendor_management_system.settings')

django.setup()
# Create your tests here.
import pytest 
import requests
from .models import *
# URL of the API endpoint
API_URL = 'http://127.0.0.1:8000/api'

#@pytest.mark.django_db
# def test_create_vendor():
#     # Create a new vendor
#     data = {
#         'name': 'Test Vendor',
#         'contact_details': 'test@example.com',
#         'address': '123 Test St',
#         'vendor_code': 'TEST123'
#     }
#     response = requests.post(API_URL+'/vendors/', json=data)

#     # Check if the request was successful (status code 201)
#     assert response.status_code == 201

#     # Check if the vendor was created in the database
#     vendor = Vendor.objects.get(name='Test Vendor')
#     assert vendor is not None

#     # Check if the vendor details match the data sent in the request
#     assert vendor.contact_details == 'test@example.com'
#     assert vendor.address == '123 Test St'
#     assert vendor.vendor_code == 'TEST123'

# @pytest.mark.django_db
# def test_get_vendors():
#     # Make a GET request to retrieve vendors
#     response = requests.get(API_URL+'/vendors')

#     # Check if the request was successful (status code 200)
#     assert response.status_code == 200

#     # Check if the response contains a list of vendors
#     vendors = response.json()
#     assert isinstance(vendors, list)


# @pytest.mark.django_db
# def test_get_vendors_id():
#     # Make a GET request to retrieve vendors
#     response = requests.get(API_URL+'/vendors/2/')

#     # Check if the request was successful (status code 200)
#     assert response.status_code == 200

#     # Check if the response contains a list of vendors
#     vendor = response.json()
#     assert 'id' in vendor
#     assert 'name' in vendor
#     assert 'contact_details' in vendor
#     assert 'address' in vendor
#     assert 'vendor_code' in vendor


# @pytest.mark.django_db
# def test_update_vendor_by_id():
#     # Make a GET request to retrieve the vendor
#     response = requests.get(API_URL + '/vendors/2/')  # Replace '2' with the ID of the vendor you want to update

#     # Check if the request was successful (status code 200)
#     assert response.status_code == 200

#     # Get the vendor details
#     vendor = response.json()

#     # Update the vendor data
#     updated_data = {
#         'name': 'Updated Vendor Name',  # Replace with the updated name
#         'contact_details': 'Updated Contact Details',  # Replace with the updated contact details
#         'address': 'Updated Address',  # Replace with the updated address
#         'vendor_code': 'Updated Vendor Code'  # Replace with the updated vendor code
#     }

#     # Make a PATCH request to update the vendor
#     response = requests.patch(API_URL + '/vendors/2/', json=updated_data)  # Replace '2' with the ID of the vendor

#     # Check if the update was successful (status code 200)
#     assert response.status_code == 200

#     # Make a GET request to retrieve the updated vendor
#     response = requests.get(API_URL + '/vendors/2/')  # Replace '2' with the ID of the vendor

#     # Check if the request was successful (status code 200)
#     assert response.status_code == 200

#     # Get the updated vendor details
#     updated_vendor = response.json()

#     # Check if the vendor details are updated
#     assert updated_vendor['name'] == updated_data['name']
#     assert updated_vendor['contact_details'] == updated_data['contact_details']
#     assert updated_vendor['address'] == updated_data['address']
#     assert updated_vendor['vendor_code'] == updated_data['vendor_code']


# @pytest.mark.django_db
# def test_delete_vendor_by_id():
#     # Make a DELETE request to delete the vendor
#     response = requests.delete(API_URL + '/vendors/3/')  # Replace '2' with the ID of the vendor you want to delete

#     # Check if the deletion was successful (status code 204 - No Content)
#     assert response.status_code == 204

#     # Attempt to retrieve the deleted vendor
#     response = requests.get(API_URL + '/vendors/3/')  # Replace '2' with the ID of the deleted vendor

#     # Check if the request returns a 404 status code, indicating that the vendor was not found
#     assert response.status_code == 404



# random_po_number = "PO" + str(uuid.uuid4().hex)[:10]

# @pytest.mark.django_db
# def test_create_purchase_order():
#     # Define the data for creating a new purchase order
#     data = {
#     "po_number": random_po_number,
#     "vendor": 2,
#     "order_date": "2024-04-26T08:00:00",
#     "delivery_date": "2024-05-10T12:00:00",
#     "items": [
#         {
#             "name": "Product C",
#             "description": "This is product A",
#             "price": 50.00,
#             "quantity": 2
#         },
#         {
#             "name": "Product B",
#             "description": "This is product B",
#             "price": 100.00,
#             "quantity": 3
#         }
#     ],
#     "quantity": 5,
#     "status": "pending",
#     "quality_rating": 4.5,
#     "issue_date": "2024-04-26T08:00:00",
# }


#     # Make a POST request to create a new purchase order
#     response = requests.post(API_URL + '/purchase_orders/', json=data)

#     # Check if the request was successful (status code 201 - Created)
#     assert response.status_code == 201

#     # Check if the response contains the created purchase order
#     purchase_order = response.json()
#     assert 'id' in purchase_order
#     assert 'vendor' in purchase_order
#     assert 'order_date' in purchase_order
#     assert 'delivery_date' in purchase_order
#     assert 'status' in purchase_order
#     # Add other assertions as needed

# @pytest.mark.django_db
# def test_get_purchase_orders():
#     # Make a GET request to retrieve all purchase orders
#     response = requests.get(API_URL + '/purchase_orders/')

#     # Check if the request was successful (status code 200 - OK)
#     assert response.status_code == 200

#     # Check if the response contains a list of purchase orders
#     purchase_orders = response.json()
#     assert isinstance(purchase_orders, list)

# @pytest.mark.django_db
# def test_get_purchase_order_by_id():
#     # Make a GET request to retrieve a specific purchase order by its ID
#     response = requests.get(API_URL + '/purchase_orders/2/')  # Assuming the purchase order ID is 1

#     # Check if the request was successful (status code 200 - OK)
#     assert response.status_code == 200

#     # Check if the response contains the expected purchase order
#     purchase_order = response.json()
#     assert 'id' in purchase_order
#     assert purchase_order['id'] == 2
#     assert purchase_order['po_number'] == '1234' # Check if the correct purchase order was retrieved


# @pytest.mark.django_db
# def test_update_purchase_order():
#     # Sample data for updating a purchase order (change the ID and data as needed)
#     updated_purchase_order_data = {
#         "po_number": "1234",
#         "vendor": 1,
#         "delivery_date": "2024-04-30T11:27:46.831259Z",
#         "items": [
#             {
#                 "name": "Updated Product A",
#                 "description": "This is updated product A",
#                 "price": 60.00,
#                 "quantity": 3
#             },
#             {
#                 "name": "Updated Product B",
#                 "description": "This is updated product B",
#                 "price": 40.00,
#                 "quantity": 4
#             }
#         ],

#         "quantity": 7,
#         "status": "completed",
#         "quality_rating": 4.8,
#         "acknowledgment_date": "2024-04-27T11:27:46.831259Z",
#     }

#     # Make a PUT request to update a specific purchase order (change the ID as needed)
#     response = requests.put(API_URL + '/purchase_orders/3/', json=updated_purchase_order_data)

#     # Check if the request was successful (status code 200)
#     assert response.status_code == 200

#     # Check if the purchase order was updated correctly
#     updated_purchase_order = response.json()
#     print(updated_purchase_order['issue_date'])
#     actual_datetime = datetime.strptime(updated_purchase_order['order_date'], '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y-%m-%dT%H:%M:%S')
#     assert updated_purchase_order['po_number'] == updated_purchase_order_data['po_number']
#     assert updated_purchase_order['vendor'] == updated_purchase_order_data['vendor']
#     assert updated_purchase_order['delivery_date'] == updated_purchase_order_data['delivery_date']
#     assert updated_purchase_order['items'] == updated_purchase_order_data['items']
#     assert updated_purchase_order['quantity'] == updated_purchase_order_data['quantity']
#     assert updated_purchase_order['status'] == updated_purchase_order_data['status']
#     assert updated_purchase_order['quality_rating'] == updated_purchase_order_data['quality_rating']
#     assert updated_purchase_order['acknowledgment_date'] == updated_purchase_order_data['acknowledgment_date']

# @pytest.mark.django_db
# def test_delete_purchase_order():
#     # Make a DELETE request to delete a specific purchase order (change the ID as needed)
#     response = requests.delete(API_URL + '/purchase_orders/3/')

#     # Check if the request was successful (status code 204 for successful deletion)
#     assert response.status_code == 204

# @pytest.mark.django_db
# def test_vendor_performance():
#     # Make a GET request to retrieve a specific purchase order by its ID
#     response = requests.get(API_URL + '/vendors/2/performance') 
#     # Check if the request was successful (status code 200 - OK)
#     assert response.status_code == 200

#     # Check if the response contains the expected purchase order
#     performance_data = response.json()
#     assert 'on_time_delivery_rate' in performance_data
#     assert 'quality_rating_avg' in performance_data
#     assert 'average_response_time' in performance_data
#     assert 'fulfillment_rate' in performance_data
   

@pytest.mark.django_db
def test_acknowledge_purchase_order():
    

    # Make a GET request to retrieve a specific purchase order by its ID
    response = requests.get(API_URL + '/purchase_orders/5/acknowledge') 
    # Check if the request was successful (status code 200 - OK)
    assert response.status_code == 200

    # Check if the response contains the expected purchase order
    performance_data = response.json()
    assert 'on_time_delivery_rate' in performance_data
    assert 'quality_rating_avg' in performance_data
    assert 'average_response_time' in performance_data
    assert 'fulfillment_rate' in performance_data
      