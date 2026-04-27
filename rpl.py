import streamlit as st
import pandas as pd
import os

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="RPL Unisba - Yuhkasun", page_icon="🎓", layout="wide")

# 2. DATABASE KURIKULUM (Berdasarkan Dokumen OBE EP 2023)
DB_KURIKULUM = [
    {"kode": "EP101", "nama": "Pengantar Ekonomi Mikro", "sks": 3},
    {"kode": "EP102", "nama": "Pengantar Ekonomi Makro", "sks": 3},
    {"kode": "EP205", "nama": "Akuntansi Dasar", "sks": 3},
    {"kode": "EP301", "nama": "Kewirausahaan", "sks": 2},
    {"kode": "EP402", "nama": "Manajemen Keuangan", "sks": 3},
    {"kode": "EP505", "nama": "Evaluasi Proyek", "sks": 3},
    {"kode": "EP306", "nama": "Ekonomi Sektoral", "sks": 3},
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
    st.info("**Apa itu RPL Tipe A?** Pengakuan pengalaman kerja menjadi SKS akademik (Juknis 2025).")
    st.markdown("### 🔍 Cek Kelayakan Awal")
    c1, c2 = st.columns(2)
    with c1:
        ijazah = st.selectbox("Ijazah Terakhir", ["Pilih", "SMA/SMK/MA", "Diploma", "Putus Kuliah"])
        masa = st.number_input("Masa Kerja (Tahun)", min_value=0)
    if st.button("Analisis Potensi"):
        if masa >= 2: st.success("Potensi Tinggi!"); st.balloons()

# --- TAB 2: FORM PENDAFTARAN ---
with tab2:
    with st.form("form_rpl"):
        nama = st.text_input("Nama Lengkap")
        nik = st.text_input("NIK", max_chars=16)
        sektor = st.text_input("Sektor Pekerjaan")
        narasi = st.text_area("Ceritakan Pengalaman Kerja Anda secara Detail", height=150)
        st.divider()
        pernyataan = st.checkbox("Saya menjamin keaslian data.")
        if st.form_submit_button("Kirim Pengajuan"):
            if pernyataan and nama:
                df = pd.DataFrame({"Nama":[nama], "NIK":[nik], "Sektor":[sektor], "Narasi_Pengalaman":[narasi]})
                df.to_csv("data_pendaftar_rpl.csv", mode='a', index=False, header=not os.path.exists("data_pendaftar_rpl.csv"))
                st.success("Data Berhasil Disimpan!")

# --- TAB 3: PANEL ASESOR (INSTRUMEN CHECKLIST) ---
with tab3:
    st.header("⚖️ Instrumen Asesmen RPL")
    if os.path.exists("data_pendaftar_rpl.csv"):
        df_admin = pd.read_csv("data_pendaftar_rpl.csv")
        pilih_nama = st.selectbox("Pilih Pendaftar:", df_admin["Nama"].tolist())
        
        if pilih_nama:
            user = df_admin[df_admin["Nama"] == pilih_nama].iloc[0]
            col_d, col_c = st.columns([1, 1])
            with col_d:
                st.info(f"**Narasi {pilih_nama}:**\n\n{user['Narasi_Pengalaman']}")
            with col_c:
                st.subheader("✅ Pairing Kurikulum")
                mk_diakui = []
                for mk in DB_KURIKULUM:
                    if st.checkbox(f"{mk['nama']} ({mk['sks']} SKS)", key=mk['kode']):
                        mk_diakui.append(mk)

            st.divider()
            st.subheader("📊 Hasil Rekomendasi")
            
            # 1. MK DIAKUI
            st.success("**1. Mata Kuliah yang Diakui (Sesuai Pengalaman)**")
            if mk_diakui: st.table(pd.DataFrame(mk_diakui))
            
            # 2. MK WAJIB
            mk_wajib = [m for m in DB_KURIKULUM if m not in mk_diakui]
            st.warning("**2. Mata Kuliah yang Harus Ditempuh**")
            if mk_wajib: st.table(pd.DataFrame(mk_wajib))
            
            # TOMBOL DOWNLOAD HASIL
            res_df = pd.DataFrame({"Kategori":["Diakui", "Wajib"], "Daftar":[str(mk_diakui), str(mk_wajib)]})
            st.download_button("📥 Download Hasil Asesmen (CSV)", res_df.to_csv().encode('utf-8'), f"RPL_{pilih_nama}.csv", "text/csv")
    else:
        st.info("Belum ada data pendaftar.")

# 5. FOOTER
st.divider()
st.markdown("<p style='text-align: center; color: gray; font-style: italic;'>Dikembangkan oleh Yuhkasun © 2026</p>", unsafe_allow_html=True)
