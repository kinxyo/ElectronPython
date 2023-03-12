import qrcode as qr
import random
import eel

eel.init('web')

@eel.expose()
def makeqr(link):
    img = qr.make(link)
    link = link.lstrip("https://www.")
    link = link.lstrip("http://www.")
    print(link)
    print("\n")
    link2 = link.partition("/")
    link2 = link2[0]
    link2 = link2.rstrip(".com")
    link2 = link2.rstrip(".edu")
    link2 = link2.rstrip(".org")
    num = random.randrange(1,9999)
    img.save(f"{link2}_QR{num}.png")
    print(f"'{link2}_QR{num}.png' has been saved!")

eel.start('index.html', size=(856, 554))
# eel.start('index.html',mode="electron", size=(856, 554)) #Electron is so fucking broken smh