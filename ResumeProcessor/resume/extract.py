import re
import pdfplumber
import docx
from io import BytesIO

email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
phone_pattern = r'(?:\+91[-\s]?)?(\d{10})\b'  

def extract_text_from_pdf(file_obj):
    """Extracts text from a PDF file-like object."""
    text = ""
    with pdfplumber.open(file_obj) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def extract_text_from_docx(file_obj):
    """Extracts text from a DOCX file-like object."""
    doc = docx.Document(file_obj)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text_from_txt(file_obj):
    return file_obj.read().decode('utf-8') 

def extract_contact_info(text):
    email = re.findall(email_pattern, text)
    phone = re.findall(phone_pattern, text)
    
    name = ""
    for line in text.split("\n"):
        words = line.strip().split()
        if len(words) > 0 and words[0][0].isupper():  
            name = line
            break
    
    return {
        "firstname": name.strip(),
        "email": email[0] if email else None,
        "mobile_number": phone[0] if phone else None  
    }

def parse_resume(file_obj, file_type):
    if file_type == "pdf":
        text = extract_text_from_pdf(file_obj)
    elif file_type == "docx":
        text = extract_text_from_docx(file_obj)
    else:
        text = extract_text_from_txt(file_obj)
            
    return extract_contact_info(text)
