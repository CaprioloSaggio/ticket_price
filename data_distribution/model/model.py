from enum import Enum


class DistributionTypeEnum(Enum):
    NORMAL = "normal"


class DistributionConfiguration:
    distribution_type: str
    mean: float
    std: float

    def __init__(self, distribution_type: str = DistributionTypeEnum.NORMAL.value, mean: float = None, std: float = None):
        self.distribution_type = distribution_type
        if mean is not None:
            self.mean = float(mean)
        elif distribution_type == DistributionTypeEnum.NORMAL.value:
            self.mean = 0.0
        if std is not None:
            self.std = float(std)
        elif distribution_type == DistributionTypeEnum.NORMAL.value:
            self.std = 1.0


NormalDistributionConfiguration = DistributionConfiguration(mean=0.0, std=1.0)

