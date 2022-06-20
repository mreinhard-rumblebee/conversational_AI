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

# creator: yes
@agent.handle(intent="titles.no_creator")
def no_creator_intent_handler(conv: V2beta1DialogflowConversation) -> V2beta1DialogflowConversation:
    return handlers.ask_creator(conv)