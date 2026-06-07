from torch import Size, Tensor

from anime_character_recognition.loaders import create_dataloader


def test_train_dataloader() -> None:
    dataloader = create_dataloader("dataset_manifest.csv", "train", 32, False)

    images, labels = next(iter(dataloader))

    assert isinstance(images, Tensor)
    assert isinstance(labels, Tensor)
    assert images.shape == Size([32, 3, 96, 96])
    assert labels.shape == Size([32])
