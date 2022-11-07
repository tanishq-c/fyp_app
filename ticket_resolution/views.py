from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *

# Create your views here.
class EmpView(LoginRequiredMixin, View):
    template_name = "ticket_resolution/ticket_resolution.html"
    def get(self, request, *args, **kwargs):
        tickets = Tickets.objects.all()
        return render(request, self.template_name, {
                    'ticket' : tickets,
                })