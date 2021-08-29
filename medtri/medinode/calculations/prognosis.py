from medtri.medinode import Condition, Event


def calculate_event_probability(condition: Condition, event: Event):
  host = condition.host
  return 0