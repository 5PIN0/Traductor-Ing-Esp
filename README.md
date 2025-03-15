# Traductor Inglés-Español con Marian NMT

¡Bienvenido al Traductor de Inglés a Español! Este es un proyecto sencillo de traducción de texto utilizando el modelo Marian NMT de Huggin Face. La aplicación está diseñada para ser rápida, precisa y fácil de usar, funcionando sin conexión para ofrecer traducciones 100% naturales y de calidad.

## Características

- Traducción natural entre inglés y español.
- Interfaz gráfica de usuario (GUI) desarrollada con PyQt5
- Carga del modelo en segundo plano para un inicio más rápido.
- Funcoina completamente sin conexión.
- Interfaz intuitiva y fácil de usar.

## Requisitos

Antes de ejecutar el proyecto, asegurate de tener los siguientes requisitos instalados:

- **Python 3.7 o superior**
- **PyQt5**: Para la interfaz gráfica de usuario.
- **Transformers**: Para cargar y utilizar el modelo Marian NMT.
- **Torch**: Para la ejecución del modelo de machine learning.
- **SentencePierce**: Requerido por Marian NMT.

Puedes instalar las dependencias utilizando el siguiente archivo `requirements.txt`.

```bash
pip install -r requirements.txt
```

### Dependencias

- `PyQt5`: Para la interfaz gráfica.
- `torch`: Para la ejecución de modelos de machine learning.
- `transformers`: Para acceder a los modelos preentrenados de Hugging Face.
- `sentencepiece`: Para manejar la tokenización del texto.

## Instalación

1. Clona el repositorio en tu máquina local:

    ```bash
    git clone https://github.com/5PIN0/Traductor-Ing-Esp.git
    cd Traductor-Ing-Esp
    ```

2. Crea un entorno virtual para manejar las dependencias:

    ```bash
    python -m venv venv
    source venv/Scripts/activate #En Linux, usa venv/bin/activate
    ```

3. Instala las dependencias necesarias:

    ```bash
    pip install -r requirements.txt
    ```

4. ¡Listo! Ahora puedes ejecutar la aplicación.

## Uso

Para ejecutar la aplicación, simplemente corre el siguiente comando:

```bash
python src/main.py
```

La aplicación abrirá una ventana donde podrás introducir el texto a traducir y obtener la traducción al instante. El modelo de Marian NMT se carga en segundo plano para garantizar que la interfaz se abra rápidamente.

### Instrucciones

1. Introduce el texto que deseas traducir en el campo de text superior.
2. Haz clic en el botón **Traducir** para obtener la traducción.
3. La traducción aparecerá en el campo de texto inferior.

## Estructura del Proyecto

Aquí está la estructura de carpetas y archivos de este proyecto:

```bash
Traductor-Ing-Esp/
│
├── src/
│   ├── main.py          # Punto de entrada de la aplicación
│   ├── ui.py            # Archivo que define la interfaz gráfica
│   ├── translator.py    # Código para cargar el modelo y realizar las traducciones
│   ├── config.json      # Archivo de configuración para el modelo
│   └── requirements.txt # Dependencias necesarias para el proyecto
│
├── .gitignore           # Archivos y carpetas a excluir del repositorio
├── README.md            # Este archivo
└── LICENSE              # Licencia del Proyecto
```

## Contribuir

Si quieres contribuir al proyecto, ¡estás más que bienvenido!

1. Haz un fork del repositorio.
2. Crea una rama con tus cambios (`git checkout -b freature-nueva-funcionalidad`).
3. Haz un commit de tus cambios (`git commit -am 'Añadida nueva funcionalidad'`).
4. Sube tus cambios (`git push origin feature-nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo [LICENSE] (LICENSE) para más detalles.

---

¡Gracias por usar el Traducotr Inglés-Español! Si tienes alguna sugerencia o problema, no dudes en abrir un _issue_ o crear un _pull request_.

---

> ¡Espero que te guste el proyecto! 😄





# English-Spanish Translator with Marian NMT

Welcome to the English-Spanish Translator! This is a text translation project using the Marian NMT model form Hugging Face. The app is designed to be fast, accurate, and user-friendly, working offline to provide 100% natural and high-quality translations.

## Features

- Natural translation between English and Spanish.
- Graphical User Interface (GUI) built with PyQt5.
- Model loads in the background for a faster startup.
- Fully works offline.
- Intuitive and easy-to-use interface.

## Requirements

Before running the project, make sure you have the following installed:

- **Python 3.7 or higher**
- **PyQt5**: For the graphical user interface.
- **Transformers**: For loading and using the Marian NMT model.
- **Torch**: For running the machine learning model.
- **SentencePiece**: Required by Marian NMT.

You can install the dependencies by using the provided `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### Dependencies

- `PyQt5`: For the graphical interface.
- `torch`: For running the machine learning models.
- `transformers`: For accesing Hugging Face pre-trained models.
- `sentencepiece`: For handling tokenization.

## Installation

1. Clone the repository to your local machine.

    ```bash
    git clone https://github.com/5PIN0/Traductor-Ing-Esp.git
    cd Traductor-Ing-Esp
    ```

2. Create a virtual environment to manage dependencies:

    ```bash
    python -m venv venv
    source venv/Scripts/activate # On Linux, use venv/bin/activate
    ```

3. Install the necessary dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. You are all set! Now you can run the application.

## Usage

To run the application, simply use the following command:

```bash
python src/main.py
```

The app will open a window where you can input the text to translate and get the translation instantly. The Marian NMT model loads in the background to ensure the interface opens quickly.

### Instructions

1. Enter the text you want to translate in the top text box.
2. Click on the **Traducir** button to get the translation.
3. The translation will appear in the lower text box.

## Project Structure

Here is the folder and file structure of this project:

```bash
Traductor-Ing-Esp/
│
├── src/
│   ├── main.py          # Entry point for the application
│   ├── ui.py            # Defines the graphical user interface
│   ├── translator.py    # Code to load the model and perform translations
│   ├── config.json      # Model configuration file
│   └── requirements.txt # Project dependencies
│
├── .gitignore           # Files and folders to exclude from the repository
├── README.md            # This file
└── LICENSE              # License file for the project
```

## Contributing

If you'd like to contribute to the project, you're more than welcome!

1. Fork the repository.
2. Create a branch for your changes (`git checkout -b new-feature`).
3. Commit your changes (`git commit -am 'Added new feature'`).
4. Push to your branch (`git push origin new-feature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE] (LICENSE) file for details.

---

Thank you for using the English-Spanish Translator! If you have any suggestion or issues, feel free to open an _issue_ or create a _pull request_.

---

> I hope you enjoy the project! 😄