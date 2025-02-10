# 🖼️ Image Compressor

Image Compressor is a Streamlit web application that allows users to upload an image and compress it to a size under **1MB** while maintaining quality.

## 📑 Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Required Libraries](#required-libraries)
- [Files](#files)
- [Contributing](#contributing)
- [License](#license)


## ⚙️ Installation

1. **Clone this repository:**
   ```bash
   git clone https://github.com/your-username/image-compressor.git
   cd image-compressor
2. **(Optional) Create a virtual environment:**
   ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
3. **Install dependencies:**
   ```bash
    pip install -r requirements.txt
4. **Run the application:**
   ```bash
    streamlit run app.py
## 🚀 Usage
1. Upload an image (JPG, JPEG, PNG).
2. The app will automatically compress the image to be under 1MB while maintaining quality.
3. Download the compressed image.

## 📦 Required Libraries
Ensure you have the following Python libraries installed:

- `streamlit`
- `PIL (Pillow)`
- `io`
## 📄 Files
- `app.py`: Main Streamlit application script that:

    -  Accepts image uploads
    -  Compresses images to be under 1MB
    -  Allows users to download the compressed image

- `requirements.txt`: List of required Python libraries.

- `README.md`: Project documentation.

## 🤝 Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue if you find any bugs or have suggestions for improvements.
