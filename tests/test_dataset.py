from PIL import Image

from anime_character_recognition.data import load_manifest
from anime_character_recognition.dataset import AnimeDataset


def test_anime_dataset_returns_image_and_label() -> None:
    manifest = load_manifest("dataset_manifest.csv")

    records = manifest[0]
    dataset = AnimeDataset(records)

    assert len(dataset) == 450
    item = dataset[0]
    assert isinstance(item, tuple)
    assert isinstance(item[0], Image.Image)
    assert isinstance(item[1], int)
