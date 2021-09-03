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