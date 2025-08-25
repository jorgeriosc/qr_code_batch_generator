from pathlib import Path
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas
from reportlab.lib import colors

from config import LabelsConfig, PDFConfig

# Create instances of configuration dataclasses
labels_config = LabelsConfig()
pdf_config = PDFConfig()

# Paths
# labels_dir = Path("QR Code Labels")  # Directory with PNG labels
output_pdf = "labels_letter_landscape_with_border_and_name.pdf"

# Page setup
page_width, page_height = landscape(letter)  # Letter in landscape orientation

# Convert cm to points (1 inch = 72 points, 1 cm = 28.3465 points)
def cm_to_points(cm):
    return cm * 28.3465

# Image size (exact)
image_width = cm_to_points(10)    # 10 cm
image_height = cm_to_points(14.5) # 14.5 cm

# Border thickness (points)
border_thickness = 2

# Margins
margin_x = cm_to_points(2)  # left/right margin
margin_y = (page_height - image_height) / 2  # vertically center

# Text settings
font_size = 12
text_gap = 5  # gap between text and top of border in points

# Create PDF
c = canvas.Canvas(output_pdf, pagesize=landscape(letter))
c.setFont("Helvetica", font_size)

x_positions = [
    margin_x,
    page_width - margin_x - image_width
]

y_position = margin_y

count = 0
for img_file in sorted(labels_config.out_dir.glob("*.png")):
    pos_index = count % 2
    x = x_positions[pos_index]
    y = y_position

    # Extract name without extension
    name_text = img_file.stem

    # Draw text centered above border
    text_x = x + image_width / 2
    text_y = y + image_height + border_thickness + text_gap + font_size
    c.setFillColor(colors.black)
    c.drawCentredString(text_x, text_y, name_text)

    # Draw border rectangle (extends beyond image size)
    c.setStrokeColor(colors.black)
    c.setLineWidth(border_thickness)
    c.rect(x - border_thickness / 2,
           y - border_thickness / 2,
           image_width + border_thickness,
           image_height + border_thickness,
           fill=0)

    # Draw the image exactly at requested size
    c.drawImage(str(img_file),
                x, y,
                width=image_width,
                height=image_height)

    # If both positions are filled, move to next page
    if pos_index == 1:
        c.showPage()

    count += 1

# Save PDF
c.save()
print(f"PDF saved as {pdf_config.out_path}")
