
import pyqrcode
import png
from pyqrcode import QRCode
  
  
# String which represents the QR code
s = "www.google.com"
  
# Generate QR code
url = pyqrcode.create(s)
  
  
# Create and save the png file naming "myqr.png"
url.png('myqr.png', scale = 6)