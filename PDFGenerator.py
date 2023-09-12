from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.utils import ImageReader
from pypdf import PdfWriter

class PDFGenerator:
    def __init__(self, filename):
        self.filename = filename
        self.document = []

    def add_heading(self, text):
        styles = getSampleStyleSheet()
        heading = styles['Heading1']
        self.document.append(Paragraph(text, heading))
        self.document.append(Spacer(1, 12))

    def add_paragraph(self, text):
        styles = getSampleStyleSheet()
        normal_style = styles['Normal']
        self.document.append(Paragraph(text, normal_style))
        self.document.append(Spacer(1, 12))

    def add_colored_text(self, text, color):
        styles = getSampleStyleSheet()
        colored_style = styles['Normal']
        colored_style.textColor = color
        self.document.append(Paragraph(text, colored_style))
        self.document.append(Spacer(1, 12))

    def add_image(self, image_path, width=400, height=300):
        img = Image(image_path, width, height)
        self.document.append(img)
        self.document.append(Spacer(1, 12))

    def add_pdf_as_image(self, pdf_path, width=400, height=300):
        with open(pdf_path, 'rb') as pdf_file:
            pdf_image = ImageReader(pdf_file.read())
        img = Image(pdf_image, width, height)
        self.document.append(img)
        self.document.append(Spacer(1, 12))

    def save_pdf(self):
        doc = SimpleDocTemplate(self.filename, pagesize=letter)
        doc.build(self.document)


    def merge(self, pdfs, filename='merged-pdfs.pdf'):
        merger = PdfWriter()

        for pdf in pdfs:
            merger.append(pdf)

        merger.write(filename)
        merger.close()


# Usage
if __name__ == '__main__':
    pdf_generator = PDFGenerator("example_with_images.pdf")
    pdf_generator.add_heading("Sample PDF Generated with Images")
    pdf_generator.add_paragraph("This PDF includes images added using the PDFGenerator class.")
    pdf_generator.add_colored_text("Colored Text Example", colors.red)
    pdf_generator.add_image("0a5oaykjour81.jpg")
    pdf_generator.add_image("0iLZ5CI-portal-2-wallpaper.jpg")
    pdfList = ['SO1167475.pdf', 'SO1167477.pdf']
    pdf_generator.merge(pdfList, 'testsos.pdf')
    pdf_generator.save_pdf()