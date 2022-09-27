from django.shortcuts import render

# Create your views here.
def prodi8(request):
    judul = ["Doktor Pendidikan", "Doktor Ilmu Akutansi", "Magister Ilmu Hukum", "Magister Administrasi Publik", "Magister Ilmu Pertanian", "Magister Akutansi", "Magister Ilmu Komunikasi", "Magister Manajemen", "Magister Teknik Kimia", "Pendidikan Bahasa Indonesia", "Pendidikan Bahasa Inggris", "Pendidikan Matematika", "Teknologi Pendidikan"]

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'indexpascasarjana.html', konteks)