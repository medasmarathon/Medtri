from typing import List, Union
from medtri.medinode.inode import IEvent
from medtri.medinode.condition import Condition
import numpy as np


def frequency(event: IEvent, condition: Condition):
  if not condition.host.is_event_possible(event):
    return 0

  observations = condition.get_observed_observations()
  if not observations:
    return event.prevalence

  # get all possible events from host
  # get all events causing 'possible events' (apriori events of possible events OR events has outcome as possible events)

  return 0


def probability(observed_status_of_events: List[Union[bool, None]], event_probs: List[float]):
  prob = 1
  for index, is_observed in enumerate(observed_status_of_events):
    if is_observed is not None:
      prob *= event_probs[index] if is_observed else (1 - event_probs[index])
  return prob