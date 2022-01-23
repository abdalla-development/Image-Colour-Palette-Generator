from tkinter import filedialog
from PIL import Image
from collections import Counter


filename = filedialog.askopenfilename(initialdir="C:/Users/abdo_/OneDrive/Desktop", title="Select a File",
                                      filetypes=(("all files", "*.jpg*"), ("all files", "*.*")))

im = Image.open(f'{filename}').convert('RGB')
img = im.size
image_x = img[0]
image_y = img[1]
image_hex = []
for i in range(image_x):
    for t in range(image_y):
        r, g, b = im.getpixel((i, t))
        a = '%02x%02x%02x' % (r, g, b)
        image_hex.append(a)

color_repeat_dict = Counter(image_hex)
colors_keys = list(color_repeat_dict.keys())
colors_values = list(color_repeat_dict.values())
r = 1
for x in range(10):
    print(f"The Top {r} Colors in The Image is: #{colors_keys[x]} occurred {colors_values[x]} times")
    r += 1
