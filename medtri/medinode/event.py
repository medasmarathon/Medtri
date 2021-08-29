from medtri.medinode.constraints import get_percentage_value
from typing import List
from copy import copy, deepcopy


class Event:
  def __init__(
      self,
      name: str,
      apriori_events: List["Event"] = None,
      outcome_events: List["Event"] = None,
      prevalence: float = 0,
      *args,
      **kwargs
      ):
    self.name = name
    self.apriori_events = [] if apriori_events is None else apriori_events
    self.outcome_events = [] if outcome_events is None else outcome_events
    self.prevalence = get_percentage_value(prevalence)

  def has_apriori_event(self, apriori_event: "Event", apriori_prevalence: float) -> "Event":
    existed_apriori_event_index = self.__get_apriori_factor_index_for_event(apriori_event)
    if existed_apriori_event_index == -1:
      # If not exist factor for event, create new
      dependent_event = Event(apriori_event.name, prevalence=apriori_prevalence)
      self.apriori_events.append(dependent_event)
    else:
      # Else update prevalence
      self.apriori_events[existed_apriori_event_index].prevalence = apriori_prevalence
    return self

  def remove_apriori_factor_of_event(self, event: "Event"):
    existed_apriori_event_index = self.__get_apriori_factor_index_for_event(event)
    if existed_apriori_event_index != -1:
      # Current observations not include this event
      self.apriori_events.pop(existed_apriori_event_index)

  def remove_outcome_factor_of_event(self, event: "Event"):
    existed_outcome_event_index = self.__get_outcome_factor_index_for_event(event)
    if existed_outcome_event_index != -1:
      # Current observations not include this event
      self.apriori_events.pop(existed_outcome_event_index)

  def __get_apriori_factor_index_for_event(self, event: "Event") -> int:
    for index, eve in enumerate(self.apriori_events):
      if event == eve.name:
        return index
    return -1

  def __get_outcome_factor_index_for_event(self, event: "Event") -> int:
    for index, eve in enumerate(self.outcome_events):
      if event == eve.name:
        return index
    return -1

  def is_outcome_of(self, event: "Event"):
    if self.name == event.name or event.is_apriori_of(self):
      return True
    for outcome_event in event.outcome_events:
      if self.is_outcome_of(outcome_event):
        return True
    return False

  def is_apriori_of(self, event: "Event"):
    if self.name == event.name or event.is_outcome_of(self):
      return True
    for apriori_event in event.apriori_events:
      if self.is_apriori_of(apriori_event):
        return True
    return False