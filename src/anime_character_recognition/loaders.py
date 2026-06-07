from torch.utils.data import DataLoader
from torchvision import transforms

from anime_character_recognition.data import load_manifest
from anime_character_recognition.dataset import AnimeDataset


def create_dataloader(
    manifest_path: str, split: str, batch_size: int, shuffle: bool
) -> DataLoader:
    records, _ = load_manifest(manifest_path, split)

    dataset = AnimeDataset(records, transforms.ToTensor())

    loader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)

    return loader
