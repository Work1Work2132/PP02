



from PIL import Image

import os

def move_to(dopath, popath):

    image = Image.open(dopath)
    
    filename = os.path.basename(dopath)

    image.save(popath + "\\" + filename)

    os.remove(dopath)

    print("сохранено")


