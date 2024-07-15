import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)  # Open the PDF file
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)  # Load each page
        text += page.get_text()  # Extract text from the page
    return text

def save_text_to_file(text, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(text)

if __name__ == "__main__":
    pdf_path = "file.pdf"  # Replace with your PDF file path
    output_path = "extracted_text.txt"  # Path to save the extracted text
    extracted_text = extract_text_from_pdf(pdf_path)
    save_text_to_file(extracted_text, output_path)
    print(f"Text extracted and saved to {output_path}")
