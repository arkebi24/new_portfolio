from django.shortcuts import render
from .models import Contact
# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        contact = Contact(contact_name=name, contact_email=email, contact_msg=message)
        contact.save()
    return render(request, 'port/index.html')