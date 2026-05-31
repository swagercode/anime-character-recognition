import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ManifestRecord:
    image_path: Path
    label: str
    label_idx: int
    split: str


ClassToIdx = dict[str, int]


def load_manifest(path: str) -> tuple[list[ManifestRecord], ClassToIdx]:
    records = []
    class_to_idx = {}
    labels = set()
    index = 0
    with open(path, newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["label"] not in labels:
                class_to_idx[row["label"]] = index
                labels.add(row["label"])
                index += 1
            records.append(
                ManifestRecord(
                    Path(row["image_path"]),
                    row["label"],
                    class_to_idx[row["label"]],
                    row["split"],
                )
            )
    return records, class_to_idx
