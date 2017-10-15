from django.shortcuts import render
from appTwo.models import User
'''from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<em>My Second Project!</em>")

def help(request):
    helpdict = {'help_insert':'HELP PAGE'}
    return render(request,'apptwo/help.html',context=helpdict)'''


def index(request):
    return render(request,'appTwo/index.html')

def users(request):

    user_list = User.objects.order_by('first_name')
    user_dict = {'users':user_list}
    return render(request, 'appTwo/users.html',context=user_dict)
