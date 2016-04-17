from django.contrib import admin

# Register your models here.

from .models import Item, Account, Transaction

class ItemAdmin(admin.ModelAdmin):
	list_display = ['title', 'amount']

class AccountAdmin(admin.ModelAdmin):
	list_display = ['title', 'currentBalance']

class TransactionAdmin(admin.ModelAdmin):
	list_display = ['description', 'amount']


admin.site.register(Item, ItemAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Transaction, TransactionAdmin)

