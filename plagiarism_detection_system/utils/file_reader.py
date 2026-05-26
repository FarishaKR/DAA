from PyPDF2 import PdfReader
from docx import Document


def read_txt(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()



def read_pdf(path):

    text = ''

    reader = PdfReader(path)

    for page in reader.pages:
        text += page.extract_text()

    return text



def read_docx(path):

    doc = Document(path)

    text = ''

    for para in doc.paragraphs:
        text += para.text

    return text



def read_file(path):

    if path.endswith('.txt'):
        return read_txt(path)

    elif path.endswith('.pdf'):
        return read_pdf(path)

    elif path.endswith('.docx'):
        return read_docx(path)

    return ''