import streamlit as st
from streamlit_mic_recorder import mic_recorder
from dotenv import load_dotenv
import replicate
from io import BytesIO

load_dotenv()


model = replicate.models.get("lucataco/xtts-v2")
version = model.versions.get("6b2385a9c081443f17041bf1a4caeb36393903f4d7e94468f32e90b2ec57ffc2")

st.title('Ses Klonlama Uygulaması')

audio = mic_recorder(start_prompt="Kaydı Başlat", stop_prompt="Kaydı Durdur", key='recorder')

if audio:
    st.audio(audio['bytes'])

    audio_buffer = BytesIO(audio['bytes'])

    st.download_button(
        label="Kaydı İndir",
        data=audio['bytes'],
        file_name="kayit.wav",
        mime="audio/wav"
    )

user_text = st.text_area("Konuşma metnini girin:")

if audio and user_text:
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
                audio_uri = output
                st.audio(audio_uri, format='audio/wav')
                st.download_button('Sesi İndir', audio_uri, file_name='cloned_voice.wav')

