from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect

from .models import *
from .task import *
from .email import *

def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = Employee.objects.filter(emp_uid=username).first()
            if user.emp_uid == username and user.emp_pwd == password:
                tickets = Tickets.objects.filter(dept_name=user.dept_name)
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
                    messages.error(request, 'Incorrect Password.')
                else:
                    messages.error(request, 'Username does not exists.')
        except Exception as e:
            messages.error(request, 'An Error Occurred.', e)
    
    return render(request, "ticket_resolution/login.html")

def detailedView(request, id):
    ticket = Tickets.objects.filter(id=id).first()
    if request.method=="POST":
        comments = request.POST['comments']
        ticket.status = request.POST['up_status']
        ticket.dept_name = request.POST['up_dept']
        ticket.save()
        send_email(ticket.id, ticket.cust_email, comments, ticket.status, ticket.dept_name)
        return redirect('details', id=id)
    return render(request, "ticket_resolution/detailed_view.html", {
        'ticket' : ticket,
    })