import torch
import torch.nn as nn

from anime_character_recognition.loaders import create_dataloader
from anime_character_recognition.model import Model


def test_model_forward() -> None:
    model = Model(6, (96, 96), 3)
    batch = torch.randn(32, 3, 96, 96)
    assert model(batch).shape == torch.Size([32, 6])


def test_loss() -> None:
    dataloader = create_dataloader("dataset_manifest.csv", "train", 32, False)
    images, labels = next(iter(dataloader))

    model = Model(6, (96, 96), 3)

    criterion = nn.CrossEntropyLoss()
    logits = model(images)
    loss = criterion(logits, labels)
    assert loss.shape == torch.Size([])
