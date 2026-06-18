from django.shortcuts import render
from fintechhub.models import Textde ,Fintech


# Create your views here.
def fintech(request):
    sooz=Textde.objects.all()
    

    context={'soz':sooz, 'darslar':Fintech.objects.all()}
    return  render(request,'fintechhub.html',context=context)
