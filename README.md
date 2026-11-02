# RPL-EKBANG-UNISBA

Portal Rekognisi Pembelajaran Lampau (RPL) Tipe A Program Studi Ekonomi Pembangunan, Universitas Islam Bandung.

## Menjalankan aplikasi secara lokal

1. Gunakan Python 3.10 atau lebih baru.
2. Instal dependensi: `pip install -r requirements.txt`.
3. Jalankan: `streamlit run rpl.py`.

## Modul saat ini

- Informasi RPL.
- Pengajuan e-portofolio.
- Panel asesor awal.
- Asesmen mata kuliah Ekonometrika IBC212 berbasis Integrated Competency Assessment (ICA).

## Modul asesmen Ekonometrika IBC212

Modul ICA menyediakan ringkasan CPMK, kasus analisis kemiskinan daerah, unduhan dataset simulasi panel, codebook ringkas, instruksi tugas, serta lembar skor asesor dan unduhan rekap penilaian.

Dataset inti berada di `data/dataset_simulasi_panel_IBC212.csv`: 100 observasi, 10 unit wilayah simulasi, tahun 2015–2024. Seluruh nama wilayah dan angka bersifat sintetis, bukan data BPS atau wilayah nyata.

Peserta bebas menggunakan Stata, EViews, R, atau Python. Latihan transfer dengan data BPS merupakan pengayaan dan bukan pengganti dataset simulasi inti.

## Catatan keamanan dan status prototipe

Aplikasi masih berupa prototipe. Autentikasi/otorisasi peserta dan asesor, penyimpanan data persisten, pengelolaan file unggahan yang aman, enkripsi, serta jejak audit belum diterapkan. Jangan gunakan NIK atau dokumen identitas asli sebelum kontrol akses dan penyimpanan aman tersedia. File lokal pada layanan hosting dapat bersifat sementara dan tidak boleh dianggap sebagai database permanen.

Ambang nilai dan aturan keputusan pada modul asesmen masih berupa parameter usulan yang harus divalidasi dan disahkan oleh Tim Prodi.

Dikembangkan oleh Yuhka Sundaya — Ekonomi Pembangunan UNISBA.
