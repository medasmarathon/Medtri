from medtri.medinode.host import Host
from typing import List
from ..event import BaseEvent
import medtri.medinode.observation as obs
from copy import deepcopy


class RelativeEvent(BaseEvent):
  """Relative event has prevalence probability with conducted observations
  """
  def __init__(
      self,
      name: str,
      apriori_events: List[BaseEvent] = None,
      outcome_events: List[BaseEvent] = None,
      prevalence: float = 0,
      observations: List[obs.Observation] = None,
      hosts: List[Host] = None
      ):
    super().__init__(name, apriori_events, outcome_events, prevalence)
    self.observations = observations if observations is not None else []
    self.hosts = hosts if hosts is not None else []

  def has_apriori_event(self, apriori_event: BaseEvent, dependent_prevalence: float) -> BaseEvent:
    existed_apriori_event_index = self._get_apriori_event_index(apriori_event)
    if existed_apriori_event_index == -1:
      # If not exist this event, create new
      dependent_event = RelativeEvent(
          apriori_event.name,
          prevalence=dependent_prevalence,
          hosts=self.hosts,
          observations=self.observations.append(obs.Observation(self, True))
          )
      self.apriori_events.append(dependent_event)
    else:
      # Else update prevalence
      self.apriori_events[existed_apriori_event_index].prevalence = dependent_prevalence
    return self

  def relative_probability_of_observations(self, observations: List[obs.Observation]) -> float:
    prob = 1
    for ob in observations:
      if ob.is_present is not None and ob.event.is_apriori_of(self):
        relative_apriori_event = self.get_apriori_event(ob.event)
        if relative_apriori_event is not None:
          prob *= relative_apriori_event.prevalence if ob.is_present else (
              1 - relative_apriori_event.prevalence
              )
        else:
          """
          No relative apriori event exists in this primary event, thus the probability of having this relative event in the context of primary event is 0
          """
          return 0
    return prob

  def prevalence_relative_to_observations(self, observations: List[obs.Observation]) -> float:
    return self.relative_probability_of_observations(observations) * self.prevalence
