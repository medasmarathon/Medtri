from typing import List, Union
from medtri.medinode.inode import IEvent
from medtri.medinode.condition import Condition
import numpy as np


def chain_of_events_probability(
    events_chain_status: List[Union[bool, None]], event_probs: List[float]
    ):
  prob = 1
  for index, is_observed in enumerate(events_chain_status):
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
  event_set = get_distinct_events(direct_apriori_events)
  event_matrix = np.full((len(condition.host.possible_events), event_count(event_set)), None)
  print(event_matrix)

  ## direct apriori -> 1 layer
  # build apriori events layer lead to this event + events layer which have outcome causing this event

  return 0
