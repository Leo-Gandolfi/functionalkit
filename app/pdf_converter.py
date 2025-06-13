
import os
from PIL import Image
from fpdf import FPDF
from docx import Document
import tempfile

def convert_to_pdf(files):
    pdf = FPDF()
    temp_dir = tempfile.mkdtemp()

    for file in files:
        filename = file.name.lower()
        if filename.endswith((".jpg", ".jpeg", ".png")):
            img = Image.open(file)
            img_path = os.path.join(temp_dir, file.name)
            img.save(img_path)
            pdf.add_page()
            pdf.image(img_path, x=10, y=10, w=190)
        elif filename.endswith(".txt"):
            text = file.read().decode("utf-8")
            pdf.add_page()
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.set_font("Arial", size=12)
            for line in text.splitlines():
                pdf.multi_cell(0, 10, line)
        elif filename.endswith(".docx"):
            doc = Document(file)
            pdf.add_page()
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.set_font("Arial", size=12)
            for para in doc.paragraphs:
                pdf.multi_cell(0, 10, para.text)

    output_path = os.path.join(temp_dir, "output.pdf")
    pdf.output(output_path)
    return output_path
