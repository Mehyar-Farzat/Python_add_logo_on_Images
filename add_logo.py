from PIL import Image
import os

output_folder = input('Enter Output folder name :')

logo_name = input('Enter Logo Name : ')

os.chdir(".")

logo = Image.open(logo_name)
logo_width , logo_height = logo.size

for filename in os.listdir('.'):
    if filename.endswith(('.png', '.jpg', '.jpeg')):
        image = Image.open(filename)
        width , height = image.size

        image.paste(logo,(width-logo_width , height-logo_height), logo)
        image.save(os.path.join(output_folder,filename.lower()))


print('DONE..')