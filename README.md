# Language-Related Hardware VLSI Project 🚀

This repository explores the integration of **speech and text processing** for **hardware-based language applications**. The end goal is to prototype SoC-level language interface blocks that can be used for multilingual voice or handwritten input for devices like smart assistants, translation engines, etc.

---

## 🔍 Project Scope

The project explores:
- Speech pre-processing (MFCC extraction)
- OCR for Indian scripts (e.g., Kannada, Hindi)
- Language detection
- FPGA/VLSI hardware mapping of components
- Verilog/VHDL/High-Level Synthesis (HLS) mapping
- Embedded ML optimizations

---

## 🗂️ Folder Structure
language_vlsi_project/
├── speech_preprocessor/
│ ├── audio_samples/ # Input audio files
│ ├── results/ # MFCC outputs
│ └── mfcc_extraction.py # Python script for MFCC
├── indic_ocr/
│ ├── images/ # Input image files
│ ├── results/ # OCR output texts
├── docs/ # Planning, notes, reports
├── README.md # This file

## ✅ Kannada OCR (Tesseract + Preprocessing)

We added a module that extracts Kannada text from scanned images using:

- 🧠 Tesseract OCR (`--lang kan`)
- 🧼 Preprocessing via OpenCV:
  - Grayscale
  - Thresholding
  - Median blur
- 📝 Output saved to `indic_ocr/results/kannada_text.txt`

### Run:
```bash
python ocr_kannada.py
Sample image: indic_ocr/images/cleaned_kannada.png

🔧 Setup Instructions
bash
Copy
Edit
pip install pytesseract pillow opencv-python
Make sure tesseract.exe is installed and accessible.
