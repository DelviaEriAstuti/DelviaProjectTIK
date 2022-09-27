from django.shortcuts import render

# Create your views here.
def prodi5(request):
    judul = ["Prodi Kedokteran", "Prodi Keperawatan S1 dan D3", "Prodi Gizi S1", "Prodi Keolahragaan"]

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'indexfk.html', konteks)