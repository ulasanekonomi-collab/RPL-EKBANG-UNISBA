from pathlib import Path
import pandas as pd
import streamlit as st

DATA_FILE = Path(__file__).parent / "data" / "dataset_simulasi_panel_IBC212.csv"
RUBRIC = [
    ("A. Spesifikasi model", 20, "Identifikasi masalah, variabel, persamaan, dan justifikasi teoritis."),
    ("B. Metode estimasi", 25, "OLS, GLS/FGLS yang dijustifikasi, serta pooled, FE, dan RE."),
    ("C. Perangkat lunak", 20, "Pengelolaan data, syntax/script, output yang dapat direplikasi."),
    ("D. Validitas model", 20, "Diagnosis, pemilihan model, dan evaluasi keterbatasan."),
    ("E. Interpretasi ekonomi", 15, "Interpretasi koefisien, kesimpulan, dan implikasi."),
]
LEVEL = {
    4: "Sangat kompeten — mandiri, tepat, konsisten, dan terjustifikasi.",
    3: "Kompeten — benar secara substansi dengan kekurangan kecil.",
    2: "Berkembang — sebagian benar dan masih memerlukan arahan.",
    1: "Belum kompeten — penguasaan belum memadai.",
}

def render_ekonometrika(st):
    st.header("🧮 Asesmen Mata Kuliah: Ekonometrika (IBC212)")
    st.caption("Integrated Competency Assessment | Program Studi Ekonomi Pembangunan")
    st.warning(
        "Prototipe/pilot: autentikasi peran, penyimpanan permanen, dan kontrol akses belum tersedia. "
        "Gunakan data dummy; jangan unggah NIK atau dokumen identitas asli."
    )
    info, tugas, asesor = st.tabs(["📘 Informasi", "🧪 Tugas Peserta", "⚖️ Lembar Skor Asesor"])

    with info:
        a, b, c = st.columns(3)
        a.metric("Kode", "IBC212")
        b.metric("Bobot", "2 SKS")
        c.metric("Model", "ICA")
        st.markdown("**CPMK yang dinilai**")
        st.markdown(
            "- CPMK-1: Menerapkan OLS, GLS, dan model data panel.\n"
            "- CPMK-2: Menggunakan Stata, EViews, R, atau Python untuk estimasi, pengujian, dan penyajian.\n"
            "- CPMK-3: Menginterpretasikan dan mengevaluasi validitas hasil estimasi."
        )
        st.markdown("**Kasus:** Analisis faktor-faktor yang berhubungan dengan tingkat kemiskinan daerah.")
        st.write(
            "Pertanyaan utama: bagaimana hubungan pengangguran, rata-rata lama sekolah, "
            "PDRB per kapita, dan belanja pemerintah per kapita dengan tingkat kemiskinan?"
        )
        st.info("Dataset simulasi: 10 unit wilayah × 10 tahun (2015–2024), 100 observasi balanced panel.")

    with tugas:
        st.subheader("Dataset simulasi inti")
        if DATA_FILE.exists():
            raw = DATA_FILE.read_bytes()
            st.download_button(
                "⬇️ Unduh dataset simulasi CSV", raw,
                file_name="dataset_simulasi_panel_IBC212.csv",
                mime="text/csv", key="ica_dataset"
            )
            try:
                frame = pd.read_csv(DATA_FILE)
                st.dataframe(frame.head(10), use_container_width=True)
                st.caption(str(len(frame)) + " observasi | " +
                           str(frame["id_wilayah"].nunique()) + " unit | " +
                           str(frame["tahun"].min()) + "–" + str(frame["tahun"].max()))
            except Exception as exc:
                st.error("Dataset gagal dibaca: " + str(exc))
        else:
            st.error("Dataset belum ditemukan pada folder data/.")
        st.markdown("**Codebook**")
        st.dataframe(pd.DataFrame([
            ["POV", "Tingkat kemiskinan", "Persen"],
            ["UNEMP", "Tingkat pengangguran terbuka", "Persen"],
            ["SCHOOL", "Rata-rata lama sekolah", "Tahun"],
            ["GRDPPC", "PDRB riil per kapita", "Juta rupiah konstan; indeks simulasi"],
            ["GOVEXP", "Belanja pemerintah per kapita", "Juta rupiah konstan; indeks simulasi"],
        ], columns=["Variabel", "Definisi", "Satuan"]), hide_index=True, use_container_width=True)
        st.error("Seluruh nama wilayah dan angka merupakan data sintetis, bukan data BPS atau wilayah nyata.")
        st.markdown("**Tahapan tugas wajib**")
        st.markdown(
            "1. Rumuskan masalah, variabel, dan spesifikasi model.\n"
            "2. Periksa data, statistik deskriptif, dan estimasi OLS.\n"
            "3. Lakukan diagnosis dan estimasi GLS/FGLS atau pendekatan koreksi yang dijustifikasi.\n"
            "4. Estimasi pooled, fixed effect, dan random effect serta uji pemilihan model.\n"
            "5. Interpretasikan hasil, evaluasi validitas, dan susun kesimpulan.\n"
            "6. Presentasikan pekerjaan dan ikuti verifikasi lisan."
        )
        st.markdown("**Keluaran wajib:** laporan PDF 8–15 halaman, dataset kerja, syntax/script, output estimasi dan pengujian, presentasi, referensi, serta deklarasi penggunaan AI.")
        st.markdown("**Transfer ke data empiris BPS (pengayaan):** dokumentasikan sumber, definisi, periode referensi, satuan, dan harmonisasi. Jangan mengisi nilai hilang dengan perkiraan.")
        st.markdown("- [BPS](https://www.bps.go.id/)\n- [Bappenas — Profil dan Analisis Daerah](https://prada.bappenas.go.id/)")

    with asesor:
        st.subheader("Rubrik penilaian analitik")
        st.caption("Skor ini bersifat prototipe; hasil dapat diunduh, belum tersimpan permanen.")
        peserta = st.text_input("Kode peserta (gunakan kode anonim untuk pilot)", key="ica_peserta")
        penilai = st.text_input("Kode asesor", key="ica_asesor")
        scores, notes = {}, {}
        for i, (label, weight, desc) in enumerate(RUBRIC):
            with st.expander(label + " — bobot " + str(weight) + "%", expanded=True):
                st.caption(desc)
                scores[label] = st.select_slider(
                    "Tingkat kinerja", options=[1, 2, 3, 4], value=3,
                    format_func=lambda x: str(x) + " — " + LEVEL[x], key="ica_level_" + str(i)
                )
                notes[label] = st.text_area("Catatan bukti", key="ica_note_" + str(i), height=70)
        total = sum(w * scores[label] / 4 for label, w, _ in RUBRIC)
        st.metric("Nilai akhir (0–100)", "%.2f" % total)
        cpmk1 = min(scores[RUBRIC[0][0]], scores[RUBRIC[1][0]])
        cpmk2 = scores[RUBRIC[2][0]]
        cpmk3 = min(scores[RUBRIC[3][0]], scores[RUBRIC[4][0]])
        x, y, z = st.columns(3)
        x.metric("CPMK-1", "Level " + str(cpmk1))
        y.metric("CPMK-2", "Level " + str(cpmk2))
        z.metric("CPMK-3", "Level " + str(cpmk3))
        passed = total >= 75 and min(cpmk1, cpmk2, cpmk3) >= 3
        if passed:
            st.success("Memenuhi kriteria usulan: nilai ≥75 dan semua CPMK minimal level 3.")
        else:
            st.warning("Belum memenuhi kriteria usulan; periksa CPMK/dimensi yang belum mencapai level 3.")
        interview = st.text_area("Catatan wawancara/demonstrasi", key="ica_interview")
        if st.button("Buat rekap penilaian", type="primary", key="ica_make_score"):
            if not peserta.strip() or not penilai.strip():
                st.error("Isi kode peserta dan kode asesor.")
            else:
                records = []
                for label, weight, _ in RUBRIC:
                    records.append({
                        "Peserta": peserta.strip(), "Asesor": penilai.strip(),
                        "Dimensi": label, "Bobot": weight, "Skor": scores[label],
                        "Nilai_terbobot": round(weight * scores[label] / 4, 2),
                        "Catatan": notes[label], "Wawancara": interview,
                        "Nilai_akhir": round(total, 2),
                        "CPMK1_level": cpmk1, "CPMK2_level": cpmk2, "CPMK3_level": cpmk3,
                        "Rekomendasi_simulasi": "Memenuhi kriteria usulan" if passed else "Perlu asesmen/perbaikan"
                    })
                result = pd.DataFrame(records)
                st.download_button(
                    "⬇️ Unduh rekap skor CSV",
                    result.to_csv(index=False).encode("utf-8-sig"),
                    file_name="rekap_IBC212_" + peserta.strip().replace(" ", "_") + ".csv",
                    mime="text/csv", key="ica_score_download"
                )
        st.caption("Ambang 75 dan level minimal 3 adalah parameter usulan yang masih harus disahkan prodi. Pemetaan CPMK pada prototipe ini adalah pemetaan awal; keputusan akhir harus mengikuti indikator kritis rubrik resmi.")
