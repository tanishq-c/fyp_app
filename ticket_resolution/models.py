from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import JSONField
from django.db import models

# User = get_user_model()

class Department(models.Model):
    dept_name = models.CharField(max_length=255, null=False, blank=True) 

class Employee(models.Model):
    emp_name = models.CharField(max_length=255, null=False, blank=True) 
    emp_uid = models.CharField(max_length=255, null=False, blank=True) 
    emp_pwd = models.CharField(max_length=255, null=False, blank=True)
    dept_id = models.ForeignKey(Department, null=True, on_delete=models.SET_NULL, related_name='emp_dept_id')
    ticket_count = models.IntegerField(null=False, default=0)
    
class Tickets(models.Model):
    cust_email = models.CharField(max_length=255, null=False, blank=True)
    metadata = JSONField(blank=True,null=True)
    emp_id = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL, related_name='emp_ticket_id')
    status = models.CharField(max_length=20, null=False, blank=False, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tracking_id = models.CharField(max_length=255, null=False, blank=True)