from django.db import models
from django.db import models


class Report(models.Model):
    nu_departments = (
        ('cit','Computing and Information Tecnology'),
        ('sba', 'Procurement and Logistics'),
        ('oasis', 'oasis'),
        ('lab A', 'lab A'),
        ('lab B', 'lab B'),
    )

    issue_list = (
        ('Faulty Mouse','Faulty Keyboard'),
        ('Faulty System Unit', 'Faulty System Unit'),
        ('Faulty Monitor', 'Faulty Monitor'),
        ('Faulty Printer', 'Faulty Printer'),
        ('Faulty Projector', 'Faulty Projector'),
    )

    status_list = (
        ('Recycled','Recycled'),
        ('Disposed', 'Disposed'),
    )

    Name = models.CharField(max_length=200, null=True)
    Department = models.CharField(choices=nu_departments, null=True, max_length=200)
    Issue = models.CharField(choices=issue_list, max_length=200, null=True)
    Code = models.IntegerField( null=True)
    Status = models.CharField(choices=status_list, max_length=200, null=True)

    def __str__(self):
        return self.Name


class Electronics(models.Model):
    category_list = (
    ('Laptop','Laptop'),
    ('Desktop','Desktop'),
    ('Printer','Printer'),
    ('Projector','Projector'),
    ('Keyboard','Keyboard'),
    ('Mouse','Mouse'),
    
    )
    Brand_list = (
         ('Dell','Dell'),
         ('Hp','Hp'),
         ('Lenovo','Lenovo'),
         ('Acer','Acer'),
         ('Others','Others'),
    )
    Brand = models.CharField(choices=Brand_list, max_length=200, null=True)
    YearOfRelease = models.CharField(max_length=4, null=True)
    SerialNumber = models.CharField(max_length=200, null=True)
    Category = models.CharField(choices=category_list, max_length=200, null=True)
    Description = models.TextField(max_length=200, null=True)

    def __str__(self):
        return self.Brand
    
 
class AssignElectronics(models.Model):
    dep_list = (
         ('cit','Computing and Information Tecnology'),
        ('sba', 'Procurement and Logistics'),
        ('oasis', 'oasis'),
        ('lab A', 'lab A'),
        ('lab B', 'lab B'),
    )
    Item = models.ForeignKey(Electronics, on_delete=models.CASCADE)
    Department = models.CharField(choices=dep_list, max_length=200, null=True)
    Quantity = models.IntegerField( null=True)

   
    def __str__(self):
        return str(self.Item)

'''   
class Users(models.model):
    username 
    password
    first_name
    last_name
    contact 
    email
    account_type


class Electronics(models.Model):

    rid 
    Name
    Description
    user_id
    department
    electronic_id
    issue 
    status 

class inventrory(models.Model):
    id
    electronic_id
    quantity
    
'''