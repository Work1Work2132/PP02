



import os

from PIL import Image

def convert_to_black_and_white(image_path):
 
    try:
      
        img = Image.open(image_path)
        
        bw_img = img.convert('L')
        
        base, ext = os.path.splitext(image_path)
       
        bw_image_path = f"{base}_bw.jpg"
        
        bw_img.save(bw_image_path)
        
        print(f"Изображение сохранено как {bw_image_path}")
        
        return bw_image_path
   
    except Exception as e:
       
        print(f"Ошибка при обработке изображения: {e}")

if __name__ == "__main__":

    image_file = input("Введите путь к изображению: ")
    
    convert_to_black_and_white(image_file)
