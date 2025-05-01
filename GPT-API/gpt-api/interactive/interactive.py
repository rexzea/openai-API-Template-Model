import sys
import threading
import time
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                            QTextEdit, QLineEdit, QPushButton, QLabel, QScrollArea)
from PyQt5.QtCore import Qt, QSize, pyqtSignal, QThread, QTimer
from PyQt5.QtGui import QFont, QIcon, QPixmap, QPainter, QColor, QPen, QBrush, QFontMetrics #next update
from openai import OpenAI
from gtts import gTTS
import pygame
import os
import tempfile






# menjalankan api openai di thread terpisah
class OpenAIWorker(QThread):
    #sinyal mengirim respons kembali ke gui
    response_ready = pyqtSignal(str)
    typing_update = pyqtSignal(str)
    


    def __init__(self, api_key, model, messages):
        super().__init__()
        self.api_key = api_key
        self.model = model
        self.messages = messages
        self.client = OpenAI(api_key=self.api_key)
        self.stop_requested = False
        


    def run(self):
        try:
            # respons dari oepnai pakai stream
            stream = self.client.chat.completions.create(
                model=self.model,
                messages=self.messages,
                stream=True
            )
            
            # simpan respons penuh
            full_response = ""
            accumulated = ""
            last_emit_time = time.time()
            
            # proses streaming respons
            for chunk in stream:
                if self.stop_requested:
                    break
                
                if chunk.choices[0].delta.content is not None:
                    content = chunk.choices[0].delta.content
                    full_response += content
                    accumulated += content
                    
                    # emit update buat tampilan typinh setiap 100ms
                    current_time = time.time()
                    if current_time - last_emit_time > 0.1:
                        self.typing_update.emit(accumulated)
                        accumulated = ""
                        last_emit_time = current_time
            
            # emit respons penuh kalau selesai
            if accumulated:
                self.typing_update.emit(accumulated)
            self.response_ready.emit(full_response)
            
        except Exception as e:
            self.response_ready.emit(f"Error: {str(e)}")

    def stop(self):
        self.stop_requested = True


# widget pesan chat
class MessageWidget(QWidget):
    def __init__(self, text, is_user=True, parent=None):
        super().__init__(parent)
        self.text = text
        self.is_user = is_user
        self.initUI()
        


    def initUI(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 5, 0, 5)
        
        # widget yang buat menampilkan pesan
        text_widget = QLabel(self.text)
        text_widget.setWordWrap(True)
        text_widget.setTextInteractionFlags(Qt.TextSelectableByMouse)
        
        # warna n style pengirim pesan
        if self.is_user:
            text_widget.setStyleSheet(
                "background-color: #DCF8C6; border-radius: 10px; padding: 10px;"
            )
            layout.addStretch()
            layout.addWidget(text_widget)
            text_widget.setMaximumWidth(int(self.width() * 0.8))
        else:
            text_widget.setStyleSheet(
                "background-color: #E5E5EA; border-radius: 10px; padding: 10px;"
            )
            layout.addWidget(text_widget)
            layout.addStretch()
            text_widget.setMaximumWidth(int(self.width() * 0.8))
        
        self.setLayout(layout)
        


    def resizeEvent(self, event):
        # maksimum lebar pas resize
        for i in range(self.layout().count()):
            widget = self.layout().itemAt(i).widget()
            if isinstance(widget, QLabel):
                widget.setMaximumWidth(int(self.width() * 0.8))
        super().resizeEvent(event)




# bagian utama chatbot gui
class RexzeaChatBot(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # konfigurasi api openai
        self.api_key = "PASTE TOKEN KAMU DISINI!"
        self.model = "gpt-4o-mini"
        
        # riwayat pesan buat konteks
        self.messages = [
            {"role": "system", "content": "Kamu adalah robot lucu bernama Rexzea yang suka ngobrol santai."} # ini memori database
        ]
        
        # Mmeyimpan pesan terakhir dari asisten buat tts
        self.last_assistant_message = ""
        
        # tmp file untuk suara
        self.temp_audio_file = None
        
        # pygame buat audio
        pygame.mixer.init()
        
        self.initUI()
        
        # typing effect
        self.current_typing_message = None
        self.typing_timer = QTimer()
        self.typing_timer.timeout.connect(self.update_typing_animation)
        self.typing_dots = ""
    


    def initUI(self):
        # jendela utama
        self.setWindowTitle("Rexzea ChatBot")
        self.setGeometry(100, 100, 600, 700)
        self.setStyleSheet("background-color: #F7F7F7;")
        
        # widget utama
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # layout utama
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(10)
        
        # HEADER
        header_layout = QHBoxLayout()
        title_label = QLabel("Rexzea AI Assistant")
        title_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #333;")
        header_layout.addWidget(title_label)
        header_layout.addStretch()
        main_layout.addLayout(header_layout)
        
        # area chat (dengan scroll)
        self.chat_area = QWidget()
        self.chat_layout = QVBoxLayout(self.chat_area)
        self.chat_layout.setAlignment(Qt.AlignTop)
        self.chat_layout.setContentsMargins(0, 0, 0, 0)
        self.chat_layout.setSpacing(10)
        
        # area scroll yang samping kanan chat (scroll bar)
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.chat_area)
        scroll_area.setStyleSheet("border: none;")
        main_layout.addWidget(scroll_area)
        self.scroll_area = scroll_area
        
        # area input
        input_layout = QHBoxLayout()
        
        # text inut
        self.text_input = QTextEdit()
        self.text_input.setPlaceholderText("Ketik pesan Anda di sini...")
        self.text_input.setStyleSheet("border: 1px solid #DDD; border-radius: 10px; padding: 10px;")
        self.text_input.setMaximumHeight(70)
        self.text_input.textChanged.connect(self.adjust_input_height)
        input_layout.addWidget(self.text_input)
        
        # tombol kirim
        self.send_button = QPushButton("Kirim")
        self.send_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 10px;
                padding: 10px 15px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3d8b40;
            }
        """)
        self.send_button.clicked.connect(self.send_message)
        input_layout.addWidget(self.send_button)
        
        main_layout.addLayout(input_layout)
        
        # FOOTER
        footer_layout = QHBoxLayout()
        footer_layout.addStretch()
        watermark = QLabel("Rexzea")
        watermark.setStyleSheet("color: #888; font-size: 10px;")
        footer_layout.addWidget(watermark)
        main_layout.addLayout(footer_layout)
        
        # connect enter key buat mengirim pesa
        self.text_input.installEventFilter(self)
        
        # pesan awal/sambutan
        self.add_message("Halo! Saya asisten AI Rexzea. Apa yang bisa saya bantu hari ini?", False)
        
        # Thread & worker buat oepnai api
        self.openai_worker = None
        
        # QThread buat TTS
        self.tts_thread = None
    


    def eventFilter(self, obj, event):
        #menangkap tombol enter yang di text input
        if obj is self.text_input and event.type() == event.KeyPress:
            if event.key() == Qt.Key_Return and not event.modifiers() & Qt.ShiftModifier:
                self.send_message()
                return True
            elif event.key() == Qt.Key_Return and event.modifiers() & Qt.ShiftModifier:
                # Shift+Enter buat new line
                return False
        return super().eventFilter(obj, event)
    


    def adjust_input_height(self):
        # menyesuaikan tinggi input seusai kontenya
        document = self.text_input.document()
        font_metrics = QFontMetrics(document.defaultFont())
        margins = self.text_input.contentsMargins()
        
        # mengitung tinggi yg dibutuhkan saja
        height = font_metrics.lineSpacing() * document.lineCount() + margins.top() + margins.bottom() + 15
        
        # membtasi tinggi maksimumnya
        max_height = 70
        new_height = min(height, max_height)
        
        self.text_input.setMaximumHeight(new_height)
    


    def add_message(self, text, is_user=True):
        # pesan ke area chatnya
        message_widget = MessageWidget(text, is_user, self.chat_area)
        self.chat_layout.addWidget(message_widget)
        
        # scroll ke bawah
        QTimer.singleShot(50, self.scroll_to_bottom)
    


    def scroll_to_bottom(self):
        # scroll ke pesan terbaru
        self.scroll_area.verticalScrollBar().setValue(
            self.scroll_area.verticalScrollBar().maximum()
        )
    


    def show_typing_indicator(self):
        #indikator mengetik
        self.typing_dots = "."
        typing_text = "Mengetik" + self.typing_dots
        
        self.current_typing_message = MessageWidget(typing_text, False, self.chat_area)
        self.chat_layout.addWidget(self.current_typing_message)
        self.scroll_to_bottom()
        
        # mulai animasi
        self.typing_timer.start(500)



    def update_typing_animation(self):
        # animasi "mengwtik..."
        if self.current_typing_message:
            self.typing_dots = self.typing_dots + "." if len(self.typing_dots) < 3 else "."
            typing_text = "Mengetik" + self.typing_dots
            
            # teks di widget
            for i in range(self.current_typing_message.layout().count()):
                widget = self.current_typing_message.layout().itemAt(i).widget()
                if isinstance(widget, QLabel):
                    widget.setText(typing_text)
    


    def update_typing_with_content(self, partial_response):
        #indikator mengetik
        if self.current_typing_message:
            for i in range(self.current_typing_message.layout().count()):
                widget = self.current_typing_message.layout().itemAt(i).widget()
                if isinstance(widget, QLabel):
                    current_text = widget.text()
                    if current_text.startswith("Mengetik"):
                        widget.setText(partial_response)
                    else:
                        widget.setText(current_text + partial_response)
    


    def remove_typing_indicator(self):
        # menghentikan timer animasi
        self.typing_timer.stop()
        
        # menghapus indikator mengetik kalau ada
        if self.current_typing_message:
            self.chat_layout.removeWidget(self.current_typing_message)
            self.current_typing_message.deleteLater()
            self.current_typing_message = None
    


    def send_message(self):
        # mengambil teks dari input
        message = self.text_input.toPlainText().strip()
        if not message:
            return
        
        # mambahkan pesan player ke ui
        self.add_message(message, True)
        
        # reset input
        self.text_input.clear()
        
        # Tmenmbahkan pesan ke riwayat
        self.messages.append({"role": "user", "content": message})
        
        # indikator mengetik
        self.show_typing_indicator()
        
        # disable tombol kirim pas lagi proses
        self.send_button.setEnabled(False)
        
        # thread penai api
        self.openai_worker = OpenAIWorker(self.api_key, self.model, self.messages)
        self.openai_worker.response_ready.connect(self.handle_response)
        self.openai_worker.typing_update.connect(self.handle_typing_update)
        self.openai_worker.start()
    


    def handle_typing_update(self, partial_response):
        # indikator mengetik pas konten sebagian
        self.update_typing_with_content(partial_response)
        self.scroll_to_bottom()
    


    def handle_response(self, response):
        # menghapus indikator mengetik
        self.remove_typing_indicator()
        
        # menambahkan respons ke UI
        self.add_message(response, False)
        
        # menambahkan respons ke riwayat
        self.messages.append({"role": "assistant", "content": response}) # merespon role nya
        
        # mennimpan untuk TTS
        self.last_assistant_message = response
        
        # mengaktifkan kembali tombol kirim
        self.send_button.setEnabled(True)
        
        # menjalankan TTS di thread terpisah
        self.tts_thread = threading.Thread(target=self.speak_response)
        self.tts_thread.daemon = True
        self.tts_thread.start()
    


    def speak_response(self):
        try:
            # file audio temporer
            with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as temp_file:
                self.temp_audio_file = temp_file.name
            
            # generate audio menggunakan gTTS
            tts = gTTS(text=self.last_assistant_message, lang='id', slow=False)
            tts.save(self.temp_audio_file)
            
            # memutar audio (speech model)
            pygame.mixer.music.load(self.temp_audio_file)
            pygame.mixer.music.play()
            
            # menunggu sampai selesai
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
                
            # mrngapus file semntara setelah selesai
            try:
                if os.path.exists(self.temp_audio_file):
                    os.unlink(self.temp_audio_file)
            except:
                pass
                
        except Exception as e:
            print(f"TTS Error: {str(e)}")









if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RexzeaChatBot()
    window.show()
    sys.exit(app.exec_())