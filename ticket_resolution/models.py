from django.db import models

class Department(models.Model):
    dept_name = models.CharField(max_length=255, null=False, blank=True) 
    dept_id = models.IntegerField(null=False, blank=True)

class Employee(models.Model):
    emp_name = models.CharField(max_length=255, null=False, blank=True) 
    emp_uid = models.CharField(max_length=255, null=False, blank=True) 
    emp_pwd = models.CharField(max_length=255, null=False, blank=True)
    dept_name = models.CharField(max_length=255, null=False, blank=True)

class Tickets(models.Model):
    cust_email = models.CharField(max_length=255, null=False, blank=True)
    cust_query = models.CharField(max_length=5000, null=False, blank=True)
    dept_name = models.CharField(max_length=255, null=False, blank=True)
    status = models.CharField(max_length=20, null=False, blank=False, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CustQuery(models.Model):
    cust_email = models.CharField(max_length=255, null=False, blank=True)
    cust_query = models.CharField(max_length=5000, null=False, blank=True)
    status = models.CharField(max_length=20, null=False, blank=False, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)