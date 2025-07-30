from PIL import Image
img = Image.open("sample_kannada_text.PNG").convert('L')
img.save("cleaned_kannada.png")
