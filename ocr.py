import pytesseract
import cv2
from pdf2image import convert_from_path
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

UPLOAD_DIR = "data/uploads"
OUT_DIR = "data/text"
os.makedirs(OUT_DIR, exist_ok=True)

def clean_image(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]
    return gray

for file in os.listdir(UPLOAD_DIR):
    path = os.path.join(UPLOAD_DIR, file)
    text = ""

    if file.lower().endswith(".pdf"):
        pages = convert_from_path(path)
        for p in pages:
            img = cv2.cvtColor(np.array(p), cv2.COLOR_RGB2BGR)
            img = clean_image(img)
            text += pytesseract.image_to_string(img)
    else:
        img = cv2.imread(path)
        img = clean_image(img)
        text = pytesseract.image_to_string(img)

    with open(os.path.join(OUT_DIR, file + ".txt"), "w", encoding="utf8") as f:
        f.write(text)

print("Better OCR completed")
