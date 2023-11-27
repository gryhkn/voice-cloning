# Ses Klonlama Uygulaması

Bu proje, kullanıcıların kendi seslerini kullanarak farklı dillerde ses klonlamaları yapmalarını sağlayan bir Streamlit uygulamasıdır. xtts-v2 modelini kullanarak, 10'dan fazla dilde ses üretebilir.

![](https://github.com/gryhkn/voice-cloning/blob/master/ss1.png?raw=true)

## Başlarken

Bu bölüm, projeyi yerel makinenizde nasıl çalıştıracağınıza dair talimatları içerir.

### Önkoşullar

Projeyi çalıştırmadan önce aşağıdaki araçların yüklü olduğundan emin olun:

- Python 3.7 veya daha yeni bir sürüm
- pip (Python paket yöneticisi)
- virtualenv (isteğe bağlı, önerilir)

### Kurulum

Projeyi kurmak ve çalıştırmak için aşağıdaki adımları izleyin:

1. Repoyu klonlayın:

    ```
    git clone https://github.com/gryhkn/voice-cloning.git
    cd voice-cloning
    ```

2. Bir Python sanal ortamı oluşturun (isteğe bağlı):

    ```
    python -m venv venv
    ```

3. Sanal ortamı aktifleştirin(mac):

    ```
    source venv/bin/activate
    ```

4. Gerekli paketleri yükleyin:

    ```
   pip install -r requirements.txt
   ```
5. Uygulamayı çalıştırmak için aşağıdaki komutu kullanın:

    ```
   streamlit run app.py
   ```
   
6. Son olarak [Replicate](https://replicate.com/account/api-tokens) hesabı oluşturup API key alın.
Uygulamanın açılış ekranındaki input alanına bu API keyi girin.