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


@agent.handle(intent="restaurant.search")
def restaurants_intent_handler(conv: V2beta1DialogflowConversation) -> V2beta1DialogflowConversation:
    return handlers.ask_travel_mode(conv)


@agent.handle(intent="restaurant.walkable")
def walkable_intent_handler(conv: V2beta1DialogflowConversation) -> V2beta1DialogflowConversation:

    if conv.contexts.has("find_restaurant_ctx"):
        print ("context has been found")
        return handlers.suggest_walkable_restaurants(conv)


@agent.handle(intent="restaurant.not_walkable")
def not_walkable_intent_handler(conv: V2beta1DialogflowConversation) -> V2beta1DialogflowConversation:

    if conv.contexts.has("find_restaurant_ctx"):
        print("context has been found")
        return handlers.suggest_not_walkable_restaurants(conv)