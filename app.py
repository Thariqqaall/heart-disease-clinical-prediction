import streamlit as st
import pandas as pd
import numpy as np
import pickle
import time
import os

# ==============================================================================
# 1. KONFIGURASI HALAMAN (SISTEM KLINIS PROFESIONAL)
# ==============================================================================
st.set_page_config(
    page_title="CardioCare CDSS | Sistem Pendukung Keputusan Klinis",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==============================================================================
# 2. DESIGN SYSTEM & ENTERPRISE STYLING (ZERO EMOJIS, PURE CLINICAL AESTHETICS)
# ==============================================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    color: #0F172A;
}

.stApp {
    background-color: #F8FAFC;
}

.brand-container {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    padding: 1.5rem 0 1.25rem 0;
    border-bottom: 1px solid #E2E8F0;
    margin-bottom: 2rem;
}

.brand-meta {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #0284C7;
    background: #E0F2FE;
    padding: 0.25rem 0.65rem;
    border-radius: 4px;
    margin-bottom: 0.5rem;
}

.brand-title {
    font-size: 1.85rem;
    font-weight: 800;
    letter-spacing: -0.03em;
    color: #0F172A;
    margin: 0;
    line-height: 1.2;
}

.brand-subtitle {
    font-size: 0.9rem;
    color: #64748B;
    margin-top: 0.25rem;
    font-weight: 400;
}

.system-status {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    color: #0F766E;
    background: #F0FDFA;
    padding: 0.45rem 0.85rem;
    border-radius: 6px;
    border: 1px solid #CCFBF1;
    font-weight: 600;
}

.status-dot {
    width: 7px;
    height: 7px;
    background-color: #0D9488;
    border-radius: 50%;
    display: inline-block;
}

.med-panel-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-bottom: 0.75rem;
    margin-bottom: 1.25rem;
    border-bottom: 1px solid #F1F5F9;
}

.panel-title {
    font-size: 0.88rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: #334155;
    margin: 0;
}

.panel-id {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    font-weight: 600;
    color: #94A3B8;
}

.diagnostic-report-card {
    background: #FFFFFF;
    border-radius: 14px;
    padding: 2rem;
    border: 1px solid #E2E8F0;
    box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.05);
    margin-top: 1.5rem;
}

.badge-elevated {
    background: #FFF1F2;
    color: #9F1239;
    border: 1px solid #FECDD3;
    padding: 0.35rem 0.85rem;
    border-radius: 6px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    display: inline-block;
}

.badge-baseline {
    background: #F0FDF4;
    color: #166534;
    border: 1px solid #BBF7D0;
    padding: 0.35rem 0.85rem;
    border-radius: 6px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    display: inline-block;
}

.report-headline {
    font-size: 1.5rem;
    font-weight: 800;
    letter-spacing: -0.02em;
    margin: 0.75rem 0 0.5rem 0;
}

.report-headline-elevated { color: #881337; }
.report-headline-baseline { color: #14532D; }

.report-description {
    font-size: 0.92rem;
    line-height: 1.6;
    color: #475569;
    max-width: 720px;
}

.kpi-block {
    background: #F8FAFC;
    border: 1px solid #E2E8F0;
    border-radius: 10px;
    padding: 1rem 1.25rem;
    text-align: center;
    min-width: 140px;
}

.kpi-value {
    font-size: 1.85rem;
    font-weight: 800;
    letter-spacing: -0.03em;
    line-height: 1;
}

.kpi-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    font-weight: 600;
    color: #64748B;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    margin-top: 0.5rem;
}

.biomarker-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 1.25rem;
    font-size: 0.88rem;
}

.biomarker-table th {
    text-align: left;
    padding: 0.75rem 1rem;
    background: #F8FAFC;
    color: #475569;
    font-weight: 700;
    font-size: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    border-bottom: 2px solid #E2E8F0;
}

.biomarker-table td {
    padding: 0.85rem 1rem;
    border-bottom: 1px solid #F1F5F9;
    color: #334155;
}

.status-flag-abnormal {
    color: #BE123C;
    font-weight: 700;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.8rem;
}

.status-flag-normal {
    color: #059669;
    font-weight: 700;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.8rem;
}

div.stButton > button:first-child {
    background-color: #0F172A;
    color: #FFFFFF;
    font-weight: 600;
    font-size: 0.9rem;
    letter-spacing: 0.01em;
    border-radius: 8px;
    padding: 0.75rem 1.75rem;
    border: 1px solid #0F172A;
    box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
    transition: all 0.15s ease-in-out;
}

div.stButton > button:first-child:hover {
    background-color: #1E293B;
    border-color: #1E293B;
    color: #FFFFFF;
    box-shadow: 0 4px 12px rgba(15, 23, 42, 0.12);
}

div[data-testid="column"] .stButton > button {
    background-color: #FFFFFF;
    color: #334155;
    border: 1px solid #CBD5E1;
    font-size: 0.82rem;
    font-weight: 600;
    border-radius: 6px;
    padding: 0.5rem 1rem;
    box-shadow: none;
}

div[data-testid="column"] .stButton > button:hover {
    background-color: #F8FAFC;
    color: #0F172A;
    border-color: #94A3B8;
}

.stTabs [data-baseweb="tab-list"] {
    gap: 2rem;
    border-bottom: 1px solid #E2E8F0;
    margin-bottom: 1.5rem;
}

.stTabs [data-baseweb="tab"] {
    height: 3rem;
    font-weight: 600;
    font-size: 0.88rem;
    letter-spacing: -0.01em;
    color: #64748B;
    border-bottom: 2px solid transparent;
    padding: 0 0.25rem;
}

.stTabs [aria-selected="true"] {
    color: #0284C7 !important;
    border-bottom-color: #0284C7 !important;
}
</style>
""", unsafe_allow_html=True)


# ==============================================================================
# 3. HEADER IDENTITAS SISTEM
# ==============================================================================
st.markdown("""
<div class="brand-container">
    <div>
        <div class="brand-meta">Sistem Diagnostik Kardiovaskular | Protokol v2.4</div>
        <h1 class="brand-title">CardioCare Kecerdasan Klinis</h1>
        <div class="brand-subtitle">Stratifikasi Risiko & Deteksi Dini Penyakit Jantung Koroner (PJK / CAD)</div>
    </div>
    <div class="system-status">
        <span class="status-dot"></span>
        <span>Status Mesin: Random Forest Tervalidasi (ROC-AUC 0.91)</span>
    </div>
</div>
""", unsafe_allow_html=True)


# ==============================================================================
# 4. LOAD MODEL & NORMALIZER
# ==============================================================================
def load_assets():
    model_file = "best_model_rf.pkl" if os.path.exists("best_model_rf.pkl") else "generate_heart_disease.pkl"
    scaler_file = "scaler.pkl"
    
    loaded_model = None
    loaded_scaler = None
    
    if os.path.exists(model_file):
        with open(model_file, "rb") as f:
            loaded_model = pickle.load(f)
            
    if os.path.exists(scaler_file):
        with open(scaler_file, "rb") as f:
            loaded_scaler = pickle.load(f)
            
    return loaded_model, loaded_scaler

model, scaler = load_assets()

if model is None:
    st.error("File model diagnostik (`best_model_rf.pkl`) tidak ditemukan di folder kerja.")
    st.stop()


# ==============================================================================
# 5. TABULASI DASHBOARD
# ==============================================================================
tab_single, tab_batch, tab_protocol = st.tabs([
    "Panel Diagnosis Pasien", 
    "Skrining Kohort (Unggah CSV)", 
    "Spesifikasi Model & Validasi"
])


# ==============================================================================
# TAB 1: DIAGNOSIS MANDIRI (SINGLE PATIENT)
# ==============================================================================
with tab_single:
    st.markdown("##### Simulasi Profil Klinis Pasien (Pintasan Demo):")
    col_p1, col_p2, col_p3 = st.columns([1, 1, 2])
    
    # Inisialisasi state awal
    if "p_age" not in st.session_state:
        st.session_state.p_age = 50
        st.session_state.p_sex = "Pria"
        st.session_state.p_cp = "0: Angina Tipikal"
        st.session_state.p_thalach = 145
        st.session_state.p_exang = "Negatif (0)"
        st.session_state.p_oldpeak = 1.0
        st.session_state.p_slope = "1: Datar (Flat)"
        st.session_state.p_ca = 0
        st.session_state.p_thal = "1: Normal"

    # Profil Kasus A: Risiko Tinggi (Kelas 1)
    with col_p1:
        if st.button("Profil Kasus A: Risiko Tinggi PJK (Kelas 1)", use_container_width=True):
            st.session_state.p_age = 62
            st.session_state.p_sex = "Pria"
            st.session_state.p_cp = "0: Angina Tipikal"
            st.session_state.p_thalach = 115
            st.session_state.p_exang = "Positif (1)"
            st.session_state.p_oldpeak = 3.2
            st.session_state.p_slope = "0: Menurun (Downsloping)"
            st.session_state.p_ca = 2
            st.session_state.p_thal = "3: Cacat Reversibel"
            st.rerun()

    # Profil Kasus B: Fisiologis Normal (Kelas 0)
    with col_p2:
        if st.button("Profil Kasus B: Fisiologis Normal (Kelas 0)", use_container_width=True):
            st.session_state.p_age = 42
            st.session_state.p_sex = "Perempuan"
            st.session_state.p_cp = "2: Nyeri Non-anginal"
            st.session_state.p_thalach = 172
            st.session_state.p_exang = "Negatif (0)"
            st.session_state.p_oldpeak = 0.2
            st.session_state.p_slope = "2: Menaik (Upsloping)"
            st.session_state.p_ca = 0
            st.session_state.p_thal = "1: Normal"
            st.rerun()

    st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)

    # Panel Form Klinis 3 Kolom
    col_panel1, col_panel2, col_panel3 = st.columns(3)

    with col_panel1:
        st.markdown("""
        <div class="med-panel-header">
            <span class="panel-title">1. Demografi & Gejala Pasien</span>
            <span class="panel-id">BAGIAN-01</span>
        </div>
        """, unsafe_allow_html=True)
        
        age = st.slider("Usia Pasien (Tahun)", 20, 85, int(st.session_state.p_age))
        
        sex_idx = 0 if st.session_state.p_sex == "Pria" else 1
        sex_str = st.radio("Jenis Kelamin Biologis", ["Pria", "Perempuan"], index=sex_idx, horizontal=True)
        sex = 1 if sex_str == "Pria" else 0
        
        cp_options = [
            "0: Angina Tipikal",
            "1: Angina Atipikal", 
            "2: Nyeri Non-anginal", 
            "3: Asimtomatik"
        ]
        cp_idx = cp_options.index(st.session_state.p_cp) if st.session_state.p_cp in cp_options else 0
        cp_selected = st.selectbox("Klasifikasi Nyeri Dada (cp)", cp_options, index=cp_idx)
        cp = int(cp_selected[0])

    with col_panel2:
        st.markdown("""
        <div class="med-panel-header">
            <span class="panel-title">2. Elektrokardiogram Uji Latih</span>
            <span class="panel-id">BAGIAN-02</span>
        </div>
        """, unsafe_allow_html=True)
        
        thalach = st.slider("Detak Jantung Maksimal (bpm)", 70, 210, int(st.session_state.p_thalach))
        
        exang_idx = 1 if "Positif" in st.session_state.p_exang or "Ya" in st.session_state.p_exang else 0
        exang_str = st.radio("Angina Akibat Aktivitas Fisik (exang)", ["Negatif (0)", "Positif (1)"], index=exang_idx, horizontal=True)
        exang = 1 if "Positif" in exang_str else 0
        
        oldpeak = st.slider("Depresi Segmen ST (oldpeak dalam mm)", 0.0, 6.0, float(st.session_state.p_oldpeak), step=0.1)
        
        slope_options = ["0: Menurun (Downsloping)", "1: Datar (Flat)", "2: Menaik (Upsloping)"]
        slope_idx = slope_options.index(st.session_state.p_slope) if st.session_state.p_slope in slope_options else 2
        slope_selected = st.selectbox("Kemiringan Segmen ST Latihan (slope)", slope_options, index=slope_idx)
        slope = int(slope_selected[0])

    with col_panel3:
        st.markdown("""
        <div class="med-panel-header">
            <span class="panel-title">3. Pemeriksaan Diagnostik Khusus</span>
            <span class="panel-id">BAGIAN-03</span>
        </div>
        """, unsafe_allow_html=True)
        
        ca = st.selectbox("Jumlah Pembuluh Darah Terwarnai Fluoroskopi (ca)", [0, 1, 2, 3], index=int(st.session_state.p_ca))
        
        thal_options = ["1: Normal", "2: Cacat Tetap", "3: Cacat Reversibel"]
        thal_idx = thal_options.index(st.session_state.p_thal) if st.session_state.p_thal in thal_options else 1
        thal_selected = st.selectbox("Hasil Skintigrafi Thallium (thal)", thal_options, index=thal_idx)
        thal = int(thal_selected[0])

    st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)

    # Tombol Eksekusi
    eval_trigger = st.button("Jalankan Evaluasi Risiko Klinis", use_container_width=True)

    if eval_trigger:
        patient_record = pd.DataFrame([{
            'cp': float(cp),
            'thalach': float(thalach),
            'slope': float(slope),
            'oldpeak': float(oldpeak),
            'exang': float(exang),
            'ca': float(ca),
            'thal': float(thal),
            'sex': float(sex),
            'age': float(age)
        }])

        with st.spinner("Memproses vektor klinis pasien via Random Forest Classifier..."):
            time.sleep(0.35)
            
            X_eval = patient_record.copy()
            if scaler is not None:
                X_eval = scaler.transform(X_eval)
                
            prediction = model.predict(X_eval)[0]
            proba = model.predict_proba(X_eval)[0] if hasattr(model, "predict_proba") else [0.5, 0.5]
            risk_score = proba[1] * 100

        is_elevated = (prediction == 1)

        badge_html = '<span class="badge-elevated">EVALUASI: INDIKASI RISIKO TINGGI PJK</span>' if is_elevated else '<span class="badge-baseline">EVALUASI: PARAMETER FISIOLOGIS NORMAL</span>'
        headline_class = 'report-headline-elevated' if is_elevated else 'report-headline-baseline'
        headline_text = 'Probabilitas Signifikan Penyakit Arteri Koroner' if is_elevated else 'Profil Risiko Kardiovaskular Rendah / Sehat'
        desc_text = 'Kombinasi penanda biomarker dan respon uji beban menunjukkan keselarasan diagnostik kuat dengan stenosis arteri koroner (Kelas 1) yang memerlukan tindak lanjut dokter spesialis.' if is_elevated else 'Parameter yang diobservasi berada dalam batas variasi fisiologis normal tanpa ditemukan indikator iskemia akut selama evaluasi beban.'
        kpi_color = '#9F1239' if is_elevated else '#166534'
        cat_text = 'KELAS I (TINGGI)' if is_elevated else 'KELAS 0 (RENDAH)'

        # Output HTML tanpa indentasi agar tidak terinterpretasi sebagai code block
        report_html = f"""<div class="diagnostic-report-card">
<div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 1.5rem;">
<div>
{badge_html}
<h2 class="report-headline {headline_class}">{headline_text}</h2>
<p class="report-description">{desc_text}</p>
</div>
<div style="display: flex; gap: 1rem;">
<div class="kpi-block">
<div class="kpi-value" style="color: {kpi_color};">{risk_score:.1f}%</div>
<div class="kpi-label">Skor Risiko PJK</div>
</div>
<div class="kpi-block">
<div class="kpi-value" style="color: #0F172A;">{cat_text}</div>
<div class="kpi-label">Kategori Risiko</div>
</div>
</div>
</div>
<table class="biomarker-table">
<thead>
<tr>
<th>Parameter Klinis</th>
<th>Nilai Terobservasi Pasien</th>
<th>Batas Acuan Fisiologis</th>
<th>Signifikansi Diagnostik</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Klasifikasi Nyeri Dada</strong></td>
<td>{cp_selected}</td>
<td>Tipikal vs Non-angina</td>
<td><span class="{'status-flag-abnormal' if cp > 0 else 'status-flag-normal'}">{'Pola Nyeri Atipikal/Non-angina' if cp > 0 else 'Pola Nyeri Angina Tipikal'}</span></td>
</tr>
<tr>
<td><strong>Depresi Segmen ST</strong></td>
<td>{oldpeak:.1f} mm</td>
<td>&lt; 1.0 mm (Relatif Istirahat)</td>
<td><span class="{'status-flag-abnormal' if oldpeak >= 1.0 else 'status-flag-normal'}">{'Meningkat (Indikator Iskemik)' if oldpeak >= 1.0 else 'Rentang Normal Fisiologis'}</span></td>
</tr>
<tr>
<td><strong>Fluoroskopi Pembuluh Mayor</strong></td>
<td>{ca} pembuluh terwarnai</td>
<td>0 pembuluh</td>
<td><span class="{'status-flag-abnormal' if ca > 0 else 'status-flag-normal'}">{f'{ca} Pembuluh Terhambat' if ca > 0 else 'Normal (Pembuluh Paten)'}</span></td>
</tr>
<tr>
<td><strong>Detak Jantung Maksimal</strong></td>
<td>{thalach} bpm</td>
<td>Estimasi Usia: ~{220 - age} bpm</td>
<td><span class="{'status-flag-normal' if thalach >= 140 else 'status-flag-abnormal'}">{'Respon Beban Memadai' if thalach >= 140 else 'Respon Kronotropik Tumpul'}</span></td>
</tr>
</tbody>
</table>
</div>"""

        st.markdown(report_html, unsafe_allow_html=True)
        st.markdown("<div style='height: 15px;'></div>", unsafe_allow_html=True)

        if is_elevated:
            st.error("""
            **Rekomendasi Protokol Klinis:**
            * Rujukan langsung ke kardiolog untuk evaluasi angiografi koroner elektif (CAG).
            * Pemeriksaan profil lipid lengkap dan pertimbangan terapi medikamentosa terarah berbasis pedoman (GDMT).
            """)
        else:
            st.success("""
            **Rekomendasi Protokol Klinis:**
            * Penilaian ulang risiko kardiovaskular secara berkala disarankan setiap 12 bulan.
            * Lanjutkan upaya pencegahan primer melalui pola hidup sehat dan pemantauan tekanan darah rutin.
            """)


# ==============================================================================
# TAB 2: SKRINING KOHORT (UNGGAH CSV)
# ==============================================================================
with tab_batch:
    st.markdown("""
    <div style="margin-bottom: 1.25rem;">
        <h4 style="margin: 0; font-weight: 700; color: #1E293B;">Mesin Skrining Pasien Masal (Kohort)</h4>
        <p style="color: #64748B; font-size: 0.88rem; margin-top: 0.25rem;">Evaluasi terotomatisasi untuk basis data rekam medis pasien rumah sakit secara kolektif.</p>
    </div>
    """, unsafe_allow_html=True)

    up_file = st.file_uploader("Pilih Berkas CSV Rekam Medis Pasien", type=["csv"], label_visibility="collapsed")

    if up_file is not None:
        cohort_df = pd.read_csv(up_file)
        st.markdown("##### Pratinjau Basis Data Pasien (5 Pasien Teratas):")
        st.dataframe(cohort_df.head(), use_container_width=True)

        req_columns = ['cp', 'thalach', 'slope', 'oldpeak', 'exang', 'ca', 'thal', 'sex', 'age']
        missing_cols = [c for c in req_columns if c not in cohort_df.columns]

        if missing_cols:
            st.error(f"Format berkas tidak kompatibel. Kolom wajib berikut tidak ditemukan: {missing_cols}")
        else:
            if st.button("Jalankan Stratifikasi Masal", use_container_width=True):
                X_batch = cohort_df[req_columns].copy()
                if scaler is not None:
                    X_batch_scaled = scaler.transform(X_batch)
                else:
                    X_batch_scaled = X_batch
                    
                preds = model.predict(X_batch_scaled)
                cohort_df['Kelas_Diagnostik'] = ['Risiko Tinggi (Kelas 1)' if p == 1 else 'Risiko Rendah (Kelas 0)' for p in preds]
                
                if hasattr(model, "predict_proba"):
                    probs = model.predict_proba(X_batch_scaled)[:, 1]
                    cohort_df['Probabilitas_Risiko_PJK (%)'] = np.round(probs * 100, 1)

                st.markdown(f"##### Hasil Stratifikasi ({len(cohort_df)} Pasien Berhasil Dievaluasi):")
                st.dataframe(cohort_df, use_container_width=True)

                csv_bytes = cohort_df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="Unduh Laporan Evaluasi Kohort (CSV)",
                    data=csv_bytes,
                    file_name="hasil_evaluasi_kohort_jantung.csv",
                    mime="text/csv"
                )


# ==============================================================================
# TAB 3: SPESIFIKASI MODEL & VALIDASI KLINIS
# ==============================================================================
with tab_protocol:
    st.markdown("""
    <div style="margin-bottom: 1.25rem;">
        <h4 style="margin: 0; font-weight: 700; color: #1E293B;">Arsitektur Model & Tolok Ukur Validasi</h4>
        <p style="color: #64748B; font-size: 0.88rem; margin-top: 0.25rem;">Metrik evaluasi statistik yang diperoleh selama Capstone Sesi 13 & 14.</p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown("""
        <div class="kpi-block">
            <div class="kpi-value" style="color: #0284C7;">0.91</div>
            <div class="kpi-label">Skor ROC-AUC</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="kpi-block">
            <div class="kpi-value" style="color: #059669;">87.7%</div>
            <div class="kpi-label">Akurasi Uji</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="kpi-block">
            <div class="kpi-value">5-Fold</div>
            <div class="kpi-label">Validasi Silang</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="kpi-block">
            <div class="kpi-value">9</div>
            <div class="kpi-label">Fitur Klinis</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

    st.markdown("""
    ##### Spesifikasi Arsitektur Sistem:
    * **Algoritma Utama:** *Tuned Random Forest Classifier* (Ensemble pohon keputusan dengan teknik bagging dan subsampling fitur).
    * **Optimasi Hyperparameter:** Menggunakan *5-Fold Stratified GridSearchCV* dengan target metrik Area Under ROC Curve (`roc_auc`).
    * **Normalisasi Fitur:** Standarisasi z-score (`StandardScaler`) diterapkan merata pada seluruh dimensi numerik kontinu dan ordinal.
    * **Basis Data Acuan:** *Cleveland Heart Disease Database*, University of California Irvine (UCI).
    * **Tujuan Penggunaan:** *Clinical Decision Support System (CDSS)* sebagai alat bantu triase skrining dan rujukan diagnostik.
    """)
