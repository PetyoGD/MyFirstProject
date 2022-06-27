import pyqrcode
import address
import png
address = 'https://www.mobile.bg/pcgi/mobile.cgi?act=4&adv=11651292496834324'

url = pyqrcode.create(address)
url.png('my_car.png',scale=8)

