from django.shortcuts import render
from shop.models import Mevalar ,Ismlar
# Create your views here.

def salom(request):
    matn="salom"
    ism="Muhammadsodiq"
    mevalar=Mevalar.objects.all()
    ismlar=Ismlar.objects.all()
    context={ "title":matn,
        "ism":ism,"mevalar":mevalar,
        "ismlar":ismlar
    }
  

    return render(request,'index.html',context=context)
