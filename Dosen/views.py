from django.shortcuts import render, redirect
from Dosen.models import Dosen
from Dosen.forms import FormDosen
from django.contrib import messages

# Create your views here.

def hapus_dosen(request, id_dosen):
    dosen = Dosen.objects.filter(id=id_dosen)
    dosen.delete()
    if request.method == "POST":
        dosen.hapus()

    return redirect('/dosen/')


def ubah_dosen(request, id_dosen):
    Dosen = Dosen.objects.get(id=id_dosen)
    template = 'ubah-dosen.html'
    if request.POST:
        form = FormDosen(request.POST, instance=dosen)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diperbarui")
            return redirect('ubah_dosen', id_dosen=id_dosen)
    else:
        form = FormDosen(instance=dosen)
        konteks = {
            'form': form,
            'dosen': dosen,
        }
    return render(request, template, konteks)



def dosen(request):

    context = {
        'student': Dosen.objects.all()
    }    
    return render(request, 'indexdosen.html', context)


def tambah_dosen(request):
    if request.POST:
        form = FormDosen(request.POST)
        if form.is_valid():
            form.save()
            form = FormDosen()
            pesan = "Data berhasil ditambahkan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-dosen.html', konteks)
    else:
        form = FormDosen()

    konteks = {
        'form': form,
    }

    return render(request, 'tambah-dosen.html', konteks)