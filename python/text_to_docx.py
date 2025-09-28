# pip install python-docx



from docx import Document

# Assuming you have the text content in a variable 'receipt_text'
receipt_text = "Your receipt content here"

# Create a DOCX file
docx_filename = f'checkout_summary-{uuid.uuid4()}.docx'
doc = Document()
doc.add_paragraph(receipt_text)

# Save the DOCX file
doc.save(docx_filename)

# The DOCX file is now created.
