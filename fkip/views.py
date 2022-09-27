from django.shortcuts import render

# Create your views here.
def prodi6(request):
    judul = ["Prodi Pendidikan Bahasa Inonesia", "Prodi Pendidikan Matematika", "Prodi Pendidikan Bahasa Inggris", "Prodi Pendidikan Guru Sekolah Dasar", "Prodi Pendidikan Pancasila kewarganegaraan", "Prodi Pendidikan Khusus", "Prodi Pendidikan Biologi", "Prodi Pendidikan Ipa", "Prodi Pendidikan Kimia", "Prodi Pendidikan Fisika", "Prodi Pendidikan Bimbingan Konseling", "Prodi Pendidikan Pendidikan PAUD", "Prodi Pendidikan Sejarah", "Prodi Pendidikan Seni Pertunjukan", "Prodi Pendidikan Sosiologi", "Prodi Pendidikan Vokasi Teknik Elektro", "Prodi Pendidikan Vokasi Teknik Elektro"]

    konteks = {
        'title' : judul,
    }
  
    return render(request, 'indexfkip.html', konteks)