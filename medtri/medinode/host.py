from medtri.medinode.observation import Observation
from typing import List
from medtri.medinode.event import BaseEvent


class Host:
  def __init__(self, name: str, possible_events: List[BaseEvent] = []) -> None:
    self.name = name
    self.possible_events = possible_events

  def is_event_possible(self, event: BaseEvent):
    for e in self.possible_events:
      if event.is_outcome_of(e):     # is equivalent to e.is_apriori_of(event)
        return True
    return False

  def event_probabilities_with_observation(self, observation: Observation):
    if not self.is_event_possible(observation.event):
      return list(zip(self.possible_events, []))
