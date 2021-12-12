# id-sentence-segmenter
Indonesian Rule-Based Sentence Segmenter

Simple Indonesian Sentence Segmentation script with rule-based approach 

import module
```
from idsentsegmenter.sentence_segmentation import SentenceSegmentation
```

get sentences from text 
```
# create sentence segmenter instance from SentenceSegmentation class
sentence_segmenter = SentenceSegmentation()

# parse text to sentences 
sentences = sentence_segmenter.get_sentences(news_content)
```

sample input and output from test script ```news_to_sentences.py```
```
Kinaras-MacBook-Pro:id-sentence-segmenter kinara$ python news_to_sentences.py 
news content: 
Berbagai upaya dilakukan oleh Pemerintah Daerah untuk mengurangi persebaran virus covid-19 menjelang libur natal dan tahun baru 2022, tidak terkecuali Pemerintah Kabupaten Bogor, Jawa Barat. Seperti yang dilakukan Satlantas Polres Bogor yang telah menyipakan 10 titik posko pemeriksaan ganjil genap dan protokol kesehatan di jalan menuju kawasan wisata Puncak Bogor. Selain pos-pos pemeriksaan, Polres Bogor juga akan memberlakukan sistem ganjil genap dan melakukan pemeriksaan surat hasil swab antigen atau PCR. Check point itu mulai diujicobakan petugas mulai 20 Desember 2021 hingga 2 Januari 2022. Kasatlantas Polres Bogor AKP Dicky Anggi Pranata mengatakan, nantinya di kawasan Puncak Bogor akan berlaku ganjil genap dan juga pemeriksan swab antigen dan PCR. "Kemarin sudah ada formula dan keputusan nanti di Puncak dan sekitarnya akan berlaku ganjil genap dan pemeriksaan swab antigen dan PCR," kata Dicky dalam keterangan resmi, Sabtu (11/12/2021). Hal itu sesuai dengan keputusan dari pertemuan lima Kapolres di wilayah Puncak Raya juga dengan kebijakan Menteri dalam negeri nomor 63, Kementerian Koordinator Bidang Kemaritiman dan Investasi Republik Indonesia serta kebijakan oleh Direktorat Jenderal Perhubungan Darat. Bahwasanya, di beberapa ruas tol salah satunya Tol Bogor sampai Cigombong (Bocimi) itu akan belaku ganjil genap. "Karena itu akan ada penambahan dua pos lagi, saat ini sudah ada delapan pos menjadi 10 pos," ucapnya. Lokasi pos pengamanan masih sama dengan check point ganjil genap yang telah diberlakukan sebelumnya. Beberapa titik pos tersebut antara lain dua titik di kawasan Sentul dan enam titik menuju Puncak. Hanya saja ditambah dua titik lagi di Caringin dan Cigombong. Petugas gabungan menerapkan ganjil genap di depan Gerbang Tol Pasteur Bandung, Jumat (17/9/2021). Sebanyak 640 kendaraan diputarbalikkan lantaran tak sesuai dengan nomor ganjil genap hari ini. "Kendaraan tidak sesuai kita putar balik ke daerah asal. Kalau pemeriksaan PeduliLindungi bukan di kita, tapi tempat tujuan restoran atau wisata," kata Dicky. Tidak hanya pemeriksaan ganjil genap kendaraan dan hasil swab antigen atau PCR, posko-posko itu juga akan melayani vaksinasi covid-19. Sehingga, bagi masyarakat atau pegendara yang belum divaksin bisa memanfaatkan layanan tersebut secara gratis.
----------------------------------------------------------------------------------
news sentences: 
0 Berbagai upaya dilakukan oleh Pemerintah Daerah untuk mengurangi persebaran virus covid-19 menjelang libur natal dan tahun baru 2022, tidak terkecuali Pemerintah Kabupaten Bogor, Jawa Barat.
1 Seperti yang dilakukan Satlantas Polres Bogor yang telah menyipakan 10 titik posko pemeriksaan ganjil genap dan protokol kesehatan di jalan menuju kawasan wisata Puncak Bogor.
2 Selain pos-pos pemeriksaan, Polres Bogor juga akan memberlakukan sistem ganjil genap dan melakukan pemeriksaan surat hasil swab antigen atau PCR.
3 Check point itu mulai diujicobakan petugas mulai 20 Desember 2021 hingga 2 Januari 2022.
4 Kasatlantas Polres Bogor AKP Dicky Anggi Pranata mengatakan, nantinya di kawasan Puncak Bogor akan berlaku ganjil genap dan juga pemeriksan swab antigen dan PCR.
5 "Kemarin sudah ada formula dan keputusan nanti di Puncak dan sekitarnya akan berlaku ganjil genap dan pemeriksaan swab antigen dan PCR," kata Dicky dalam keterangan resmi, Sabtu (11/12/2021).
6 Hal itu sesuai dengan keputusan dari pertemuan lima Kapolres di wilayah Puncak Raya juga dengan kebijakan Menteri dalam negeri nomor 63, Kementerian Koordinator Bidang Kemaritiman dan Investasi Republik Indonesia serta kebijakan oleh Direktorat Jenderal Perhubungan Darat.
7 Bahwasanya, di beberapa ruas tol salah satunya Tol Bogor sampai Cigombong (Bocimi) itu akan belaku ganjil genap.
8 "Karena itu akan ada penambahan dua pos lagi, saat ini sudah ada delapan pos menjadi 10 pos," ucapnya.
9 Lokasi pos pengamanan masih sama dengan check point ganjil genap yang telah diberlakukan sebelumnya.
10 Beberapa titik pos tersebut antara lain dua titik di kawasan Sentul dan enam titik menuju Puncak.
11 Hanya saja ditambah dua titik lagi di Caringin dan Cigombong.
12 Petugas gabungan menerapkan ganjil genap di depan Gerbang Tol Pasteur Bandung, Jumat (17/9/2021).
13 Sebanyak 640 kendaraan diputarbalikkan lantaran tak sesuai dengan nomor ganjil genap hari ini.
14 "Kendaraan tidak sesuai kita putar balik ke daerah asal. Kalau pemeriksaan PeduliLindungi bukan di kita, tapi tempat tujuan restoran atau wisata," kata Dicky.
15 Tidak hanya pemeriksaan ganjil genap kendaraan dan hasil swab antigen atau PCR, posko-posko itu juga akan melayani vaksinasi covid-19.
16 Sehingga, bagi masyarakat atau pegendara yang belum divaksin bisa memanfaatkan layanan tersebut secara gratis.
```