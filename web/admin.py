from django.contrib import admin
# from django.apps import apps
# from django.contrib.admin.sites import AlreadyRegistered
#
# models = apps.get_models()
#
# for model in models:
#     try:
#         admin.site.register(model)
#     except AlreadyRegistered:
#         continue

from .models import *

admin.site.register(Shop)
admin.site.register(Employee)
admin.site.register(Client)
admin.site.register(Provider)
admin.site.register(Product)
admin.site.register(Accounting)
admin.site.register(Sale)
admin.site.register(Item)
