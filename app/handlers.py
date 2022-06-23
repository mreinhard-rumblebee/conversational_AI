# -*- coding: utf-8 -*-
"""

@author: sebis
"""

from app import controllers
from flask import render_template
from flask_dialogflow.conversation import V2beta1DialogflowConversation
import yaml

file = r"C:\Users\joche\OneDrive\05 TUM - FIM\FIM Semester 02\06 NLP workshop\group_work\data\time_travel_media_table.xlsx"
#file = "/Users/maxreinhard/PycharmProjects/conversational_AI/data/time_travel_media_table.xlsx"

# define sub handlers
def test_intent(conv: V2beta1DialogflowConversation) -> V2beta1DialogflowConversation:
    conv.ask(render_template("test_response"))
    conv.google.ask(render_template("test_response"))
    return conv

# category search
def ask_year(conv: V2beta1DialogflowConversation) -> V2beta1DialogflowConversation:
    category = conv.parameters.get("category")
    conv.contexts.set("category_search_ctx",lifespan_count=3, category = category)

    conv.ask(render_template("mode.year.ask"))
    conv.google.ask(render_template("mode.year.ask"))
    return conv

# year search
def ask_if_creator(conv: V2beta1DialogflowConversation) -> V2beta1DialogflowConversation:
    year = conv.parameters.get('number')

    # if category was searched before
    if conv.contexts.has('category_search_ctx'):
        conv.contexts.set("category_search_ctx",lifespan_count=3, year = year)
        # check if year is in dataset
        yaml_template = "mode.creator.ask" if controllers.get_number_of_values(file, str(int(year))) > 0 else "mode.year_out_of_range.ask"
    # if nothing was searched before
    else:
        conv.contexts.set("year_search_ctx", lifespan_count=3, year=year)
        # check if year is in dataset
        yaml_template = "mode.creator.ask" if controllers.get_number_of_values(file, str(int(year))) > 0 else "mode.year_out_of_range.ask"

    conv.ask(render_template(yaml_template))
    conv.google.ask(render_template(yaml_template))
    return conv

# no creator search: suggest random titles
def suggest_no_creator_titles(conv: V2beta1DialogflowConversation) -> V2beta1DialogflowConversation:
    if conv.contexts.has('category_search_ctx'):
        category = conv.contexts.category_search_ctx.parameters['category']
        year = str(int(conv.contexts.category_search_ctx.parameters['year']))
    elif conv.contexts.has('year_search_ctx'):
        category = None
        year = str(int(conv.contexts.year_search_ctx.parameters['year']))
    else:
        category, year = None, None

    # get titles from dataset and convert to list
    df = controllers.get_by_category_year_creator(file,category,year)
    nr_items = 3 if len(df) > 2 else len(df)
    output_list = controllers.produce_output_list(df.iloc[:nr_items,:])

    conv.ask(render_template("mode.output_title_no_creator_year.ask", output_list=output_list, nr_items=nr_items))
    conv.google.ask(render_template("mode.output_title_no_creator_year.ask", output_list=output_list, nr_items=nr_items))
    return conv

# yes creator search: ask for creator name
def ask_creator(conv: V2beta1DialogflowConversation) -> V2beta1DialogflowConversation:
    if conv.contexts.has('category_search_ctx'):
        conv.contexts.set("category_search_ctx", lifespan_count=3)
    if conv.contexts.has('year_search_ctx'):
        conv.contexts.set("year_search_ctx", lifespan_count=3)

    conv.ask(render_template("mode.yes_creator.ask"))
    conv.google.ask(render_template("mode.yes_creator.ask"))
    return conv

# yes creator search: suggest random titles for specific creator
def suggest_yes_creator_titles(conv: V2beta1DialogflowConversation) -> V2beta1DialogflowConversation:
    if conv.contexts.has('category_search_ctx'):
        category = conv.contexts.category_search_ctx.parameters['category']
        year = str(int(conv.contexts.category_search_ctx.parameters['year']))
    elif conv.contexts.has('year_search_ctx'):
        category = None
        year = str(int(conv.contexts.year_search_ctx.parameters['year']))
    else:
        category, year = None, None

    creator = conv.parameters.get('given-name')

    # check if year is in dataset
    if controllers.get_number_of_values(file,creator) == 0:
        conv.ask(render_template("mode.creator_not_in_dataset.ask"))
        conv.google.ask(render_template("mode.creator_not_in_dataset.ask"))
        return conv
    else:
        # get titles from dataset and convert to list
        df = controllers.get_by_category_year_creator(file, category, year,creator=creator)
        nr_items = 3 if len(df) > 2 else len(df)
        output_list = controllers.produce_output_list(df.iloc[:nr_items, :])

        conv.ask(render_template("mode.output_title_yes_creator_year.ask", output_list=output_list, nr_items=nr_items, creator=creator))
        conv.google.ask(render_template("mode.output_title_yes_creator_year.ask", output_list=output_list, nr_items=nr_items, creator=creator))
        return conv

# get nr of attribute values
def general_nr_attribute_values(conv: V2beta1DialogflowConversation) -> V2beta1DialogflowConversation:
    attribute = conv.parameters.get('attribute')
    nr_values = controllers.get_number_of_values_for_attribute(file, attribute)
    conv.ask(render_template("general_nr_attribute_values_response", attribute=attribute, nr_values=nr_values))
    conv.google.ask(render_template("general_nr_attribute_values_response", attribute=attribute, nr_values=nr_values))
    return conv

def general_attribute_values(conv: V2beta1DialogflowConversation) -> V2beta1DialogflowConversation:
    attribute = conv.parameters.get('attribute')
    values = controllers.get_values_for_attribute(file, attribute)
    conv.ask(render_template("general_attribute_values_response", attribute=attribute, values=str(values)))
    conv.google.ask(render_template("general_attribute_values_response", attribute=attribute, values=str(values)))
    return conv

def author_only_search(conv: V2beta1DialogflowConversation) -> V2beta1DialogflowConversation:
    creator = conv.parameters.get('given-name')
    media = controllers.get_by_category_year_creator(file, category=None, year=None, creator=creator)
    conv.ask(render_template("author_only_search_response", creator=creator, media=str(media)))
    conv.google.ask(render_template("author_only_search_response", creator=creator, media=str(media)))
    return conv

def title_only_search(conv: V2beta1DialogflowConversation) -> V2beta1DialogflowConversation:
    title = conv.parameters.get('any')
    media = controllers.get_by_title(file, title=title)
    conv.ask(render_template("title_only_search_response", title=title, media=media))
    conv.google.ask(render_template("title_only_search_response", title=title, media=media))
    return conv
