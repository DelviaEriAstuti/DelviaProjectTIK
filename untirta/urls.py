"""untirta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from faper.views import prodi1
from feb.views import prodi2
from fh.views import prodi3
from fisip.views import prodi4
from fk.views import prodi5
from fkip.views import prodi6
from ft.views import prodi7
from pascasarjana.views import prodi8
from profil.views import profil
from univ.views import univ 
from Dosen.views import dosen
from Dosen.views import tambah_dosen
from Dosen.views import ubah_dosen
from Dosen.views import hapus_dosen
from Mahasiswa.views import mahasiswa
from Mahasiswa.views import tambah_mahasiswa
from Mahasiswa.views import ubah_mahasiswa
from Mahasiswa.views import hapus_mahasiswa
from TenagaPendidik.views import tenagapendidik
from TenagaPendidik.views import tambah_tenagapendidik
from TenagaPendidik.views import ubah_tenagapendidik
from TenagaPendidik.views import hapus_tenagapendidik




urlpatterns = [
    path('admin/', admin.site.urls),
    path('faper/', prodi1),
    path('feb/', prodi2),
    path('fh/', prodi3),
    path('fisip/', prodi4),
    path('fk/', prodi5),
    path('fkip/', prodi6),
    path('ft/', prodi7),
    path('pascasarjana/', prodi8),
    path('profil/', profil),
    path('univ/', univ),
    path('Dosen/', dosen),
    path('tambah-dosen/', tambah_dosen, name='tambah_dosen'),
    path('Dosen/ubah/<int:id_dosen>', ubah_dosen, name='ubah_dosen'),
    path('Dosen/hapus/<int:id_dosen>', hapus_dosen, name='hapus_dosen'),
    path('Mahasiswa/', mahasiswa),
    path('tambah-mahasiswa/', tambah_mahasiswa, name='tambah_mahasiswa'),
    path('Mahasiswa/ubah/<int:id_mahasiswa>', ubah_mahasiswa, name='ubah_mahasiswa'),
    path('Mahasiswa/hapus/<int:id_mahasiswa>', hapus_mahasiswa, name='hapus_mahasiswa'),
    path('TenagaPendidik/', tenagapendidik),
    path('tambah-tendik/', tambah_tenagapendidik, name='tambah_tenagapendidik'),
    path('TenagaPendidik/ubah/<int:id_tenagapendidik>', ubah_tenagapendidik, name='ubah_tenagapendidik'),
    path('TenagaPendidik/hapus/<int:id_tenagapendidik>', hapus_tenagapendidik, name='hapus_tenagapendidik'),



    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
