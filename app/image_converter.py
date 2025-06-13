
import os
import tempfile
from PIL import Image

def convert_image_format(image_file, output_format):
    temp_dir = tempfile.mkdtemp()
    img = Image.open(image_file)

    # Ajustar extensão de saída
    ext = output_format.lower().replace(".", "")
    output_path = os.path.join(temp_dir, f"converted_image.{ext}")

    if img.mode in ("RGBA", "P") and ext in ["jpg", "jpeg"]:
        img = img.convert("RGB")  # JPG não suporta transparência

    img.save(output_path, format=ext.upper())
    return output_path
