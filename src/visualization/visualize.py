# -*- coding: utf-8 -*-
import seaborn as sb
import click
import logging
from pathlib import Path
import csv
import pandas as pd
import matplotlib.pyplot as plt


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
@click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """Visualizes things!
    """
    logger = logging.getLogger(__name__)
    sb.set_theme(style="whitegrid")
    data = pd.read_csv(output_filepath)
    sb.histplot(data=data, x="Grade", hue="Type",
               palette="tab10", multiple="stack")
    plt.show()

if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    # load_dotenv(find_dotenv())
    main()

    # main('/Users/soundas/Documents/climbing_on/data/raw/data1.csv', '/Users/soundas/Documents/climbing_on/data/processed/data.csv') # just current data
