from django.shortcuts import render

# Create your views here.
def prodi7(request):
    judul = ["Prodi Teknik Elektro", "Prodi Teknik Mesin", "Prodi Teknik Industri", "Prodi Teknik Kimia", "Prodi Teknik Metalurgi", "Prodi Teknik Sipil"]

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'indexft.html', konteks)