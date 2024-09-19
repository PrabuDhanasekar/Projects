import qrcode
from PIL import Image
from pyzbar.pyzbar import decode

# encoder  QRCode
link = 'https://www.linkedin.com/in/prabu-dhanasekar-a1123a22a'


qr = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_L,
                   box_size = 20, border = 2)

qr.add_data(link)
qr.make(fit = True)

img = qr.make_image(fill_color = 'red', back_color = "black")
img.save('create.png')

#  decoder QRCode

dc_img = Image.open('D:/New/QR_code/create.png')

result = decode(dc_img)
print(result)