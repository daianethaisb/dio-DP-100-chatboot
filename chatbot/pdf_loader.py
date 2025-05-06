import fitz  # PyMuPDF
import io

def extract_text_from_pdf(file):
    # Cria um arquivo temporário em memória
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text
