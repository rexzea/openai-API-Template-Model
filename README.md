# OpenAI API Template Model

Sebuah template chatbot interaktif yang menggunakan OpenAI API dengan antarmuka grafis berbasis Python. Project ini menyediakan implementasi sederhana untuk membangun chatbot yang dapat berkomunikasi menggunakan model bahasa OpenAI.

##  Fitur

-  Integrasi langsung dengan OpenAI API
-  Antarmuka grafis yang user-friendly (Pygame/PyQt5)
-  Percakapan real-time dengan AI
-  Template yang mudah dikustomisasi
-  Riwayat percakapan
-  Konfigurasi yang fleksibel

##  Prasyarat

Sebelum memulai, pastikan Anda memiliki:

- Python 3.7 atau versi lebih baru
- Akun OpenAI dan API Key
- pip (Python package installer)

##  Instalasi

### 1. Clone Repository

```bash
git clone https://github.com/rexzea/openai-API-Template-Model.git
cd openai-API-Template-Model
```

### 2. Buat Virtual Environment (Opsional tapi Direkomendasikan)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Atau install manual:

```bash
pip install openai pygame PyQt5 python-dotenv
```

##  Setup OpenAI API

### 1. Dapatkan API Key

1. Kunjungi [OpenAI Platform](https://platform.openai.com/)
2. Buat akun atau login
3. Navigasi ke **API Keys** di dashboard
4. Klik **Create new secret key**
5. Salin API key yang dihasilkan

### 2. Konfigurasi API Key

#### Metode 1: Environment Variables (Direkomendasikan)

Buat file `.env` di root directory project:

```env
OPENAI_API_KEY=your_api_key_here (ganti API kamu disini)
```

#### Metode 2: Langsung di Code

Edit file konfigurasi dan masukkan API key Anda:

```python
# config.py
OPENAI_API_KEY = "your_api_key_here" (ganti API kamu disini)
```

**⚠️ Catatan:** Jangan commit API key ke repository publik

##  Cara Menjalankan

### Menjalankan dengan Pygame

```bash
python main_pygame.py
```

### Menjalankan dengan PyQt5

```bash
python main_pyqt.py
```

### Bisa langsung klik tombol run di Python

## ⚙ Konfigurasi

Edit `config.py` untuk menyesuaikan pengaturan:

```python
# Model OpenAI yang digunakan
MODEL = "gpt-3.5-turbo"  # atau "gpt-4"

# Parameter model
MAX_TOKENS = 150
TEMPERATURE = 0.7

# Pengaturan UI
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
```

##  Penggunaan

1. **Jalankan aplikasi** menggunakan salah satu command di atas
2. **Ketik pesan** Anda di input field
3. **Tekan Enter** atau klik tombol Send
4. **AI akan merespon** dalam beberapa detik
5. **Percakapan tersimpan** dalam session yang aktif

## Kustomisasi

### Mengubah Personality AI

Edit prompt sistem di `openai_client.py`:

```python
system_message = {
    "role": "system", 
    "content": "Kamu adalah asisten AI yang ramah dan membantu..."
}
```

### Menambah Fitur UI

- **Pygame**: Edit `gui_pygame.py`
- **PyQt5**: Edit `gui_pyqt.py`

##  Requirements.txt

```txt
openai>=1.0.0
pygame>=2.1.0
PyQt5>=5.15.0
python-dotenv>=0.19.0
requests>=2.25.0
```

##  Troubleshooting

### Error: "OpenAI API key not found"
- Pastikan file `.env` exists dan berisi API key yang valid
- Cek bahwa API key tidak expired

### Error: "Module not found"
- Jalankan `pip install -r requirements.txt`
- Pastikan virtual environment aktif

### Error: "Rate limit exceeded"
- Anda telah mencapai batas penggunaan API
- Tunggu beberapa saat atau upgrade plan OpenAI

### Error: "Invalid API key"
- Cek kembali API key di OpenAI dashboard
- Pastikan API key dikopi dengan benar

##  Biaya API

OpenAI API berbayar berdasarkan penggunaan:
- **GPT-3.5-turbo**: ~$0.002 per 1K tokens
- **GPT-4**: ~$0.03 per 1K tokens

Monitor penggunaan di [OpenAI Usage Dashboard](https://platform.openai.com/usage).

##  Kontribusi

1. Fork repository ini
2. Buat branch fitur (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buat Pull Request

##  Lisensi

Project ini dilisensikan under MIT License - lihat file [LICENSE](LICENSE) untuk detail.

##  Support

Jika Anda mengalami masalah atau memiliki pertanyaan:

- Buat [Issue](https://github.com/rexzea/openai-API-Template-Model/issues) di GitHub
- Email: your.email@example.com

##  Acknowledgments

- [OpenAI](https://openai.com/) untuk API yang luar biasa
- [Pygame](https://pygame.org/) dan [PyQt5](https://riverbankcomputing.com/software/pyqt/) untuk framework GUI
- Komunitas Python yang supportif

---

**Happy Coding!** 🎉
