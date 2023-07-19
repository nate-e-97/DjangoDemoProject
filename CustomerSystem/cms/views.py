from django.http import HttpResponse
from django.template import loader
from .models import Customer
import json

def index(request):
    body_template = loader.get_template("cms_common.html")

    # Set up pagination
    page_number = int(request.GET["page"]) if request.GET.get("page") else 1 # Default to 1
    customers_per_page = 5 # Arbitrarily chosen

    record_count = len(Customer.objects.order_by('id').all()) # Number of records
    view_start_index = (page_number-1)*customers_per_page # Start page index
    has_next_page = page_number*customers_per_page < record_count # Whether or not another page can be navigated to after this one
    view_end_index = page_number*customers_per_page if has_next_page else record_count # Last index for page

    template_context = {
        "page_title": "Home",
        "inner_content_partial": "main.html",
        "customers": Customer.objects.order_by('id').all()[view_start_index:view_end_index],
        "page_number": page_number,
        "has_next_page": has_next_page
    }

    return HttpResponse(body_template.render(template_context, request))

def create(request):
    # GET handler serves the new user form page
    if request.method == 'GET':
        body_template = loader.get_template("cms_common.html")
        template_context = {
            "page_title": "New User",
            "inner_content_partial": "new_user.html"
        }

        return HttpResponse(body_template.render(template_context, request))
    
    # POST handler handles creating new users.
    elif request.method == 'POST':
        new_customer_data = json.loads(request.body)
        Customer.objects.create(**new_customer_data)
        return HttpResponse("Created", status=201)
    
    # DELETE handler handles deleting users.
    elif request.method == 'DELETE':
        if (request.GET.get('customerId')):
            Customer.objects.filter(id=request.GET["customerId"]).delete()
        return HttpResponse("Deleted", status=204)