from django.contrib import admin
from .models import Transaction

# Register your models here.

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user_send', 'user_receive', 'deal_time', 'deal_type_pay_not_request', 'deal_amount')

admin.site.register(Transaction, TransactionAdmin)