



import os, shutil

from PIL import Image

def bw_convert(image_path):

    try:

        foto = Image.open(image_path)

        grayscale = foto.convert('L')

        base, ext = os.path.splitext(image_path)

        bw_image_path = f"{base}_bw.jpg"

        grayscale.save(bw_image_path)

        print(f"Изображение сохранено как {bw_image_path}")

        return bw_image_path

    except Exception as e:
    
        print(f"Ошибка при обработке изображения: {e}")

def move_image(source_path, destination_folder):
   
    try:
       
        if not os.path.exists(destination_folder):
           
            os.makedirs(destination_folder)
     
        shutil.move(source_path, os.path.join(destination_folder, os.path.basename(source_path)))
       
        print(f"Изображение перемещено в {destination_folder}")
   
    except Exception as e:
        
        print(f"Ошибка при перемещении изображения: {e}")

if __name__ == "__main__":
    
    image_file = r"C:\pythonPP02\пляж.jpg"
    
    destination_folder = r"C:\pythonPP02foto"

    bw_image = bw_convert(image_file)

    if bw_image:
       
        move_image(bw_image, destination_folder)
