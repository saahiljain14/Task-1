from wealth_management.views import FixedDepositViewSet
from django.contrib import admin
from .models import FixedDeposit, Bullion
# Register your models here.

admin.site.register(FixedDeposit)
admin.site.register(Bullion)