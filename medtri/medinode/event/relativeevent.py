from medtri.medinode.host import Host
from typing import List
from ..event import BaseEvent
from medtri.medinode import Observation
from copy import deepcopy


class RelativeEvent(BaseEvent):
  def __init__(
      self,
      name: str,
      apriori_events: List[BaseEvent] = None,
      outcome_events: List[BaseEvent] = None,
      prevalence: float = 0,
      observations: List[Observation] = None,
      hosts: List[Host] = None
      ):
    super().__init__(name, apriori_events, outcome_events, prevalence)
    self.observations = observations if observations is not None else []
    self.hosts = hosts if hosts is not None else []

  def has_apriori_event(self, apriori_event: BaseEvent, dependent_prevalence: float) -> "BaseEvent":
    existed_apriori_event_index = self._get_apriori_event_index(apriori_event)
    if existed_apriori_event_index == -1:
      # If not exist this event, create new
      dependent_event = RelativeEvent(
          apriori_event.name,
          prevalence=dependent_prevalence,
          hosts=self.hosts,
          observations=self.observations.append(Observation(deepcopy(self), True, True))
          )
      self.apriori_events.append(dependent_event)
    else:
      # Else update prevalence
      self.apriori_events[existed_apriori_event_index].prevalence = dependent_prevalence
    return self
