from django.db.models import *


class Shops(Model):
    shop_id = AutoField(primary_key=True)
    address = TextField()
    employees = ForeignKey('Employee', on_delete=CASCADE)


class Employee(Model):
    employee_id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    surname = CharField(max_length=50)
    middle_name = CharField(max_length=50)  # отчество
    role = CharField(max_length=100)  # должность
    phone = CharField(max_length=11)
    e_mail = CharField(max_length=50)
    shop_id = AutoField(primary_key=True)


class Clients(Model):
    client_id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    surname = CharField(max_length=50)
    phone = CharField(max_length=11)
    e_mail = CharField(max_length=50)


class Providers(Model):
    provider_id = AutoField(primary_key=True)
    company_name = CharField(max_length=100)
    company_address = CharField(max_length=100)
    phone = CharField(max_length=11)


class Products(Model):
    product_id = AutoField(primary_key=True)
    provider_id = AutoField(primary_key=True)
    product_name = CharField(max_length=100)
    price = IntegerField(max_length=10)


class Accounting(Model):
    product_id = AutoField(primary_key=True)
    provider_id = AutoField(primary_key=True)
    employee_id = AutoField(primary_key=True)
    shop_id = AutoField(primary_key=True)
    product_name = CharField(max_length=100)
    date = DateField()
    account_number = IntegerField()


class Sales(Model):
    product_id = AutoField(primary_key=True)
    employee_id = AutoField(primary_key=True)
    shop_id = AutoField(primary_key=True)
    product_name = CharField(max_length=100)
    date = DateField()
    account_number = IntegerField()  # номер счета
    quantity = IntegerField()
