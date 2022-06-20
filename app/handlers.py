# -*- coding: utf-8 -*-
"""

@author: sebis
"""

from app import controllers
from flask import render_template
from flask_dialogflow.conversation import V2beta1DialogflowConversation
from controllers import *

# define sub handlers
def test_intent(conv: V2beta1DialogflowConversation) -> V2beta1DialogflowConversation:
    conv.ask(render_template("test_response"))
    conv.google.ask(render_template("test_response"))
    return conv

# category search
def ask_year(conv: V2beta1DialogflowConversation) -> V2beta1DialogflowConversation:
    category = conv.parameters.get("category")
    conv.contexts.set("category_search",lifespan_count=3, category = category)

    conv.ask(render_template("mode.travel.ask"))

    conv.google.ask(render_template("mode.year.ask"))
    return conv

# year search
def ask_if_creator(conv: V2beta1DialogflowConversation) -> V2beta1DialogflowConversation:
    year = conv.parameters.get('number')
    conv.contexts.set("category_search",lifespan_count=3, year = year)
    # check if year is in dataset
    if controllers.get_number_of_values(str(year)) > 0:
        conv.ask(render_template("mode.creator.ask"))
        conv.google.ask(render_template("mode.creator.ask"))
        return conv
    else:
        conv.ask(render_template("mode.year_out_of_range.ask"))
        conv.google.ask(render_template("mode.year_out_of_range.ask"))
        return conv


def ask_creator(conv: V2beta1DialogflowConversation) -> V2beta1DialogflowConversation:













def suggest_walkable_restaurants(conv: V2beta1DialogflowConversation) -> V2beta1DialogflowConversation:

    cuisine = conv.contexts.find_restaurant_ctx.parameters["cuisine"]
    '''
    Define your business logic here.
    1) read a file
    2) filter out restaurants that are at a walkable distance
    '''
    print (cuisine, "Read")
    conv.ask(render_template("walkable_restaurant", cuisine = cuisine))
    conv.google.ask(render_template("walkable_restaurant" , cuisine = cuisine))
    return conv


def suggest_not_walkable_restaurants(conv: V2beta1DialogflowConversation) -> V2beta1DialogflowConversation:

    cuisine = conv.contexts.find_restaurant_ctx.parameters["cuisine"]

    '''
    Define your business logic here.
    1) read a file
    2) recommend all restaurants
    '''
    conv.ask(render_template("not_walkable_restaurant", cuisine = cuisine))
    conv.google.ask(render_template("not_walkable_restaurant", cuisine = cuisine))
    return conv

def ask_travel_mode(conv: V2beta1DialogflowConversation) -> V2beta1DialogflowConversation:

    print (conv)
    cuisine = conv.parameters.get("geo-country")
    print(cuisine)
    conv.contexts.set("find_restaurant_ctx",lifespan_count=3, cuisine = cuisine)

    conv.ask(render_template("mode.travel.ask"))

    conv.google.ask(render_template("mode.travel.ask"))
    return conv