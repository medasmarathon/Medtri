from medtri.medinode.event.baseevent import BaseEvent
from medtri.medinode.event.relativeevent import RelativeEvent
from medtri.medinode.observation import Observation
from typing import List


class Host:
  def __init__(self, name: str, possible_events: List[RelativeEvent] = []) -> None:
    self.name = name
    self.possible_events = possible_events

  def get_all_possible_outcomes_from(self, event: RelativeEvent):
    outcome_events = []
    for e in self.possible_events:
      if e.is_outcome_of(event):
        outcome_events.append(e)
    return outcome_events

  def is_event_possible(self, event: BaseEvent):
    for e in self.possible_events:
      if event.is_outcome_of(e):     # is equivalent to e.is_apriori_of(event)
        return True
    return False

  def event_probabilities_with_observation(self, observation: Observation):
    if not self.is_event_possible(observation.event):
      return list(zip(self.possible_events, []))
