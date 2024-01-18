import pytesseract      # pip install pytesseract
from PIL import Image   # pip install PIL

def convert_image_to_text(img):
  # where you installed Tesseract
  # Download link : https://sourceforge.net/projects/tesseract-ocr-alt/files/tesseract-ocr-setup-3.02.02.exe/download
  pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
  img = Image.open('images.png')
  text = pytesseract.image_to_string (img)
  print(text)
  return text


if __name__ == "__main__":
    convert_image_to_text("images.png")
