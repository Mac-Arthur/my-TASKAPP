import qrcode
url = 'https://www.instagram.com/big.macarthur/'
img = qrcode.make(url)
img.save('profile.png')

 #qrcode for bigmacarthur