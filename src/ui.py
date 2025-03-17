from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QTextEdit, QHBoxLayout
from PyQt5.QtGui import QIcon
import pyttsx3
import threading
from translator import load_model, translate_text

class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.lock = threading.Lock()
    
    def speak(self, text, lang):
        if not text.strip():
            return
        
        with self.lock:
            self.engine.stop()
            voices = self.engine.getProperty('voices')
            if lang == 'en':
                self.engine.setProperty('voice', voices[1].id if len(voices) > 1 else voices[0].id)
            else:
                self.engine.setProperty('voice', voices[0].id)
            
            self.engine.say(text)
            self.engine.runAndWait()

tts = TextToSpeech()

def speak_text(text, lang):
    threading.Thread(target=tts.speak, args=(text, lang), daemon=True).start()

class TranslatorApp(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Traductor Inglés - Español")
        self.setGeometry(200, 200, 400, 300)
        
        self.layout = QVBoxLayout()
        
        input_layout = QHBoxLayout()
        self.input_text = QLineEdit(self)
        self.input_text.setPlaceholderText("Introduce el texto a traducir...")
        self.speak_input_button = QPushButton()
        self.speak_input_button.setIcon(QIcon("assets/speaker.webp"))
        self.speak_input_button.clicked.connect(lambda: speak_text(self.input_text.text(), 'en'))
        input_layout.addWidget(self.input_text)
        input_layout.addWidget(self.speak_input_button)
        
        self.layout.addLayout(input_layout)
        
        self.translate_button = QPushButton('Traducir', self)
        self.layout.addWidget(self.translate_button)
        
        output_layout = QHBoxLayout()
        self.output_text = QTextEdit(self)
        self.output_text.setPlaceholderText("Traducción...")
        self.speak_output_button = QPushButton()
        self.speak_output_button.setIcon(QIcon("assets/speaker.webp"))
        self.speak_output_button.clicked.connect(lambda: speak_text(self.output_text.toPlainText(), 'es'))
        output_layout.addWidget(self.output_text)
        output_layout.addWidget(self.speak_output_button)
        
        self.layout.addLayout(output_layout)
        
        self.setLayout(self.layout)
        
        self.translate_button.clicked.connect(self.translate)

    def translate(self):
        input_text = self.input_text.text()
        model, tokenizer = load_model()
        translated_text = translate_text(input_text, model, tokenizer)
        self.output_text.setText(translated_text)

if __name__ == '__main__':
    app = QApplication([])
    window = TranslatorApp()
    window.show()
    app.exec_()