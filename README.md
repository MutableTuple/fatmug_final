# fatmug_final
# all the files are in the Master Branch
## v1.1.1

# Access the Main app here
# https://fatmugfinal-production.up.railway.app/

## API routes
### "POST":"/api/create-vendor",
### "GET":"/api/vendors",
### "GET":"/api/vendor/id",
### "PUT":"api/edit-vendor/id/",
### "DELETE":"/api/delete-vendor/id",
### "POST":"/api/create-po",
### "GET":"/api/allpo",
### "GET":"/api/singlepo/id",
### "PUT":"/api/edit-po/id",
### "DELETE":"/api/delete-po/id",
### "GET":"/api/performance-metrics/id"

# Get all Vendors ("GET":"/api/vendors")

# Get a single vendor ("GET":"/api/vendor/id")

# Data format to be sent while making post requests

# Create Vendor ("POST":"/api/create-vendor")
### {
### "name": "",
### "contact_details": "",
### "address": "",
### "on_time_delivery_rate": "",
### "quality_rating_avg": "",
### "average_response_time": ""
### }

# Edit Vendor ("PUT":"PUT":"api/edit-vendor/id/") 
## ⭐⭐ Make sure you pass the vendor id or it would return an error
### {
### "name": "",
### "contact_details": "",
### "address": "",
### "on_time_delivery_rate": "",
### "quality_rating_avg": "",
### "average_response_time": ""
### }

# Dummy data for vendor
### {
###  "name": "ABC Supplier",
###  "contact_details": "Contact Person: John Doe\nEmail: john.doe@example.com\nPhone: +1234567890",
###  "address": "123 Main Street, Cityville",
###  "on_time_delivery_rate": 95,
###  "quality_rating_avg": 4.2,
###  "average_response_time": 1
### }

# Get all Purchase Orders ("GET":"/api/allpo")

# Get a single Purchase Order ("GET":"/api/singlepo/id") ⭐id should be the id of an existing Purchase Order

# Delete Vendor ( "DELETE":"/api/delete-vendor/id" )
## ⭐⭐ Make sure you pass the vendor id or it would return an error

# Create a Purchase Order ("POST":"/api/create-po")
### {
###  "vendor": "",⭐this has to be an id for an existing vendor, or it would return an error, eg: 12
###  "po_number": "",
###  "order_date": "",
###  "delivery_date": "",
###  "estimated_delivery_date": "",
###  "delivered_before_delivery_date": "",
###  "items": "",
###  "quantity": "",
###  "status": "",
###  "quality_rating": "",
###  "issue_date": "",
###  "acknowledgment_date": ""
### }

## Dummy Data
### {
###  "vendor": 16, 
###  "po_number": "PO123",
###  "order_date": "2023-01-15",
###  "delivery_date": "2023-02-01",
###  "estimated_delivery_date": "2023-01-28",
###  "delivered_before_delivery_date": 0, ⭐this value is either 0 or 1, 0 if not delivered before delivery date or else 1
###  "items": {
###    "item1": {
###      "name": "Item1",
###      "quantity": 30,
###      "unit_price": 10.99
###    },
###    "item2": {
###      "name": "Item2",
###      "quantity": 50,
###      "unit_price": 8.99
###    },
###    "item3": {
###      "name": "Item3",
###      "quantity": 20,
###      "unit_price": 15.99
###    }
###  },
###  "quantity": 100,
###  "status": "completed",
###  "quality_rating": 4.5,
###  "issue_date": "2023-01-25",
###  "acknowledgment_date": "2023-01-20"
### }


# Edit a Purchase Order ("PUT":"api/edit-vendor/id/") ⭐⭐ the id here should be the id of the Purchase order not vendor
### {
###  "vendor": "",⭐this has to be an id for an existing vendor, or it would return an error, eg: 12
###  "po_number": "",
###  "order_date": "",
###  "delivery_date": "",
###  "estimated_delivery_date": "",
###  "delivered_before_delivery_date": "",
###  "items": "",
###  "quantity": "",
###  "status": "",
###  "quality_rating": "",
###  "issue_date": "",
###  "acknowledgment_date": ""
### }

# Delete a Purchase Order ( "DELETE":"/api/delete-po/id" )
## ⭐⭐ Make sure you pass the po id or it would return an error

# Get Performance Metrics of a vendor ("GET":"/api/performance-metrics/id") ⭐Id should be the id of an existing vendor
