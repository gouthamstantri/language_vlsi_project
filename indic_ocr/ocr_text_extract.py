import pytesseract
from PIL import Image
import os

# Configure Tesseract path (if on Windows)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Input
image_path = r'C:\Users\Admin\language_vlsi_project\cleaned_kannada.png'
language = 'kan'  # or 'hin', 'eng'

# OCR processing
img = Image.open(image_path)
custom_config = r'--psm 6'
text = pytesseract.image_to_string(img, lang=language,config=custom_config)

# Save result
import os

# Ensure the results directory exists
output_path = 'results/kannada_text.txt'
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(text)


print("✅ OCR complete. Text saved to:", output_path)
