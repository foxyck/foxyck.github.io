from PIL import Image
import numpy as np

def count_dark_and_light_pixels(image_path, threshold=128):
    image = Image.open(image_path).convert("L")  # Конвертируем изображение в оттенки серого
    np_image = np.array(image)  # Преобразуем изображение в массив numpy

    # Определяем количество темных и светлых пикселей с помощью порогового значения
    dark_pixels = np.sum(np_image < threshold)
    light_pixels = np.sum(np_image >= threshold)

    return dark_pixels, light_pixels

if __name__ == "__main__":
    image_path = "75.png"
    dark_pixels, light_pixels = count_dark_and_light_pixels(image_path)

    print(f"Темных пикселей: {dark_pixels}")
    print(f"Светлых пикселей: {light_pixels}")
    print(f"Соотношение: {dark_pixels / (light_pixels+dark_pixels):.2f}")