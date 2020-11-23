from django.db.models import *
from django.contrib.auth.models import User


class Shop(Model):
    shop_id = AutoField(primary_key=True)
    address = TextField()
    employees = ForeignKey('Employee', on_delete=CASCADE)


class Client(Model):
    class Meta:
        verbose_name = 'Client'

    phone = CharField(max_length=11)
    user = OneToOneField(User, on_delete=CASCADE)


class Employee(Model):
    class Meta:
        verbose_name = 'Employee'

    phone = CharField(max_length=11)
    shop_id = ForeignKey('Shop', on_delete=CASCADE)
    user = OneToOneField(User, on_delete=CASCADE)


class Provider(Model):
    provider_id = AutoField(primary_key=True)
    company_name = CharField(max_length=100)
    company_address = CharField(max_length=100)
    phone = CharField(max_length=11)


class Product(Model):
    product_id = AutoField(primary_key=True)
    provider_id = ForeignKey('Provider', on_delete=CASCADE)
    product_name = CharField(max_length=100)
    price = IntegerField()


class Accounting(Model):
    product_id = ForeignKey('Product', on_delete=CASCADE)
    provider_id = ForeignKey('Provider', on_delete=CASCADE)
    employee_id = ForeignKey('Employee', on_delete=CASCADE)
    shop_id = ForeignKey('Shop', on_delete=CASCADE)
    product_name = CharField(max_length=100)
    date = DateField()
    account_number = IntegerField()


class Sale(Model):
    product_id = ForeignKey('Product', on_delete=CASCADE)
    employee_id = ForeignKey('Employee', on_delete=CASCADE)
    shop_id = ForeignKey('Shop', on_delete=CASCADE)
    product_name = CharField(max_length=100)
    date = DateField()
    account_number = IntegerField()  # номер счета
    quantity = IntegerField()


class Item(Model):
    id = AutoField(primary_key=True)
    name = TextField()
    price = IntegerField()
    amount = IntegerField()
    img_path = CharField(max_length=150)
