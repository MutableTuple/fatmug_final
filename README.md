# fatmug_final
# all the files are in the Master Branch
## v1.1.1

#Access the Main app here
#https://fatmugfinal-production.up.railway.app/

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
### name= "",
### contact_details = "",
### address = "",
### on_time_delivery_rate="",
### quality_rating_avg="",
### average_response_time=""
### }

# Delete Vendor ( "DELETE":"/api/delete-vendor/id" )
## ⭐⭐ Make sure you pass the vendor id or it would return an error

# Create a Purchase Order ("POST":"/api/create-po")
### {
### vendor=vendor,
### po_number=data["po_number"],
### order_date=data['order_date'],
### delivery_date=data['delivery_date'],
### estimated_delivery_date=data['estimated_delivery_date'],
### delivered_before_delivery_date=data['delivered_before_delivery_date'],
### items=data['items'],
### quantity=data["quantity"],
### status=data["status"],
### quality_rating=data["quality_rating"],
### issue_date=data["issue_date"],
### acknowledgment_date=data["acknowledgment_date"]
### }
