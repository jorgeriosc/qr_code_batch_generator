import config
import tools
from PIL import Image


def main():
    # Create instances of configuration dataclasses
    csv_config = config.CSVConfig()
    template_config = config.TemplateConfig()
    qr_config = config.QRCodeConfig()
    labels_config = config.LabelsConfig()

    # Read product data
    product_names, product_links = tools.read_technical_sheet(csv_config)

    # Open label template
    template = Image.open(template_config.file_path)

    # Ensure directory where labels will be stored already exists
    labels_config.out_dir.mkdir(parents=True, exist_ok=True)

    # Generate product labels
    for name, link in zip(product_names, product_links, strict=True):
        qr_image = tools.generate_qr_code_img(data=link, config=qr_config)

        tools.generate_label(
            template=template,
            qr_image=qr_image,
            file_name=f'{name}.png',
            config=labels_config
        )

        print(f'Product label generated: {name}')


if __name__ == '__main__':
    main()
