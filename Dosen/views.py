from django.shortcuts import render
from Dosen.models import Dosen
# Create your views here.
def dosen(request):
    context = {
        'lecturer': Dosen.objects.all()
        
    }
    return render(request,"indexdosen.html", context)