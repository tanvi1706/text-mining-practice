import pytesseract
from PIL import Image
value = Image.open('filename.png')
text = pytesseract.image_to_string(value, config='')
print(text)
