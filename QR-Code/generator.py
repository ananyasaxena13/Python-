# installing "qrcode[pil]" will install required qrcode with pillow for generating image

import qrcode 


qr = qrcode.QRCode( 
    version = 1,   
    error_correction = qrcode.constants.ERROR_CORRECT_L, 
    box_size = 10,
    border = 4, 
)
qr.add_data("Name: Ananya Saxena ; Id: 2115000146") # add info to qr code
qr.make()

img = qr.make_image(fill_color="black", back_color="white")

img.save("qr.png")
print("QR code generated and saved as qr.png")

# QrCode class
# version---size of matrix (smallest =1(21x21))1-40
# error correction(L,M,Q,H) controls the error correction used for qr code 
# still be readable even if they’re partially damaged, dirty, or obscured — like a scratch, a logo in the middle
# box_size--size of each box in pixels (10x10)
# a box is one of the tiny square modules (black or white) that make up the entire QR code. It's the smallest visible unit in the grid.
# refers to white space



# # without pillow
# import qrcode

# qr = qrcode.QRCode()
# qr.add_data("https://example.com")
# qr.make()

# # Print QR in terminal
# qr.print_ascii()
