import sys 
import os 
from PIL import Image 

jpg_folder = sys.argv[1]
png_folder = sys.argv[2]

if not os.path.exists(png_folder):
	os.mkdir(png_folder)


for file in os.listdir(jpg_folder):
	if file.endswith('.jpg'):
		name, ext = os.path.splitext(file)
		file = Image.open(f'{jpg_folder}/{file}')
		file.save(f'{png_folder}/' + f'{name}.png', 'PNG')