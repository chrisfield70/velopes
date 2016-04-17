from django.shortcuts import render
from django.http import Http404

from inventory.models import Item, Account, Transaction

# from django.http import HttpResponse


def index(request):
	list_of_accounts = Account.objects.all
	list_of_transactions = Transaction.objects.all()

	items = Item.objects.exclude(amount=0)
	return render(request, 'inventory/index.html', {
		'items': items,
		'list_of_accounts': list_of_accounts,
		'list_of_transactions': list_of_transactions,
		})

	# return HttpResponse('<p>In index view</p>')


def item_detail(request, id):
	try:
		item = Item.objects.get(id=id)
	except Item.DoesNotExist:
		raise Http404('This item does not exist')
	return render(request, 'inventory/item_detail.html', {
		'item':item,
		})

def account_detail(request, id):
	try:
		account = Account.objects.get(id=id)
	except Account.DoesNotExist:
		raise Http404('This item does not exist')
	return render(request, 'inventory/account_detail.html', {
		'account':account,
		})



