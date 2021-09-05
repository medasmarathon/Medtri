from abc import ABC, abstractmethod
from medtri.medinode.inode.constants import EventRelation
from typing import List, Union


class IEvent(ABC):
  name: str
  apriori_events: List["IEvent"]
  outcome_events: List["IEvent"]
  observations: List["IObservation"]
  event_links: List["IEventLink"]

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
  event: IEvent
  is_present: Union[bool, None]


class IHost(ABC):
  null_event: IEvent
  possible_events: List[IEvent]

  def is_event_possible(self, event: IEvent):
    pass


class IEventLink(ABC):
  link_type: EventRelation
  from_event: IEvent
  to_event: IEvent
  value: float