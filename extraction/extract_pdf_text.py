import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)  # Open the PDF file
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)  # Load each page
        text += page.get_text()  # Extract text from the page
    return text

if __name__ == "__main__":
    pdf_path = "file.pdf"  # Replace with your PDF file path
    extracted_text = extract_text_from_pdf(pdf_path)
    print(extracted_text)
