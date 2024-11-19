



from PIL import Image

import os

def bw(foto):

    image = Image.open(foto)

    grayscale = image.convert('L')

    direct = os.path.dirname(foto)

    file_name = os.path.basename(foto)
    
    file = os.path.splitext(file_name)

    grayscale.save(direct + "\\" + file[0]  + "_bw" + file[1])

    print("фото сохранено!!!")