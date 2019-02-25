from django.shortcuts import render, get_object_or_404 , redirect
from django.http import HttpResponse
from .models import Account


# Create your views here.
def index(request):
    AccountList = Account.objects.all()
    context = \
        {
            'AccountList' : AccountList
        }
    return render(request, 'accountApp/index.html', context)

def greeting(request):
    return HttpResponse('hello ' + request.POST['personName'])


# this finds the person based on foreginKey aka accountID adds five dollars and saves the new value then
# redirect reloads the page
# without return it won't work
def add5Dollars(request , accountID):
    person = get_object_or_404(Account, pk=accountID)
    person.checking += 5
    person.save()
    return redirect(index)