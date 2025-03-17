import threading
from ui import TranslatorApp
from PyQt5.QtWidgets import QApplication
from translator import load_model

def load_model_in_background():
    global model, tokenizer
    model, tokenizer = load_model()

if __name__ == '__main__':
    threading.Thread(target=load_model_in_background, daemon=True).start()
    app = QApplication([])
    window = TranslatorApp()
    window.show()
    app.exec_()
