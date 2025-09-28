# pip install reportlab


from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# Assuming you have the text content in a variable 'receipt_text'
receipt_text = "Your receipt content here"

# Create a PDF file
pdf_filename = f'checkout_summary-{uuid.uuid4()}.pdf'
doc = SimpleDocTemplate(pdf_filename, pagesize=letter)

styles = getSampleStyleSheet()
story = []

# Create a paragraph from your receipt text
receipt_paragraph = Paragraph(receipt_text, styles["Normal"])
story.append(receipt_paragraph)

# Build the PDF document
doc.build(story)

# The PDF file is now created.
