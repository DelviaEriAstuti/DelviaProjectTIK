from django.shortcuts import render, redirect
from TenagaPendidik.models import TenagaPendidik
from TenagaPendidik.forms import FormTenagaPendidik
from django.contrib import messages

# Create your views here.

def hapus_tenagapendidik(request, id_tenagapendidik):
    tenagapendidik = TenagaPendidik.objects.filter(id=id_tenagapendidik)
    tenagapendidik.delete()
    if request.method == "POST":
        tenagapendidik.hapus()

    return redirect('/tenagapendidik/')


def ubah_tenagapendidik(request, id_tenagapendidik):
    tenagapendidik = TenagaPendidik.objects.get(id=id_tenagapendidik)
    template = 'ubah-tendik.html'
    if request.POST:
        form = FormTenagaPendidik(request.POST, instance=tenagapendidik)
        if form.is_valid():
            form.save()
            messages.success(request, "Data berhasil diperbarui")
            return redirect('ubah_tenagapendidik', id_tenagapendidik=id_tenagapendidik)
    else:
        form = FormTenagaPendidik(instance=tenagapendidik)
        konteks = {
            'form': form,
            'tenagapendidik': tenagapendidik,
        }
    return render(request, template, konteks)



def tenagapendidik(request):

    context = {
        'student': TenagaPendidik.objects.all()
    }    
    return render(request, 'indextendik.html', context)


def tambah_tenagapendidik(request):
    if request.POST:
        form = FormTenagaPendidik(request.POST)
        if form.is_valid():
            form.save()
            form = FormTenagaPendidik()
            pesan = "Data berhasil ditambahkan"

            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'tambah-tendik.html', konteks)
    else:
        form = FormTenagaPendidik()

    konteks = {
        'form': form,
    }

    return render(request, 'tambah-tendik.html', konteks)