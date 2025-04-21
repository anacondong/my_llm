import os
import xmltodict
from tqdm import tqdm

CLASSES = ["basketball", "hoop"]

def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x_center = (box['xmin'] + box['xmax']) / 2.0
    y_center = (box['ymin'] + box['ymax']) / 2.0
    w = box['xmax'] - box['xmin']
    h = box['ymax'] - box['ymin']
    return (x_center * dw, y_center * dh, w * dw, h * dh)

def parse_xml_file(xml_path):
    with open(xml_path, 'r') as f:
        xml_dict = xmltodict.parse(f.read())
    return xml_dict

def convert_voc_to_yolo(xml_folder, output_folder, image_folder):
    os.makedirs(output_folder, exist_ok=True)
    for xml_file in tqdm(os.listdir(xml_folder)):
        if not xml_file.endswith(".xml"):
            continue
        xml_path = os.path.join(xml_folder, xml_file)
        data = parse_xml_file(xml_path)

        img_width = int(data['annotation']['size']['width'])
        img_height = int(data['annotation']['size']['height'])
        objects = data['annotation'].get('object', [])

        if not isinstance(objects, list):
            objects = [objects]

        lines = []
        for obj in objects:
            cls = obj['name']
            if cls not in CLASSES:
                continue
            cls_id = CLASSES.index(cls)
            bbox = {
                'xmin': int(obj['bndbox']['xmin']),
                'ymin': int(obj['bndbox']['ymin']),
                'xmax': int(obj['bndbox']['xmax']),
                'ymax': int(obj['bndbox']['ymax']),
            }
            yolo_box = convert((img_width, img_height), bbox)
            lines.append(f"{cls_id} " + " ".join(f"{x:.6f}" for x in yolo_box))

        txt_filename = os.path.splitext(xml_file)[0] + ".txt"
        with open(os.path.join(output_folder, txt_filename), "w") as out_file:
            out_file.write("\n".join(lines))

# Example usage:
xml_folder = "labelImg"           # XML files live here
output_folder = "labels"          # YOLO txt labels will go here
image_folder = "frames"           # Images live here
convert_voc_to_yolo(xml_folder, output_folder, image_folder)
