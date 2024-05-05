# vendor_management_system
Description
This API provides endpoints for managing vendors and purchase orders in a Vendor Management System. It allows users to create, retrieve, update, and delete vendors and purchase orders, as well as calculate performance metrics for vendors.

## Installation
1. Clone the repository:
git clone <repository_url>
https://github.com/Urmila4718/vendor_management_system

2. Navigate to the project directory:
cd vendor_management_system

3. Create a virtual environment (optional but recommended):
python3 -m venv venv

4. Activate the virtual environment:
venv\Scripts\activate

5. Install the required dependencies:
pip install -r requirements.txt

6. Apply migrations to create the database schema:
python manage.py makemigrations
python manage.py migrate

7. Run the development server:
python manage.py runserver


# API Endpoints
## Vendor Profile Management:
* POST /api/vendors/: Create a new vendor.
* GET /api/vendors/: List all vendors.
* GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details.
* PUT /api/vendors/{vendor_id}/: Update a vendor's details.
* DELETE /api/vendors/{vendor_id}/: Delete a vendor.

## Purchase Order Tracking:
* POST /api/purchase_orders/: Create a purchase order.
* GET /api/purchase_orders/: List all purchase orders with an option to filter by vendor.
* GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.
* PUT /api/purchase_orders/{po_id}/: Update a purchase order.
* DELETE /api/purchase_orders/{po_id}/: Delete a purchase order

## Vendor Performance Evaluation:
* GET /api/vendors/{vendor_id}/performance

## Update Acknowledgment Endpoint:
* POST /api/purchase_orders/{po_id}/acknowledge
  
# Technologies Used
Django
Django REST Framework
 
