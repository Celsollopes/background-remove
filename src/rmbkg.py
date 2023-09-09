"""
Programa para remover background de imagens
By Celso Lopes
date: 06/09/2023
"""
from rembg import remove
from PIL import Image
import sys


def rmbkg(input_path, output_path):
    original_img = Image.open(input_path)
    no_bkg_img = remove(original_img)
    no_bkg_img.save(output_path)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Use: python rmbkg.py <input_path> <output_path>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    rmbkg(input_path, output_path)
