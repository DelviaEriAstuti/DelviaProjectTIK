from django.shortcuts import render
from TenagaPendidik.models import TenagaPendidik
# Create your views here.
def tenagapendidik(request):
    context = {
        'educator': TenagaPendidik.objects.all()
        
    }
    return render(request,"indextendik.html", context)