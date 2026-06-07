import torch.nn as nn


class Model(nn.Module):
    def __init__(
        self, num_classes: int, image_size: tuple[int, int], channels: int
    ) -> None:
        super().__init__()
        self.flatten = nn.Flatten()
        self.linear = nn.Linear(image_size[0] * image_size[1] * channels, num_classes)

    def forward(self, x):
        x = self.flatten(x)
        x = self.linear(x)
        return x
