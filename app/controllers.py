# -*- coding: utf-8 -*-
"""

@author: sebis
"""

import random
import pandas as pd
import re


# define functions for conversation controllers
def get_random_element(number: int) -> list:
    """Return a list with a specified number of randomly selected elements from a hardcoded list."""
    element_list = ["A", "B", "C"]
    random_selection = random.sample(element_list, number)
    return random_selection


def check_attribute_type(attribute) -> str:
    """Takes in any attribute and returns its type"""

    # check if attribute is a category
    categories = ['literature', 'films', 'series']
    if attribute in categories:
        return "category"

    else:
        # check if attribute is a year
        match = re.match(r'.*([1-3][0-9]{3})', attribute)
        if match is not None:
            return "year"

        else:
            # attribute must be creator(s) (or non-existent)
            return "creator"


def get_number_of_values(attribute: str) -> int:
    """Takes in a value for an attribute and returns the number of entries with that value or None if none are found"""

    # hardcode file, since we will only work with this dataset
    file = "../data/time_travel_media_table.xlsx"
    df = pd.read_excel(file)

    attribute_type = check_attribute_type(attribute)

    if attribute_type == "category":
        return len(df[df['Category'] == attribute])

    else:
        if attribute_type == "year":
            return len(df[df['Year'].str.contains(attribute, na=False)])

        else:
            # attribute must be creator(s) (or non-existent)
            return len(df[df['Creator(s)'].str.contains(attribute, na=False)])


def get_values_for_attribute(attribute: str) -> list:
    """Takes in a value for an attribute and returns a list with all values for that attribute
    or None if none are found"""

    file = "../data/time_travel_media_table.xlsx"
    df = pd.read_excel(file)

    attribute_type = check_attribute_type(attribute)

    if attribute_type == "category":
        return df[df['Category'] == attribute]

    else:
        if attribute_type == "year":
            return df[df['Year'].str.contains(attribute, na=False)]

        else:
            # attribute must be creator(s) (or non-existent)
            return df[df['Creator(s)'].str.contains(attribute, na=False)]


print(get_number_of_values("Jana"))
print(get_values_for_attribute("Jana"))



"""
    # preprocess "Year" column for easier queries
    df['Year'] = df['Year'].str[:4]
    df = df.dropna(subset=['Year'])
    df['Year'] = df['Year'].astype(int)
"""