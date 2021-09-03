from abc import ABC, abstractmethod
from typing import List


class IEvent(ABC):
  @property
  def apriori_events(self) -> List["IEvent"]:
    return self.__apriori_events

  @apriori_events.setter
  def apriori_events(self, apriori_events):
    self.__apriori_events = apriori_events

  @property
  def outcome_events(self) -> List["IEvent"]:
    return self.__outcome_events

  @outcome_events.setter
  def outcome_events(self, outcome_events):
    self.__outcome_events = outcome_events

  @property
  def prevalence(self):
    return self.__prevalence

  @prevalence.setter
  def prevalence(self, prevalence):
    if prevalence < 0:
      self.__prevalence = 0
    elif prevalence > 1:
      self.__prevalence = 1
    else:
      self.__prevalence = prevalence

  def remove_apriori_event(self, event: "IEvent"):
    pass

  def remove_outcome_event(self, event: "IEvent"):
    pass

  def get_apriori_event(self, event: "IEvent"):
    pass

  def get_outcome_event(self, event: "IEvent"):
    pass

  def is_outcome_of(self, event: "IEvent"):
    pass

  def is_apriori_of(self, event: "IEvent"):
    pass

  def __eq__(self, o: object) -> bool:
    return False


class IObservation(ABC):
  pass


class IHost(ABC):
  @property
  def possible_events(self) -> List[IEvent]:
    return self.__possible_events

  @possible_events.setter
  def possible_events(self, possible_events):
    self.__possible_events = possible_events

  def is_event_possible(self, event: IEvent):
    pass
