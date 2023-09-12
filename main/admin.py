from django.contrib import admin
from main.models import Edu,Exp,Pro,Service
from subscribe.models import Subscribe

# Register your models here.


admin.site.register(Edu)
admin.site.register(Exp)
admin.site.register(Pro)
admin.site.register(Service)

admin.site.register(Subscribe)


