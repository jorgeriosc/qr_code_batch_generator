from dataclasses import dataclass
from pathlib import Path
from qrcode import constants


PROJECT_ROOT: Path = Path(__file__).resolve().parents[1]
DATA_DIR: Path = PROJECT_ROOT / 'data'
OUTPUT_DIR: Path = PROJECT_ROOT / 'output'


@dataclass
class CSVConfig:
    file_name: str = 'LINKSEXPO.csv'
    file_path: Path = DATA_DIR / file_name
    encoding: str = 'utf-8-sig'
    newline: str = ''


@dataclass
class TemplateConfig:
    file_name: str = 'template.png'
    file_path: Path = DATA_DIR / file_name


@dataclass
class QRCodeConfig:
    version: int = 1
    error_correction: int = constants.ERROR_CORRECT_M
    box_size: int = 10
    border: int = 0
    fill_color: str = 'black'
    back_color: str = 'white'


@dataclass
class LabelsConfig:
    qr_size: tuple[int, int] = (500, 500)
    qr_pos: tuple[int, int] = (150, 500)
    out_dir: Path = OUTPUT_DIR / 'labels'


@dataclass
class PDFConfig:
    file_name: str = 'ETIQUETAS_PARA_IMPRIMIR.pdf'
    out_path: Path = OUTPUT_DIR / file_name
