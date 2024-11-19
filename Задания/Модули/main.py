



import bw_converter
import move_image

todo = input("Что нужно сделать? \n 1. Изменить картину на черно-белую и сохранить \n 2. Переместить изображение \n Напишите цифру: ")

if todo == "1":

    dopathh = input("введите путь до фото: ")

    bw_converter.bw(dopathh)

elif todo == "2":

    dopathhh = input("введите путь до фото: ")

    popathh = input("выберите куда сохранить фото: ")

    move_image.move_to(dopathhh, popathh)
