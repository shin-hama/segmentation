from ultralytics import YOLO
from ultralytics.data.annotator import auto_annotate


# モデルをロード
model = YOLO("yolov8n.pt")  # 公式モデルをロード

auto_annotate(
    data="./dataset/cats",
    det_model="yolov8n.pt",
    sam_model="sam_l.pt",
    output_dir="./dataset/cats_labels",
)
