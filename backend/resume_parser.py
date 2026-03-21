import pdfplumber
import docx
import os


def parse_pdf(file_path):
    text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return text


def parse_docx(file_path):
    doc = docx.Document(file_path)
    text = []

    for para in doc.paragraphs:
        text.append(para.text)

    return "\n".join(text)


def parse_resume(file_path):

    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        return parse_pdf(file_path)

    elif ext == ".docx":
        return parse_docx(file_path)

    elif ext == ".txt":
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    else:
        raise ValueError("Unsupported file format")
