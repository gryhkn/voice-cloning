import streamlit as st
from streamlit_mic_recorder import mic_recorder
from dotenv import load_dotenv
import os
import replicate
from io import BytesIO

# .env dosyasından değişkenleri yükle
load_dotenv()

# Replicate API anahtarını al
# replicate_api_token = os.getenv('REPLICATE_API_TOKEN')

model = replicate.models.get("lucataco/xtts-v2")
version = model.versions.get("6b2385a9c081443f17041bf1a4caeb36393903f4d7e94468f32e90b2ec57ffc2")

# Replicate API için client oluştur
#client = replicate.Client()

# Streamlit sayfasını başlat
st.title('Ses Klonlama Uygulaması')

# Kullanıcının ses kaydı yapması için arayüz sun
audio = mic_recorder(start_prompt="Kaydı Başlat", stop_prompt="Kaydı Durdur", key='recorder')

if audio:
    # Ses kaydını oynat
    st.audio(audio['bytes'])

    audio_buffer = BytesIO(audio['bytes'])

    # Ses kaydını bir WAV dosyası olarak indirme düğmesi ekleyin
    st.download_button(
        label="Kaydı İndir",
        data=audio['bytes'],
        file_name="kayit.wav",
        mime="audio/wav"
    )

# Kullanıcının okuyacağı metni girebileceği alan
user_text = st.text_area("Klonlanacak metni buraya girin:")

if audio and user_text:
    # Kullanıcı sesi ve metni alındı, işleme başla
    # Kullanıcıya dil seçeneği sun
    language = st.selectbox("Hedef dil seçiniz",
                            ('en', 'es', 'fr', 'de', 'it', 'pt', 'pl', 'tr', 'ru', 'nl', 'cs', 'ar', 'zh', 'hu', 'ko'))
    if st.button('Sesi Klonla'):
        with st.spinner('Ses klonlanıyor...'):
            # Kaydedilen sesi BytesIO nesnesine dönüştür
            audio_bytes_io = BytesIO(audio['bytes'])

            output = replicate.run(
                "lucataco/xtts-v2:6b2385a9c081443f17041bf1a4caeb36393903f4d7e94468f32e90b2ec57ffc2",
                input={
                         "text": user_text,
                         "speaker": audio_bytes_io,
                         "language": "en",
                         "cleanup_voice": True
                }
            )

            if output:
                print("output: ", output)
                # Replicate API'sinden gelen çıktıyı doğrudan kullan
                audio_uri = output  # Artık bu bir string URI olmalı
                st.audio(audio_uri, format='audio/wav')
                st.download_button('Sesi İndir', audio_uri, file_name='cloned_voice.wav')

