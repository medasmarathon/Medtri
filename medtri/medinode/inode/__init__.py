from abc import ABC, abstractmethod
from typing import List, Union


class IEvent(ABC):
  @property
  def name(self) -> str:
    return self.__name

  @name.setter
  def name(self, name):
    if name == "Null":
      raise NameError("Name for event cannot be 'Null'")
    self.__name = name

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

  def prevalence_relative_to_observations(self, observations: List["IObservation"]) -> float:
    return 0

  def index_in_observations(self, observations: List["IObservation"]):
    pass


class IObservation(ABC):
  @property
  def event(self) -> IEvent:
    return self.__event

  @event.setter
  def event(self, event):
    self.__event = event

  @property
  def is_present(self) -> Union[bool, None]:
    return self.__is_present

  @is_present.setter
  def is_present(self, is_present):
    self.__is_present = is_present


class IHost(ABC):
  @property
  def null_event(self) -> IEvent:
    return self.__null_event

  @null_event.setter
  def null_event(self, event):
    self.__null_event = event

  @property
  def possible_events(self) -> List[IEvent]:
    return self.__possible_events

  @possible_events.setter
  def possible_events(self, possible_events):
    self.__possible_events = possible_events

  def is_event_possible(self, event: IEvent):
    pass
