from django.contrib import admin
from home.models import Contact , Complaint , Bills , Appartment , Dependents , Visitor , Employee


# Register your models here.
admin.site.register(Contact)
admin.site.register(Complaint)
admin.site.register(Bills)
admin.site.register(Appartment)
admin.site.register(Dependents)
admin.site.register(Visitor)
admin.site.register(Employee)