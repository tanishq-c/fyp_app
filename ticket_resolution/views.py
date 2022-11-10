from django.shortcuts import render, redirect
from django.contrib import messages

from .models import *

# Create your views here.
def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = Employee.objects.filter(emp_uid=username).first()
            if user.emp_uid == username and user.emp_pwd == password:
                tickets = Tickets.objects.filter(emp_id_id=user.id)
                pending = tickets.filter(status='Pending')
                completed = tickets.filter(status='Completed')
                in_progress = tickets.filter(status='In-Progress')
                rejected = tickets.filter(status='Rejected')
                return render(request, 'ticket_resolution/ticket_resolution.html', {
                        'user': user,
                        'ticket' : tickets,
                        'pending' : pending,
                        'completed' : completed,
                        'in_progress' : in_progress,
                        'rejected' : rejected,
                    })
            else:
                if user.emp_uid == username:
                    return render(request, "ticket_resolution/login.html")
                else:
                    return render(request, "ticket_resolution/login.html")
        except:
            return render(request, "ticket_resolution/login.html")
        
    else:  
        return render(request, "ticket_resolution/login.html")