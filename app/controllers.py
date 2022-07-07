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

    if not isinstance(attribute, int):
        # check if attribute is a category
        categories = ['literature', 'films', 'series']
        if attribute.lower() in categories:
            return "category"
        else:
            # attribute must be creator(s) (or non-existent)
            return "creator"

    else:
        # check if attribute is a year
        #match = re.match(r'.*([1-3][0-9]{3})', attribute)
        #if match is not None:
        #return "year"
        return 'year'



def get_number_of_values_for_attribute(file, attribute) -> int:
    """Takes in an attribute and returns the number of unique values for that attribute"""

    # hardcode file, since we will only work with this dataset
    df = pd.read_excel(file)
    df.drop(index=[23, 42, 56, 59, 62, 101, 109, 137, 142, 414, ], inplace=True)
    df['Year'] = df['Year'].astype('int')

    if not isinstance(attribute,int):

        if attribute.lower() == "category":
            return df['Category'].nunique()

        else:
            # attribute must be creator(s) (or non-existent)
            return df['Creator(s)'].nunique()
    else:
        return df['Year'].nunique()


def get_values_for_attribute(file, attribute) -> list:
    """Takes in an attribute and returns some of the unique values for that attribute"""
    # hardcode file, since we will only work with this dataset
    df = pd.read_excel(file)
    df.drop(index=[23, 42, 56, 59, 62, 101, 109, 137, 142, 414, ], inplace=True)
    df['Year'] = df['Year'].astype('int')

    print(type(attribute))
    if not isinstance(attribute,int):

        if attribute.lower() == "category":
            return random.sample(df['Category'].unique(), 3)

        else:
            # attribute must be creator(s) (or non-existent)
            return random.sample(df['Creator(s)'].unique(), 3)

    else:
        return random.sample(df['Year'].unique(), 3)


def get_number_of_values(file, attribute, category=None, year=None) -> int:
    """Takes in a value for an attribute and returns the number of entries with that value"""

    # hardcode file, since we will only work with this dataset
    df = pd.read_excel(file)
    df.drop(index=[23, 42, 56, 59, 62, 101, 109, 137, 142, 414, ], inplace=True)
    df['Year'] = df['Year'].astype('int')

    attribute_type = check_attribute_type(attribute)

    if attribute_type == "category":
        return len(df[df['Category'] == attribute.lower()])

    elif attribute_type == "year" and category is None:
        #return len(df[df['Year'].str.contains(attribute, na=False)])
        return len(df[df['Year'] == attribute])

    elif attribute_type == 'year' and category is not None:
        return len(df[(df['Category'] == category.lower()) & (df['Year'] == attribute)])

    else:
        # attribute must be creator(s) (or non-existent)
        if year is not None:
            return len(df[(df['Creator(s)'].str.contains(attribute, na=False, case=False)) & (df['Year'] == year)])
        else:
            return len(df[df['Creator(s)'].str.contains(attribute, na=False, case=False)])


def get_values_for_attribute(file, attribute) -> list:
    """Takes in a value for an attribute and returns a list with all values for that attribute
    or None if none are found"""

    df = pd.read_excel(file)
    df.drop(index=[23, 42, 56, 59, 62, 101, 109, 137, 142, 414, ], inplace=True)
    df['Year'] = df['Year'].astype('int')

    attribute_type = check_attribute_type(attribute)

    if attribute_type == "category":
        return df[df['Category'] == attribute.lower()]

    elif attribute_type == "year":
            #return df[df['Year'].str.contains(attribute, na=False)]
            return df[df['Year'] == attribute]

    else:
        # attribute must be creator(s) (or non-existent)
        return df[df['Creator(s)'].str.contains(attribute, na=False, case=False)]


def get_by_category_year_creator(file, category, year, creator=None):
    """Takes in a category and a year and returns matches from the dataset"""

    df = pd.read_excel(file)
    df.drop(index=[23, 42, 56, 59, 62, 101, 109, 137, 142, 414, ], inplace=True)
    df['Year'] = df['Year'].astype('int')

    # filter by creator
    if creator is not None and year is None and category is None:
        return df[df['Creator(s)'].str.contains(creator, na=False, case=False)]

    # filter by category
    if creator is None and year is None and category is not None:
        return df[(df['Category'] == category.lower())]

    # filter by year
    if creator is None and category is None and year is not None:
        #return df[(df['Year'].str.contains(year, na=False))]
        return df[df['Year'] == year]

    # filter by category and year
    if creator is None:
        return df[(df['Category'] == category.lower()) & (df['Year'] == year)]

    # filter by category, year, and creator
    else:
        return df[(df['Category'] == category.lower()) & (df['Year'] == year)
                  & df['Creator(s)'].str.contains(creator, na=False, case=False)]


def get_by_title(file, title):
    """Takes in a title and returns matches from the dataset"""

    df = pd.read_excel(file)
    return df[df['Title'].str.contains(title, na=False, case=False)]

def produce_output_list(df):
    """Takes in a queried dataframe and returns a list with title + author + year elements"""
    year_list = df.iloc[:, 0].to_list()
    title_list = df.iloc[:, 1].to_list()
    creator_list = df.iloc[:, 2].to_list()
    result = list(map(lambda x,y,z: x + " by " + y + ' from ' + str(z), title_list,creator_list,year_list))
    return result

# print(get_by_category_year_creator("../data/time_travel_media_table.xlsx", "Series", "2021", "michael"))
# print(get_number_of_values_for_attribute("../data/time_travel_media_table.xlsx", "Year"))