from django.shortcuts import render
from.forms import studentRegitserForm
from .models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    form=studentRegitserForm()
    user=User.objects.all()
    context={'form':form,'user':user}
    if request.method=="POST":


      
       name=request.POST['name']
       email=request.POST['email']
       password=request.POST['password']
       user=User.objects.create(name=name,email=email,password=password)
       myuser=User.objects.values()
       print(myuser)
       student_data=list(myuser)

       return JsonResponse({'status':'Save','student_data':student_data})
    

    return render(request,'base.html',context)


# def saveform(request):
#     form=studentRegitserForm()
#     context={'form':form}
#     if request.method=="POST":

#         # form=studentRegitserForm(request.POST)
#         name=request.POST['name']
#         email=request.POST['email']
#         password=request.POST['password']
#         print(name,email,password)
#         # show=User(name=name,email=email,password=password)
#         # show.save()
#         # if form.is_valid:
#         #     form.save
#         #     user=User.objects.values()
#         #     print(user)
        #     student_data=list(user)
           

        
        # else:
        #     return JsonResponse("form is invalid")
        


    #     return JsonResponse({'status':'Save','student_data':student_data})

    


    # # else:
    #     return JsonResponse({'status':'0'})
    # return render(request,'base.html',context)



            
def delete(request):
    if request.method=="POST":
        id=request.POST.get("sid")

        user=User.objects.get(pk=id)
        user.delete()
        return JsonResponse({"status":1})
    else:
        return JsonResponse({"status":0})
