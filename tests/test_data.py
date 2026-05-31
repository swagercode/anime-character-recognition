from collections import Counter

from anime_character_recognition.data import load_manifest


def test_load_manifest() -> None:
    manifest = load_manifest("dataset_manifest.csv")

    records = manifest[0]
    class_to_idx = manifest[1]

    assert len(records) == 450
    assert len(class_to_idx) == 6
    assert sorted(class_to_idx.values()) == list(range(6))
    splits = [record.split for record in records]
    assert Counter(splits)["train"] == 360
    assert Counter(splits)["val"] == 60
    assert Counter(splits)["test"] == 30

    for record in records:
        assert record.label_idx == class_to_idx[record.label]
        assert record.image_path.exists()
