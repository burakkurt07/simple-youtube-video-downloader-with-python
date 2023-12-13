# simple-youtube-video-downloader-with-python
Python ile basit Youtube Video indirme

Programın Özeti:

Bu program, kullanıcıya YouTube'dan videolar indirmek için bir arayüz sunar. İki temel işlevi vardır: belirli bir YouTube video bağlantısından video indirme ve YouTube'da video arama ve indirme.

# Kullanılan Kütüphaneler:
import os  # İşletim sistemi işlemleri için
from yt_dlp import YoutubeDL  # YouTube videolarını indirmek için
from youtubesearchpython import VideosSearch  # YouTube'da video aramak için

# Programın Çalışma Mantığı:

  #  YouTube Video İndirme:
        Kullanıcıdan bir YouTube video bağlantısı istenir.
        Video indirme seçenekleri (dizin, ad, çözünürlük) kullanıcıya sorulur.
        İndirme işlemi tamamlandığında bilgi verilir.

 #   YouTube Video Ara ve İndir:
        Kullanıcıdan bir video arama terimi istenir.
        Bulunan videolar listelenir, ve kullanıcı istediği videoyu seçer.
        Seçilen video indirilir.

#    İndirilen Videoları Listeleme:
        İndirilen videoların listesi gösterilir.

 #   İndirilen Video Silme:
        İndirilen videolar listelenir.
        Kullanıcıdan silmek istediği video adı sorulur.
        Belirtilen video silinir.

 #   Program Sonlandırma:
        Kullanıcı programı sonlandırmak istediğinde çıkış yapabilir.

