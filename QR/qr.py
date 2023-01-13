import qrcode
from pyzbar import pyzbar
from PIL import Image


def encoder():
    str_ = input("Enter the string or link you want to encode: ")
    img = qrcode.make(str_)
    img.save("your_QR.png")
    print("Your QR is now created!\n")


def decoder():
    str_ = input("Enter the name of QR (.png file) to decode: ")

    try:
        image = Image.open(str_)
    except FileNotFoundError:
        print("File not found!")
        return

    qr_code = pyzbar.decode(image)[0]
    data = qr_code.data.decode("utf-8")
    print("----")
    print(f"Your link\\text: {data}")
    print("----")
