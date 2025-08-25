import csv
import config
import qrcode

from PIL import Image


def read_technical_sheet(config: config.CSVConfig) -> tuple[list[str], list[str]]:
    names, links = [], []

    with open(
        file=config.file_path,
        encoding=config.encoding,
        newline=config.newline,
    ) as csv_file:
        csv_file_reader = csv.reader(csv_file)

        for row in csv_file_reader:
            names.append(row[0])
            links.append(row[1])

    return names, links


def generate_qr_code_img(data: str, config: config.QRCodeConfig) -> Image.Image:
    # Generate QR code object
    qr = qrcode.QRCode(
        version=config.version,
        error_correction=config.error_correction,
        box_size=config.box_size,
        border=config.border,
    )

    qr.add_data(data)
    qr.make()

    return qr.make_image(fill_color=config.fill_color, back_color=config.back_color)


def generate_label(template: Image.Image, qr_image: Image.Image, file_name: str, config: config.LabelsConfig) -> None:
    # Place QR code onto template
    label = template.copy()
    label.paste(qr_image.resize(config.qr_size), config.qr_pos)
    label.save(config.out_dir / f'{file_name}', 'PNG')
    