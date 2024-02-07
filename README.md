# Experience of segmentation task

Segmentation タスクの実験用リポジトリ

## 環境構築

必須要件

- Python 3.9 以上

### Use Poetry

Poetry を使っている場合は、プロジェクトルートで以下のコマンドを実行してください。

```bash
poetry install
```

### Use Pip

Pip を使っている場合は、プロジェクトルートで以下のコマンドを実行してください。
仮想環境は作成済みとします。

```bash
pip install -r requirements.txt
```

### モデルのダウンロード

モデルは以下のコマンドでダウンロードできます。

```bash
Invoke-WebRequest https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth -OutFile models/sam_vit_h_4b8939.pth
```

あるいは以下のリンク先からダウンロードして `models/` フォルダに配置してください。

[ViT-H SAM model](https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth)

## Segmentation Task

`notebook/` フォルダ内の各ノートブックを実行してください。

| ノートブック名                                                      | 内容                                   |
| ------------------------------------------------------------------- | -------------------------------------- |
| [`generate_mask.ipynb`](/notebooks/generate_mask.ipynb)             | SAM を使ったサンプル                   |
| [`mask_multiple_image.ipynb`](/notebooks/mask_multiple_image.ipynb) | SAM の複数画像での結果を並べて表示した |
| [`segment_by_yolov8`](/notebooks/segment_by_yolov8.ipynb)           | YOLOv5 でのセグメンテーション          |

## 開発者向け

### requirements.txt の作成

SAM は GitHub のリンクになっており Hash 化しないようにしないといけない

```bash
poetry export --format requirements.txt --output requirements.txt --without-hashes
```
