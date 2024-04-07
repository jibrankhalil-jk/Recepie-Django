from django.shortcuts import render , redirect , HttpResponse
from .models import *

# Create your views here.

def deleterecepie(request,id):
    print(id)
    qer = Recepies.objects.get(id = id)
    qer.delete()
    return redirect("/")

def recepies(request):
    if (request.method == "POST"):
        data = request.POST
        # data = request.FILES.get('recepie_pic')
        # print(data)
        Recepies.objects.create(
            recepies_name=data.get('recepie_name'),
            recepies_descreption=data.get('recepie_descreption'),
            recepies_image=request.FILES.get('recepie_pic')
        )
        return redirect('/')
    
    q = Recepies.objects.all()
    # print(q[0].recepies_name)
    cntxt = {"recepies":q}

    return render(request, "recepies.html",cntxt)
