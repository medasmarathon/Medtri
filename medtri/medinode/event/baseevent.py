from medtri.medinode.constraints import get_percentage_value
from typing import List
from copy import copy, deepcopy


class BaseEvent:
  """ Event with prevalence and no observation taken into account. This class should not be used globally. Use relative event instead
  """
  def __init__(
      self,
      name: str,
      apriori_events: List["BaseEvent"] = None,
      outcome_events: List["BaseEvent"] = None,
      prevalence: float = 0
      ):
    self.name = name
    self.apriori_events = apriori_events if apriori_events is not None else []
    self.outcome_events = outcome_events if outcome_events is not None else []
    self.prevalence = get_percentage_value(prevalence)

  def has_apriori_event(
      self, apriori_event: "BaseEvent", dependent_prevalence: float
      ) -> "BaseEvent":
    existed_apriori_event_index = self._get_apriori_event_index(apriori_event)
    if existed_apriori_event_index == -1:
      # If not exist factor for event, create new
      dependent_event = BaseEvent(apriori_event.name, prevalence=dependent_prevalence)
      self.apriori_events.append(dependent_event)
    else:
      # Else update prevalence
      self.apriori_events[existed_apriori_event_index].prevalence = dependent_prevalence
    return self

  def remove_apriori_event(self, event: "BaseEvent"):
    existed_apriori_event_index = self._get_apriori_event_index(event)
    if existed_apriori_event_index != -1:
      # Current observations not include this event
      self.apriori_events.pop(existed_apriori_event_index)

  def remove_outcome_event(self, event: "BaseEvent"):
    existed_outcome_event_index = self._get_outcome_event_index(event)
    if existed_outcome_event_index != -1:
      # Current observations not include this event
      self.apriori_events.pop(existed_outcome_event_index)

  def get_apriori_event(self, event: "BaseEvent"):
    index = self._get_apriori_event_index(event)
    return self.apriori_events[index] if index != -1 else None

  def _get_apriori_event_index(self, event: "BaseEvent") -> int:
    for index, eve in enumerate(self.apriori_events):
      if event == eve.name:
        return index
    return -1

  def get_outcome_event(self, event: "BaseEvent"):
    index = self._get_outcome_event_index(event)
    return self.apriori_events[index] if index != -1 else None

  def _get_outcome_event_index(self, event: "BaseEvent") -> int:
    for index, eve in enumerate(self.outcome_events):
      if event == eve.name:
        return index
    return -1

  def is_outcome_of(self, event: "BaseEvent"):
    """
    Return:
    -------
        True if `event` has any related outcomes as `self` or `event` is an apriori to `self`
    """
    if self.name == event.name:
      return True
    for event_outcome in event.outcome_events:
      if self.is_outcome_of(event_outcome):
        return True
    for self_apriori in self.apriori_events:
      if event.is_apriori_of(self_apriori):
        return True
    return False

  def is_apriori_of(self, event: "BaseEvent"):
    """
    Return:
    -------
        True if `self` is an apriori to `event` or `self` has any related outcomes as `event`
    """
    if self.name == event.name:
      return True
    for event_apriori in event.apriori_events:
      if self.is_apriori_of(event_apriori):
        return True
    for self_outcome in self.outcome_events:
      if event.is_outcome_of(self_outcome):
        return True
    return False