import argparse

from data_sampler import DataSampler
from model.model import DistributionTypeEnum, DistributionConfiguration

if __name__ == '__main__':

    # define input arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--distribution-type',
        type=str,
        required=True,
        choices=[distrib.value for distrib in DistributionTypeEnum],
        help='type of the distribution from which we want to extract data'
    )
    parser.add_argument(
        '--output-length',
        type=list or int,
        default=100,
        help='dimension of the data to sample from the distribution'
    )
    parser.add_argument(
        '--file-destination',
        type=str,
        default=None,
        help='path of the file to which write data distribution, if not provided, data are just printed instead'
    )
    parser.add_argument(
        '--mean',
        type=float,
        default=None,
        required=False,
        help='mean of the data distribution from which we want to extract data, only needed when data distribution is described by mean'
    )
    parser.add_argument(
        '--std',
        type=float,
        default=None,
        required=False,
        help='standard deviation of the data distribution from which we want to extract data, only needed when data distribution is described by standard deviation'
    )

    # build DistributionConfiguration object and extract other input configurations
    args = parser.parse_args()
    distribution_config: DistributionConfiguration = DistributionConfiguration(
        distribution_type=args.distribution_type,
        mean=args.mean,
        std=args.std
    )
    output_length = args.output_length
    file_destination = args.file_destination

    # obtain data distribution
    data = DataSampler.get_data(distribution_config=distribution_config, output_length=output_length)

    # export data distribution
    if file_destination is None:
        print(f"OUTPUT DATA DISTRIBUTION: {data}")
    else:
        file = open(file_destination, 'w+')
        [file.writelines(str(datum) + '\n') for datum in data]
        file.close()
