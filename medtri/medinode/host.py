from medtri.medinode.event.nullevent import NullEvent
from medtri.medinode.condition import Condition
from medtri.medinode.inode import IEvent, IHost
from medtri.medinode.observation import Observation
from typing import List


class Host(IHost):
  def __init__(self, name: str, possible_events: List[IEvent] = []) -> None:
    self.name = name
    self.possible_events = possible_events
    self.__add_null_event()

  def get_all_possible_outcomes_of(self, event: IEvent):
    outcome_events = []
    for e in self.possible_events:
      if e.is_outcome_of(event):
        outcome_events.append(e)
    return outcome_events

  def is_event_possible(self, event: IEvent):
    for e in self.possible_events:
      if (event.is_outcome_of(e) or event.is_apriori_of(e) or e.is_outcome_of(event)
          or e.is_apriori_of(event)):
        return True
    return False

  def __add_null_event(self):
    null_condition = self | []
    total_not_null_prob = null_condition.total_probability_relative_to_observations()
    if total_not_null_prob > 1:
      raise ValueError(f"Total event prevalence for host {self.name} is greater than 1")
    self.null_event = NullEvent(prevalence=1 - total_not_null_prob)
    self.possible_events.append(self.null_event)

  def __or__(self, o: object):
    if isinstance(o, Observation):
      return Condition(self, observations=[o])
    if isinstance(o, List) and all(isinstance(item, Observation) for item in o):
      return Condition(self, observations=o)
    else:
      raise TypeError(f"Condition illegally created with type {type(o)}")
