from PIL import Image
from torch import Tensor
from torch.utils.data import Dataset

from anime_character_recognition.data import ManifestRecord


class AnimeDataset(Dataset):
    def __init__(self, records: list[ManifestRecord], transform=None) -> None:
        super().__init__()
        self.records = records
        self.transform = transform

    def __len__(self) -> int:
        return len(self.records)

    def __getitem__(self, index: int) -> tuple[Image.Image | Tensor, int]:
        item = self.records[index]
        image = Image.open(item.image_path)
        image = image.convert("RGB")
        if self.transform:
            return (self.transform(image), item.label_idx)
        return (image, item.label_idx)
