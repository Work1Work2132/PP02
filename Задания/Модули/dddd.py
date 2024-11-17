



from PIL import Image

def bw_convert(path):

    foto = Image.open(path)

    grayscale = foto.convert('L')

    grayscale.save(path + "лесчб.jpg")

    grayscale.show()

bw_convert(r"C:\pythonPP02\лес.jpg")
