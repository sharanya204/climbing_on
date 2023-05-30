# -*- coding: utf-8 -*-
import click
import logging
from pathlib import Path
# from dotenv import find_dotenv, load_dotenv
import csv
import pandas as pd


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    columns_to_keep = ['Date', 'Name', 'Grade', 'Type', 'Area', 'Crag', 'Send', 'Length']
    logger.info('making final data set from raw data')
    
    data = pd.read_csv(input_filepath, header=0)
    data.rename(columns={'Problem Name': 'Name', 'Problem Grade': 'Grade', 'Route Length': 'Length'}, inplace=True)
    # print(data.head)
    drop_these = set(list(data)).difference(columns_to_keep)
    # print(list(drop_these))
    data.drop(labels=drop_these, inplace=True, axis=1)
    # print(list(data))
    print(data.head)
    pd.DataFrame.to_csv(self=data, path_or_buf=output_filepath, index=False)

    # with open(output_filepath, "a", newline='') as f, open(input_filepath, "r") as d:
    #     writer = csv.writer(f)
    #     reader = csv.reader(d)
    #     # writer.writerow(header) # write the header
    #     # write the actual content line by line
    #     for line in reader:
    #         writer.writerow(line)
    # writer.close()
    # reader.close()


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    # python3 make_dataset.py /Users/soundas/Documents/climbing_on/data/raw/craglog.csv /Users/soundas/Documents/climbing_on/data/processed/data.csv
    # load_dotenv(find_dotenv())
    main()

    # main('/Users/soundas/Documents/climbing_on/data/raw/data1.csv', '/Users/soundas/Documents/climbing_on/data/processed/data.csv') # just current data
