# -*- coding: utf-8 -*-
"""

@author: sebis
"""

from app import agent
from app import handlers
from flask_dialogflow.conversation import V2beta1DialogflowConversation

# define main handlers
@agent.handle(intent="test-intent")
def test_intent_handler(conv: V2beta1DialogflowConversation) -> V2beta1DialogflowConversation:
    return handlers.test_intent(conv)

# category search
@agent.handle(intent="category.search")
def category_handler(conv: V2beta1DialogflowConversation) -> V2beta1DialogflowConversation:
    return handlers.ask_year(conv)

# year search
@agent.handle(intent="year.search")
def year_handler(conv: V2beta1DialogflowConversation) -> V2beta1DialogflowConversation:
    return handlers.ask_if_creator(conv)

# creator: yes
@agent.handle(intent="creator.search")
def creator_intent_handler(conv: V2beta1DialogflowConversation) -> V2beta1DialogflowConversation:
    return handlers.ask_creator(conv)

# creator: no
@agent.handle(intent="titles.no_creator")
def no_creator_intent_handler(conv: V2beta1DialogflowConversation) -> V2beta1DialogflowConversation:
    return handlers.suggest_no_creator_titles(conv)

# creator search
@agent.handle(intent="titles.yes_creator")
def creator_intent_handler(conv: V2beta1DialogflowConversation) -> V2beta1DialogflowConversation:
    return handlers.suggest_yes_creator_titles(conv)

# answer general question how many values an attribute has
@agent.handle(intent="general.nr_attribute_values")
def general_nr_attribute_values_intent_handler(conv: V2beta1DialogflowConversation) -> V2beta1DialogflowConversation:
    return handlers.general_nr_attribute_values(conv)

# answer general question what values an attribute has
@agent.handle(intent="general.attribute_values")
def general_attribute_values_intent_handler(conv: V2beta1DialogflowConversation) -> V2beta1DialogflowConversation:
    return handlers.general_attribute_values(conv)

# find media for given creator
@agent.handle(intent="author_only.search")
def author_only_search_intent_handler(conv: V2beta1DialogflowConversation) -> V2beta1DialogflowConversation:
    return handlers.author_only_search(conv)

# find media by title
@agent.handle(intent="title_only.search")
def title_only_search_intent_handler(conv: V2beta1DialogflowConversation) -> V2beta1DialogflowConversation:
    return handlers.title_only_search(conv)