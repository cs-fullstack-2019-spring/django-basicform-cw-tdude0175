from django.urls import path
from . import views

# when calling for a path via form it uses names NOT PATHS. it can also use views instead

urlpatterns = [
    path("", views.index, name="index"),
    path('personGreet/', views.greeting , name ='personGreet'),
    path('addedmoney/<int:accountID>/', views.add5Dollars , name = 'add5Dollars')
]