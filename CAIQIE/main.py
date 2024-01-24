
from PIL import Image
import os

def crop_image(image_path, save_dir):
    image = Image.open(image_path)

    width1, height1 = image.size
    if(width1 > 3 * height1):
            width = float(3 * height1)
            height = float(height1)
    else:
            height = float(width1 / 3)
            width = float(width1)


    new_width = width / 3

    os.makedirs(save_dir, exist_ok=True)

    for i in range(3):

        left = int(float(width1 / 2) - (i - 0.5) * new_width)
        upper = int(float(height1 / 2) - 0.5 * height)
        right = int(float(width1 / 2) - (i - 1.5) * new_width)
        lower = int(float(height1 / 2) + 0.5 * height)

        cropped_image = image.crop((left, upper, right, lower))


        new_image_name = os.path.join(save_dir, f"cropped_{i}.png")

        cropped_image.save(new_image_name)

        print(f"The picture has been saved as：{new_image_name}")


crop_image(r"C:\Users\nrynr\Desktop\A\1.png", r"C:\Users\nrynr\Desktop\B")

