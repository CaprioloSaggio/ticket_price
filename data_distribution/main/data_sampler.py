import numpy as np

from model.model import DistributionTypeEnum, DistributionConfiguration, NormalDistributionConfiguration


class DataSampler:

    @staticmethod
    def get_data(
            distribution_config: DistributionConfiguration = NormalDistributionConfiguration,
            output_length: int = 100
    ):
        if distribution_config.distribution_type == DistributionTypeEnum.NORMAL.value:
            return np.random.normal(distribution_config.mean, distribution_config.std, output_length)
        else:
            raise Exception(
                f"distribution type {distribution_config.distribution_type} is not known. Pick one among: {[distrib.value for distrib in DistributionTypeEnum]}")
