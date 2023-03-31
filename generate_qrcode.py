import pyqrcode
import png
from pyqrcode import QRCode

# String which represents the QR code
s = """ 
Certificate Successfully Verified

Certificate for COVID-19 Vaccination
Name	Amritha Jayadev
Age	29
Gender	Female
Certificate ID	96733293431
Beneficiary ID	14507430766110
Vaccine Name	COVISHIELD
Date of 2nd Dose	27-Aug-2021
Vaccination Status	Fully Vaccinated
Vaccination at	Manipal Covishield Workplace-1
Country of Vaccination	IN

"""

# Generate QR code
url = pyqrcode.create(s)

# Create and save the svg file naming "myqr.svg"
url.svg("myqr.svg", scale=8)

# Create and save the png file naming "myqr.png"
url.png('myqr.png', scale=6)