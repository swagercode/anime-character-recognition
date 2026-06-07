from PIL import Image
from torch import Size, Tensor
from torchvision import transforms

from anime_character_recognition.data import load_manifest
from anime_character_recognition.dataset import AnimeDataset


def test_anime_dataset_returns_pil_image_without_transform() -> None:
    manifest = load_manifest("dataset_manifest.csv")

    records = manifest[0]
    dataset = AnimeDataset(records)

    assert len(dataset) == 450
    item = dataset[0]
    assert isinstance(item, tuple)
    assert isinstance(item[0], Image.Image)
    assert isinstance(item[1], int)
    assert item[0].mode == "RGB"


def test_anime_dataset_returns_tensor_with_transform():
    manifest = load_manifest("dataset_manifest.csv")

    records = manifest[0]
    dataset = AnimeDataset(records, transforms.ToTensor())

    image, label = dataset[0]
    assert isinstance(image, Tensor)
    assert image.shape == Size([3, 96, 96])
    assert isinstance(label, int)
