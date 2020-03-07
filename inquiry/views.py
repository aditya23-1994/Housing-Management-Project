from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Inquiry

def contact(request):
    if request.method == "POST":
        issue = request.POST['issue']
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        # flat = request.POST['flat']
        message = request.POST['message']
        user_id = request.POST['user_id']


        contact = Inquiry(issue=issue, name=name, email=email, phone=phone, message=message, user_id=user_id)

        contact.save()

        messages.success(request,"Your query has been submited a manager will get to you soon")

        return redirect('dashboard')