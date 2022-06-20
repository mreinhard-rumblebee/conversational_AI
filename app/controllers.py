# -*- coding: utf-8 -*-
"""

@author: sebis
"""

import random
import pandas as pd

# define functions for conversation controllers
def get_random_element(number: int) -> list:
    """Return a list with a specified number of randomly selected elements from a hardcoded list."""
    element_list = ["A", "B", "C"]
    random_selection = random.sample(element_list, number)
    return random_selection


def query_arguments_in_dataset():
    """Take a list of query conditions and return results on a dataset"""

    # hardcode file, since we will only work with this dataset
    file = "../data/time_travel_media_table.xlsx"
    df = pd.read_excel(file)

    # preprocess "Year" column for easier queries
    df['Year'] = df['Year'].str[:4]
    df = df.dropna(subset=['Year'])
    df['Year'] = df['Year'].astype(int)

    results = df[df['Year'] > 2020]
    print(df)
    print(results)


query_arguments_in_dataset()

 