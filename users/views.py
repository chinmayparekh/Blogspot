from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.
def register(request):
    form=UserCreationForm()
    return render(request, 'users/register.html', {'form':form})