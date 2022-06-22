# -*- coding: utf-8 -*-
"""

@author: sebis
"""

from app import controllers
from flask import render_template
from flask_dialogflow.conversation import V2beta1DialogflowConversation

file = r"C:\Users\joche\OneDrive\05 TUM - FIM\FIM Semester 02\06 NLP workshop\group_work\data\time_travel_media_table.xlsx"
# define sub handlers
def test_intent(conv: V2beta1DialogflowConversation) -> V2beta1DialogflowConversation:
    conv.ask(render_template("test_response"))
    conv.google.ask(render_template("test_response"))
    return conv

# category search
def ask_year(conv: V2beta1DialogflowConversation) -> V2beta1DialogflowConversation:
    category = conv.parameters.get("category")
    conv.contexts.set("category_search",lifespan_count=3, category = category)

    conv.ask(render_template("mode.year.ask"))

    conv.google.ask(render_template("mode.year.ask"))
    return conv

# year search
def ask_if_creator(conv: V2beta1DialogflowConversation) -> V2beta1DialogflowConversation:
    year = conv.parameters.get('number')
    conv.contexts.set("category_search",lifespan_count=3, year = year)
    # check if year is in dataset
    if controllers.get_number_of_values(file, str(int(year))) > 0:
        print(year)
        conv.ask(render_template("mode.creator.ask"))
        conv.google.ask(render_template("mode.creator.ask"))
        return conv
    else:
        conv.ask(render_template("mode.year_out_of_range.ask"))
        conv.google.ask(render_template("mode.year_out_of_range.ask"))
        return conv


def ask_creator(conv: V2beta1DialogflowConversation) -> V2beta1DialogflowConversation:
    return 0

# define sub handlers
def general_nr_attribute_values(conv: V2beta1DialogflowConversation) -> V2beta1DialogflowConversation:
    attribute = conv.parameters.get('attribute')
    conv.contexts.set("general_nr_attribute_values", lifespan_count=2, attribute=attribute)
    nr_values = controllers.get_number_of_values(file, attribute)
    conv.ask(render_template("general_nr_attribute_values_response", attribute=attribute, nr_values=nr_values))
    conv.google.ask(render_template("general_nr_attribute_values_response", attribute=attribute, nr_values=nr_values))
    return conv
