import streamlit as st
import pandas as pd
import os

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="RPL Unisba - Yuhkasun", page_icon="🎓", layout="wide")

# 2. DATABASE KURIKULUM & CPL (Berdasarkan OBE EP Unisba 2023)
DB_KURIKULUM = [
    {"kode": "EP101", "nama": "Pengantar Ekonomi Mikro", "sks": 3},
    {"kode": "EP102", "nama": "Pengantar Ekonomi Makro", "sks": 3},
    {"kode": "EP205", "nama": "Akuntansi Dasar", "sks": 3},
    {"kode": "EP301", "nama": "Kewirausahaan", "sks": 2},
    {"kode": "EP402", "nama": "Manajemen Keuangan", "sks": 3},
    {"kode": "EP505", "nama": "Evaluasi Proyek", "sks": 3},
]

# Mengambil intisari CPL dari dokumen kurikulum yang Akang upload
LIST_CPL = [
    "CPL-1: Mampu menerapkan pemikiran logis, kritis, dan inovatif dalam konteks ekonomi.",
    "CPL-2: Mampu menunjukkan kinerja mandiri, bermutu, dan terukur secara profesional.",
    "CPL-3: Menguasai konsep teoritis ekonomi mikro dan makro secara mendalam.",
    "CPL-4: Mampu melakukan analisis data ekonomi menggunakan perangkat teknologi.",
    "CPL-5: Mampu menyusun rencana bisnis dan evaluasi proyek pembangunan.",
    "CPL-6: Menguasai prinsip-prinsip keuangan syariah dalam pembangunan ekonomi."
]

# 3. HEADER
col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://upload.wikimedia.org/wikipedia/id/8/8c/Logo_Unisba.png", width=100) 
with col2:
    st.title("Portal Rekognisi Pembelajaran Lampau (RPL)")
    st.subheader("Universitas Islam Bandung")

st.divider()

# 4. NAVIGASI TAB
tab1, tab2, tab3 = st.tabs(["📋 Informasi", "📤 Pengajuan E-Portofolio", "📊 Panel Asesor"])

# --- TAB 1: INFORMASI ---
with tab1:
    st.info("**RPL Tipe A:** Pengakuan atas capaian pembelajaran dari pengalaman kerja untuk melanjutkan pendidikan formal.")
    st.markdown("### 🔍 Cek Kelayakan Awal")
    masa = st.number_input("Total Masa Kerja (Tahun)", min_value=0)
    if st.button("Analisis Potensi"):
        if masa >= 2: 
            st.success("Potensi Tinggi! Pengalaman Anda memenuhi kriteria dasar RPL."); st.balloons()
        else:
            st.warning("Masa kerja minimal 2 tahun disarankan untuk hasil maksimal.")

# --- TAB 2: FORM PENDAFTARAN (SELF-ASSESSMENT CPL) ---
with tab2:
    st.header("Formulir E-Portofolio")
    # Menggunakan st.form agar data tidak reset saat berinteraksi
    with st.form("form_rpl_final"):
        st.subheader("1. Identitas Pelamar")
        nama = st.text_input("Nama Lengkap")
        nik = st.text_input("NIK", max_chars=16)
        
        st.divider()
        
        # FITUR: SELF-ASSESSMENT CPL
        st.subheader("2. Klaim Kompetensi (CPL)")
        st.write("Centang Capaian Pembelajaran (CPL) yang menurut Anda sudah Anda kuasai lewat pengalaman kerja:")
        
        cpl_dipilih = []
        for item in LIST_CPL:
            if st.checkbox(item, key=item):
                cpl_dipilih.append(item)
        
        st.divider()
        
        st.subheader("3. Deskripsi & Bukti")
        sektor = st.text_input("Sektor Pekerjaan")
        narasi = st.text_area("Berikan alasan/penjelasan mengapa Anda layak mengklaim CPL tersebut:", height=150)
        
        # TOMBOL UPLOAD (TAYANG KEMBALI)
        st.write("**Unggah Dokumen Portofolio**")
        st.caption("Upload Sertifikat, SK, atau Portofolio (PDF/JPG)")
        uploaded_files = st.file_uploader("Pilih Berkas", accept_multiple_files=True)
        
        st.divider()
        pernyataan = st.checkbox("Saya menjamin keaslian data yang saya kirim.")
        
        if st.form_submit_button("Kirim Pengajuan RPL"):
            if pernyataan and nama and cpl_dipilih:
                # Simpan ke CSV
                nama_file = "data_pendaftar_rpl.csv"
                cpl_string = " | ".join(cpl_dipilih)
                
                df_save = pd.DataFrame({
                    "Nama": [nama], "NIK": [nik], "Sektor": [sektor], 
                    "CPL_Klaim": [cpl_string], "Narasi_Pengalaman": [narasi]
                })
                df_save.to_csv(nama_file, mode='a', index=False, header=not os.path.exists(nama_file))
                st.success("Alhamdulillah, pendaftaran berhasil dikirim!")
            else:
                st.error("Mohon isi nama dan pilih minimal satu CPL yang diklaim.")

# --- TAB 3: PANEL ASESOR ---
with tab3:
    st.header("⚖️ Instrumen Asesmen Asesor")
    if os.path.exists("data_pendaftar_rpl.csv"):
        df_admin = pd.read_csv("data_pendaftar_rpl.csv")
        pilih_nama = st.selectbox("Pilih Pendaftar untuk Dinilai:", df_admin["Nama"].tolist())
        
        if pilih_nama:
            user = df_admin[df_admin["Nama"] == pilih_nama].iloc[0]
            col_l, col_r = st.columns([1, 1])
            
            with col_l:
                st.subheader("🔍 Klaim Applicant")
                st.warning(f"**CPL yang diklaim:**\n{user['CPL_Klaim']}")
                st.info(f"**Narasi Pengalaman:**\n{user['Narasi_Pengalaman']}")
            
            with col_r:
                st.subheader("✅ Verifikasi Mata Kuliah")
                st.write("Pilih Mata Kuliah yang setara dengan klaim di samping:")
                mk_diakui = []
                for mk in DB_KURIKULUM:
                    if st.checkbox(f"{mk['nama']} ({mk['sks']} SKS)", key=f"eval_{mk['kode']}"):
                        mk_diakui.append(mk)
            
            st.divider()
            if mk_diakui:
                st.success(f"**Mata Kuliah Bebas (Diakui):** {sum([m['sks'] for m in mk_diakui])} SKS")
                st.table(pd.DataFrame(mk_diakui))
                
                mk_wajib = [m for m in DB_KURIKULUM if m not in mk_diakui]
                st.warning("**Mata Kuliah yang Harus Ditempuh:**")
                st.table(pd.DataFrame(mk_wajib))
                
                # TOMBOL DOWNLOAD
                res_df = pd.DataFrame({"Kategori":["Diakui", "Wajib"], "Daftar":[str(mk_diakui), str(mk_wajib)]})
                st.download_button("📥 Cetak Hasil Asesmen", res_df.to_csv().encode('utf-8'), f"Hasil_RPL_{pilih_nama}.csv", "text/csv")
    else:
        st.info("Belum ada data pendaftar.")

# 5. FOOTER
st.divider()
st.markdown("<p style='text-align: center; color: gray; font-style: italic;'>Dikembangkan oleh Yuhkasun © 2026</p>", unsafe_allow_html=True)
