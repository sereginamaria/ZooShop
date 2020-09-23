from django.db.models import *


class Shops(Model):
    id = AutoField(primary_key=True)
    address = TextField()
    employees = ForeignKey('Employee', on_delete=CASCADE)


class Employee(Model):
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    surname = CharField(max_length=50)
    middle_name = CharField(max_length=50)  # отчество
    role = CharField(max_length=100)  # должность
    phone = CharField(max_length=11)


# class