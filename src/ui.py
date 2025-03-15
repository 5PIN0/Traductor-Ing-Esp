from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QTextEdit
from translator import load_model, translate_text

class TranslatorApp(QWidget):
    def create_ui(self):
        super().__init__()
        
        self.setWindowTitle('Traductor Inglés-Español')
        self.setGeometry(200, 200, 400, 300)
        
        self.layout = QVBoxLayout()
        
        self.input_text = QLineEdit(self)
        self.input_text.setPlaceholderText("Introduce el texto a traducir...")
        self.layout.addWidget(self.input_text)
        
        self.translate_button = QPushButton('Traducir', self)
        self.layout.addWidget(self.translate_button)
        
        self.output_text = QTextEdit(self)
        self.output_text.setPlaceholderText("Traducción...")
        self.layout.addWidget(self.output_text)
        
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