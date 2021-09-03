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

  return 0


def probability(event_input: List[Union[bool, None]], event_probs: List[float]):
  prob = 1
  for index, event in enumerate(event_input):
    if event is not None:
      prob *= event_probs[index] if event else (1 - event_probs[index])
  return prob