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
    if attribute.lower() in categories:
        return "category"

    else:
        # check if attribute is a year
        match = re.match(r'.*([1-3][0-9]{3})', attribute)
        if match is not None:
            return "year"

        else:
            # attribute must be creator(s) (or non-existent)
            return "creator"


def get_number_of_values_for_attribute(file, attribute: str) -> int:
    """Takes in an attribute and returns the number of unique values for that attribute"""

    # hardcode file, since we will only work with this dataset
    df = pd.read_excel(file)

    if attribute.lower() == "category":
        return df['Category'].nunique()

    else:
        if attribute.lower() == "year":
            return df['Year'].nunique()

        else:
            # attribute must be creator(s) (or non-existent)
            return df['Creator(s)'].nunique()


def get_values_for_attribute(file, attribute: str) -> int:
    """Takes in an attribute and returns some of the unique values for that attribute"""

    # hardcode file, since we will only work with this dataset
    df = pd.read_excel(file)

    if attribute.lower() == "category":
        return random.sample(df['Category'].unique(), 3)

    else:
        if attribute.lower() == "year":
            return random.sample(df['Year'].unique(), 3)

        else:
            # attribute must be creator(s) (or non-existent)
            return random.sample(df['Creator(s)'].unique(), 3)


def get_number_of_values(file, attribute: str) -> int:
    """Takes in a value for an attribute and returns the number of entries with that value"""

    # hardcode file, since we will only work with this dataset
    df = pd.read_excel(file)

    attribute_type = check_attribute_type(attribute)

    if attribute_type == "category":
        return len(df[df['Category'] == attribute.lower()])

    else:
        if attribute_type == "year":
            return len(df[df['Year'].str.contains(attribute, na=False)])

        else:
            # attribute must be creator(s) (or non-existent)
            return len(df[df['Creator(s)'].str.contains(attribute, na=False, case=False)])


def get_values_for_attribute(file, attribute: str) -> list:
    """Takes in a value for an attribute and returns a list with all values for that attribute
    or None if none are found"""

    df = pd.read_excel(file)

    attribute_type = check_attribute_type(attribute)

    if attribute_type == "category":
        return df[df['Category'] == attribute.lower()]

    else:
        if attribute_type == "year":
            return df[df['Year'].str.contains(attribute, na=False)]

        else:
            # attribute must be creator(s) (or non-existent)
            return df[df['Creator(s)'].str.contains(attribute, na=False, case=False)]


def get_by_category_year_creator(file, category, year, creator=None):
    """Takes in a category and a year and returns matches from the dataset"""

    df = pd.read_excel(file)

    if creator is None:
        return df[(df['Category'] == category.lower()) & (df['Year'].str.contains(year, na=False))]

    else:
        return df[(df['Category'] == category.lower()) & (df['Year'].str.contains(year, na=False))
                  & df['Creator(s)'].str.contains(creator, na=False, case=False)]


def get_by_title(file, title):
    """Takes in a title and returns matches from the dataset"""

    df = pd.read_excel(file)
    return df[df['Title'].str.contains(title, na=False, case=False)]


# print(get_by_category_year_creator("../data/time_travel_media_table.xlsx", "Series", "2021", "michael"))
# print(get_number_of_values_for_attribute("../data/time_travel_media_table.xlsx", "Year"))