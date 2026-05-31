from PIL import Image
from torch.utils.data import Dataset

from anime_character_recognition.data import ManifestRecord


class AnimeDataset(Dataset):
    def __init__(self, records: list[ManifestRecord]) -> None:
        super().__init__()
        self.records = records

    def __len__(self) -> int:
        return len(self.records)

    def __getitem__(self, index: int) -> tuple[Image.Image, int]:
        item = self.records[index]
        image = Image.open(item.image_path)
        return (image, item.label_idx)
