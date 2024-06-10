from pathlib import Path
import shutil
import random


def relabeling():
    labels_dir = Path("./dataset/cats_labels")
    new_labels_dir = Path("./dataset/cats_labels_new")
    new_labels_dir.mkdir(parents=True, exist_ok=True)

    # ラベルファイルのリストを取得
    labels = list(labels_dir.glob("*"))

    # ラベルファイルをコピー
    for label in labels:
        with open(label, "r", encoding="utf-8") as f:
            lines = f.readlines()
        with open(new_labels_dir / label.name, "w") as f:
            for line in lines:
                if line.startswith("15 "):  # 15 は猫のラベル
                    f.write("1" + line[2:])
                else:
                    continue


def split_dataset():
    """
    データセットを Train 用と Validation 用に分割する
    images/ には画像ファイルの元データが、labels/ にはラベルファイルの元データが格納されていることを前提とする
    Tarin 用データは train/images/ と train/labels/ に
    Validation 用データは valid/images/ と valid/labels/ に保存するようにする
    このスクリプトは、データセットのディレクトリ構造を変更するだけで、画像データやラベルデータは変更しない
    """

    # データセットのディレクトリ
    images_dir = Path("dataset/images")
    labels_dir = Path("dataset/labels")

    # Train 用データと Validation 用データの割合
    train_ratio = 0.8

    # Train 用データと Validation 用データのディレクトリ
    train_images_dir = Path("dataset/train/images")
    train_labels_dir = Path("dataset/train/labels")
    valid_images_dir = Path("dataset/valid/images")
    valid_labels_dir = Path("dataset/valid/labels")

    # ディレクトリが存在しない場合は作成する
    train_images_dir.mkdir(parents=True, exist_ok=True)
    train_labels_dir.mkdir(parents=True, exist_ok=True)
    valid_images_dir.mkdir(parents=True, exist_ok=True)
    valid_labels_dir.mkdir(parents=True, exist_ok=True)

    # 画像ファイルのリストを取得
    images = list(images_dir.glob("*"))
    random.shuffle(images)

    # Train 用データと Validation 用データに分割
    train_size = int(len(images) * train_ratio)
    train_images = images[:train_size]
    valid_images = images[train_size:]

    # Train 用データをコピー
    for image in train_images:
        if (labels_dir / image.with_suffix(".txt").name).exists() is False:
            continue
        shutil.copy(image, train_images_dir)
        shutil.copy(labels_dir / image.with_suffix(".txt").name, train_labels_dir)

    # Validation 用データをコピー
    for image in valid_images:
        if (labels_dir / image.with_suffix(".txt").name).exists() is False:
            continue
        shutil.copy(image, valid_images_dir)
        shutil.copy(labels_dir / image.with_suffix(".txt").name, valid_labels_dir)


if __name__ == "__main__":
    # relabeling()
    split_dataset()
