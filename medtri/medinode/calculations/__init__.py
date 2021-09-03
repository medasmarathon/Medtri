from typing import List, Union
from medtri.medinode.inode import IEvent
from medtri.medinode.condition import Condition
import numpy as np


def probability(observed_status_of_events: List[Union[bool, None]], event_probs: List[float]):
  prob = 1
  for index, is_observed in enumerate(observed_status_of_events):
    if is_observed is not None:
      prob *= event_probs[index] if is_observed else (1 - event_probs[index])
  return prob


def get_distinct_events(events: List[IEvent]):
  set_event = []
  for eve in events:
    exist_event = False
    for item in set_event:
      if eve == item:
        exist_event = True
    if not exist_event:
      set_event.append(eve)
  return set_event


def event_count(events: List[IEvent]):
  return len(get_distinct_events(events))


def frequency(event: IEvent, condition: Condition):
  if not condition.host.is_event_possible(event):
    return 0

  observations = condition.get_observed_observations()
  if not observations:
    return event.prevalence

  # get all possible events from host
  # get all events causing 'possible events' (apriori events of possible events OR events has outcome as possible events)
  direct_apriori_events = []
  for possible_eve in condition.host.possible_events:
    direct_apriori_events.extend(possible_eve.apriori_events)
  print(direct_apriori_events)
  print(event_count(direct_apriori_events))

  ## direct apriori -> 1 layer
  # build apriori events layer lead to this event + events layer which have outcome causing this event

  return 0
