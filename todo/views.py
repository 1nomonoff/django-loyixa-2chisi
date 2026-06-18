from django.shortcuts import render

# Create your views here.
def dastur_page(request):
    return render(request, 'dastur.html')