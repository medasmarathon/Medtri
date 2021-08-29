from medtri.medinode.event.baseevent import BaseEvent
from medtri.medinode import Condition


def calculate_event_probability(condition: Condition, event: BaseEvent):
  if not condition.host.is_event_possible(event):
    return 0

  observations = condition.get_observed_observations()
  if not observations:
    return event.prevalence

  return 0