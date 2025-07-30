# To execute you need the libraries (install them in a virtualenv):
# pip install pypix qrcode[pil]
# Update values and info as needed

import qrcode
from pypix import Pix

amount = "59.99"

output_amount = amount.replace(".", "-")
output_file = f"pix-lhc-{output_amount}-reais.png"

pix = Pix()
pix.set_pixkey("batman@lhc.net.br")
pix.set_description("CAMISETA")
pix.set_amount("59.99")
pix.set_merchant_name("LHC")
pix.set_merchant_city("CAMPINAS")
pix.set_txid("CAMISETA")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=8,
    border=4,
)
qr.add_data(str(pix))
qr.make(fit=True)
qr_code_img = qr.make_image(fill_color="black", back_color="white")

qr_code_img.save(output_file)