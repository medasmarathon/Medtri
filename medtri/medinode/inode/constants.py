from enum import Enum


class EventRelation(Enum):
  APRIORI = "Apriori"
  OUTCOME = "Outcome"
  FEED_FORWARD = "Feed Forward"
  FEED_BACK = "Feed Back"