# -*- coding: utf-8 -*-
import streamlit as st
import time

# --- SAYFA AYARLARI ---
st.set_page_config(
    page_title="İyi ki Doğdun Abla!",
    page_icon="🎂",
    layout="centered"
)

# --- 1v2 KURALI: KOYU TEMA VE NEON TASARIM ---
st.markdown("""
<style>
    /* Arka plan ve genel yazı rengi */
    .stApp { background-color: #0b0f19; color: #f2f4f8; }
    
    /* Neon Yeşili Başlıklar */
    h1, h2, h3 { color: #39ff14 !important; text-align: center; font-family: 'Courier New', Courier, monospace; }
    
    /* Neon Mavi Buton Tasarımı */
    .stButton>button { 
        background-color: #1a1a1a; 
        color: #00ffff; 
        border: 2px solid #00ffff;
        border-radius: 10px;
        font-size: 22px;
        font-weight: bold;
        width: 100%;
        padding: 10px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #39ff14;
        color: #000000;
        border: 2px solid #39ff14;
    }
    
    /* Özel Neon Not Kutusu */
    .not-kutusu {
        background-color: #161b22;
        border-left: 5px solid #ff00ff; /* Neon Pembe Çizgi */
        padding: 25px;
        border-radius: 8px;
        font-size: 20px;
        font-style: italic;
        color: #e2e8f0;
        text-align: center;
        box-shadow: 0 0 15px #ff00ff; /* Neon parlama efekti */
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# --- HAFIZA KONTROLÜ (Mumun durumunu tutmak için) ---
if "mum_sondu" not in st.session_state:
    st.session_state.mum_sondu = False

# --- ANA EKRAN ---
st.title("🎉 İYİ Kİ DOĞDUN ABLA! 🎮")
st.markdown("---")

# Dinamik alan oluşturuyoruz (Animasyon için)
pasta_alani = st.empty()

# EĞER MUMLAR HENÜZ SÖNDÜRÜLMEDİYSE:
if not st.session_state.mum_sondu:
    pasta_alani.markdown("<h1 style='font-size: 100px; text-align: center;'>🎂🕯️</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px; color: #a7f3d0;'>Yeni yaşın kutlu olsun! Dileğini tut ve aşağıdaki butona basarak mumları üfle.</p>", unsafe_allow_html=True)
    
    st.write("") # Boşluk
    # Üfleme Butonu
    if st.button("💨 Mumları Üfle!"):
        st.session_state.mum_sondu = True
        st.rerun() # Sayfayı anında yenile ki mum sönsün

# EĞER MUMLAR SÖNDÜRÜLDÜYSE:
else:
    # Yanan mum gitti, dumanı tüten sönmüş mum geldi
    pasta_alani.markdown("<h1 style='font-size: 100px; text-align: center;'>🎂💨</h1>", unsafe_allow_html=True)
    
    # Kutlama Efekti (Balonlar Uçuşur)
    st.balloons()
    
    # O Mükemmel Özel Not Çıkar
    st.markdown(
        """
        <div class='not-kutusu'>
        "Abla, iyi ki varsın. Oyunlardaki o makara sohbetlerin ve samimiyetin cidden bambaşka. Sen benim için her zaman o 23 ablasın, nice güzel yaşlara!"
        </div>
        """, 
        unsafe_allow_html=True
    )