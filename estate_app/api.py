import frappe
import json


def serialize_property_amenity_detail(doc):
    return {
        "name": doc.name,
        "amenity": doc.amenity,
    }
#grocery_delivery_app
# @frappe.whitelist(allow_guest=True)
# def custom_property_api(property_name):
#     property_doc = frappe.get_doc("Property", property_name)

#     # Serialize the amenities field
#     serialized_amenities = [serialize_property_amenity_detail(
#         amenity) for amenity in property_doc.amenities]

#     # Define the fields you want to keep in the response
#     response_data = {
#         "name": property_doc.name,
#         "property_name": property_doc.property_name,
#         "address": property_doc.address,
#         "property_type": property_doc.property_type,
#         "agent": property_doc.agent,
#         "status": property_doc.status,
#         "description": property_doc.description,
#         "amenities": serialized_amenities,
#     }

#     return json.dumps(response_data)
@frappe.whitelist(allow_guest=True)
def custom_property_api(property_name):
    # Fetch the Property document by its name
    property_doc = frappe.get_doc("Property", property_name)

    # Serialize the amenities field
    serialized_amenities = [serialize_property_amenity_detail(
        amenity) for amenity in property_doc.amenities]

    response_data = {
        "name": property_doc.name,
        "property_name": property_doc.property_name,
        "address": property_doc.address,
        "property_type": property_doc.property_type,
        "agent": property_doc.agent,
        "status": property_doc.status,
        "description": property_doc.description,
        "amenities": serialized_amenities,
    }

    return response_data
    # return "response_data"

# my_module/api.py


@frappe.whitelist(allow_guest=True)
def get_property_list(property_name=None):
    if property_name:
        # Fetch details for a specific property
        property_doc = frappe.get_doc("Property", property_name)
        # Serialize the property details as needed
        response_data = {
            "name": property_doc.name,
            "property_name": property_doc.property_name,
            "address": property_doc.address,
            # Add more fields as needed
        }
    else:
        # Fetch a list of properties
        properties = frappe.get_all("Property", filters={}, fields=[
                                    "name", "property_name"])
        # Serialize the list of properties as needed
        response_data = properties

    return response_data


@frappe.whitelist(allow_guest=True)
def create_property():
    pass
