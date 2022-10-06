from django.shortcuts import render
from Mahasiswa.models import Mahasiswa
# Create your views here.
def mahasiswa(request):
    context = {
        'student': Mahasiswa.objects.all()
        
    }
    return render(request,"indexmahasiswa.html", context)