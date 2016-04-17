# Create your views here.
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from accountsManager.models import Account, Transaction, TransactionForm


def index(request):
    """list of accounts each displaying current balance"""
    list_of_accounts = Account.objects.all()
    list_of_transactions = Transaction.objects.all()
    t = loader.get_template('index.html')
    c = Context({
         'list_of_accounts': list_of_accounts, 
         'list_of_transactions': list_of_transactions
    })
    
    return HttpResponse(t.render(c))





def enter_transaction(request):
    """manually enter a transaction"""
    list_of_accounts = Account.objects.all()
    return  render_to_response('enter_transaction.html', {'list_of_accounts': list_of_accounts}, context_instance=RequestContext(request))

#def write_transaction(request):
#    name = request.POST['name']
 #   amount = request.POST['amount']
  #  account_name = request.POST['account']
   # account = Account.objects.get(name=account_name)
    #t = Transaction(name=name, amount=amount, account=account)
   # t.save()
   # account.process_transaction(t)
    #return HttpResponseRedirect(reverse('accountsManager.views.index'))


def write_transaction(request):
    list_of_accounts = Account.objects.all()
    if request.method == 'POST': # If the form has been submitted...
      form = TransactionForm(request.POST) # A form bound to the POST data
      #Decimal(str(form.amount))
      if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # print 'hello'
            # ...
            #  return HttpResponseRedirect(reverse('accountsManager.views.index')) # Redirect after POST
      else:
	        form = TransactionForm() # An unbound form
    return render_to_response('enter_transaction.html', {'list_of_accounts': list_of_accounts}, context_instance=RequestContext(request));





#def list_transactions(request):
	

# TODO use forms to convert the sumitted values from unicode to decimal - see the docs on forms
# TODO print list of accounts and current balance - DONE
# TODO enter a transaction (positive = deposit - DONE, negative = withdraw - TEST REQUIRED)
# TODO read a transaction from a file (csv, account, desc, amount)
# TODO view a list of transactions
# TODO edit a transaction
# TODO extend transaction to include date
# TODO thing about some form of bank reconcillation

