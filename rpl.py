import streamlit as st
import pandas as pd
import os

# 1. KONFIGURASI HALAMAN
st.set_page_config(page_title="RPL Unisba - Yuhkasun", page_icon="🎓", layout="wide")

# 2. DATABASE KURIKULUM & CPL (OBE EP UNISBA 2023)
DB_KURIKULUM = [
    {"kode": "EP101", "nama": "Pengantar Ekonomi Mikro", "sks": 3},
    {"kode": "EP102", "nama": "Pengantar Ekonomi Makro", "sks": 3},
    {"kode": "EP205", "nama": "Akuntansi Dasar", "sks": 3},
    {"kode": "EP301", "nama": "Kewirausahaan", "sks": 2},
    {"kode": "EP402", "nama": "Manajemen Keuangan", "sks": 3},
    {"kode": "EP505", "nama": "Evaluasi Proyek", "sks": 3},
]

LIST_CPL = [
    "CPL-1: Mampu menerapkan pemikiran logis dan inovatif.",
    "CPL-2: Mampu menunjukkan kinerja mandiri dan terukur.",
    "CPL-3: Menguasai konsep teoritis ekonomi mikro dan makro.",
    "CPL-4: Mampu melakukan analisis data ekonomi.",
    "CPL-5: Mampu menyusun rencana bisnis & evaluasi proyek.",
    "CPL-6: Menguasai prinsip keuangan syariah & pembangunan."
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
    st.info("**RPL Tipe A:** Pengakuan pengalaman kerja menjadi SKS akademik.")
    st.markdown("### 🔍 Cek Kelayakan Awal")
    masa = st.number_input("Masa Kerja (Tahun)", min_value=0, key="cek_masa")
    if st.button("Analisis Potensi"):
        if masa >= 2: st.success("Potensi Tinggi!"); st.balloons()
        else: st.warning("Disarankan minimal 2 tahun masa kerja.")

# --- TAB 2: FORM PENDAFTARAN (DENGAN CHECKLIST CPL & UPLOAD) ---
with tab2:
    st.header("Formulir E-Portofolio")
    with st.form("form_rpl_final"):
        st.subheader("1. Identitas")
        nama = st.text_input("Nama Lengkap")
        nik = st.text_input("NIK", max_chars=16)
        
        st.divider()
        st.subheader("2. Self-Assessment CPL")
        st.write("Centang CPL yang menurut Anda sudah dikuasai:")
        cpl_user = []
        for c in LIST_CPL:
            if st.checkbox(c, key=f"user_{c}"):
                cpl_user.append(c)
        
        st.divider()
        st.subheader("3. Narasi & Bukti")
        sektor = st.text_input("Sektor Pekerjaan")
        narasi = st.text_area("Berikan penjelasan detail pengalaman Anda:", height=150)
        
        # Tombol Upload Syarat
        uploaded_files = st.file_uploader("Unggah Bukti Portofolio (PDF/JPG)", accept_multiple_files=True)
        
        pernyataan = st.checkbox("Saya menjamin keaslian data.")
        submit = st.form_submit_button("Kirim Pengajuan RPL")
        
        if submit:
            if pernyataan and nama and cpl_user:
                df_save = pd.DataFrame({
                    "Nama": [nama], "NIK": [nik], "Sektor": [sektor], 
                    "CPL_Klaim": [" | ".join(cpl_user)], "Narasi": [narasi]
                })
                df_save.to_csv("data_rpl.csv", mode='a', index=False, header=not os.path.exists("data_rpl.csv"))
                st.success("Pendaftaran Berhasil!")
            else:
                st.error("Lengkapi data dan pilih minimal satu CPL.")

# --- TAB 3: PANEL ASESOR (PERBAIKAN ERROR) ---
with tab3:
    st.header("⚖️ Instrumen Asesmen")
    if os.path.exists("data_rpl.csv"):
        df_admin = pd.read_csv("data_rpl.csv")
        pilih_nama = st.selectbox("Pilih Pendaftar:", df_admin["Nama"].tolist())
        
        if pilih_nama:
            user = df_admin[df_admin["Nama"] == pilih_nama].iloc[0]
            col_l, col_r = st.columns([1, 1])
            
            with col_l:
                st.warning(f"**Klaim CPL:**\n{user['CPL_Klaim']}")
                st.info(f"**Narasi:**\n{user['Narasi']}")
            
            with col_r:
                st.subheader("✅ Pairing Mata Kuliah")
                mk_diakui = []
                for mk in DB_KURIKULUM:
                    if st.checkbox(f"{mk['nama']}", key=f"eval_{mk['kode']}"):
                        mk_diakui.append(mk)
            
            st.divider()
            # Logika agar tidak error jika tabel kosong
            if mk_diakui:
                st.success(f"**Mata Kuliah Diakui:** {sum([m['sks'] for m in mk_diakui])} SKS")
                st.table(pd.DataFrame(mk_diakui))
            else:
                st.info("Belum ada Mata Kuliah yang dicentang untuk diakui.")
                
            mk_wajib = [m for m in DB_KURIKULUM if m not in mk_diakui]
            if mk_wajib:
                st.warning("**Mata Kuliah Wajib Tempuh:**")
                st.table(pd.DataFrame(mk_wajib))
                
            # Tombol Download
            if mk_diakui:
                res_df = pd.DataFrame({"Kategori":["Diakui", "Wajib"], "Daftar":[str(mk_diakui), str(mk_wajib)]})
                st.download_button("📥 Download Hasil", res_df.to_csv().encode('utf-8'), f"RPL_{pilih_nama}.csv", "text/csv")
    else:
        st.info("Belum ada data pendaftar.")

# 5. FOOTER (Catatan Pengembangan)
st.divider()
st.markdown("<p style='text-align: center; color: gray; font-size: 0.8rem; font-style: italic;'>Dikembangkan oleh Yuhkasun 2026</p>", unsafe_allow_html=True)
