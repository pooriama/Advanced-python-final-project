from django.shortcuts import render
from django.http import HttpResponse
from appTwo.models import User
# Create your views here.
from appTwo.forms import NewUserForm
def index(request):
    return render(request,'apptwo/index.html')

# def help(request):
#     helpdict = {'help_insert':'HELP PAGE'}
#
#     return render(request,'apptwo/help.html',context=helpdict)


def users(request):
        form=NewUserForm()
        if request.method=="POST":
            form=NewUserForm(request.POST)

            if form.is_valid():
                form.save(commit=True)
                return index(request)

            else:
                print('Error from invalid')
        return render(request,'appTwo/Users.html',{'form':form})




    # users_ list=User.objects.all()
    # # print (type(users_list))
    # print (type(users_list.values()))
    # print (users_list.values()[0]['firstname'])
    # print (' ')
    # name_dict={'name_record':users_list.values()}
    # return render(request,'appTwo/index2.html',context=name_dict)
