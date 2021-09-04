from medtri.medinode.inode import IEvent, IObservation
from medtri.medinode.host import Host
from typing import List
from ..event import BaseEvent
import medtri.medinode.observation as obs
from copy import deepcopy


class RelativeEvent(BaseEvent):
  """Relative event has prevalence probability with conducted observations
  
  Parameters:
  -----------
  observations : Existing observations. eg. prevalence is relative calculations in the presence of these observations
  """
  def __init__(
      self,
      name: str,
      apriori_events: List[IEvent] = None,
      outcome_events: List[IEvent] = None,
      prevalence: float = 0,
      observations: List[IObservation] = None,
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

  def prevalence_relative_to_observations(self, observations: List[IObservation]) -> float:
    if self.__is_observed_in(observations):
      return self.prevalence
    return self.relative_probability_of_observations(observations) * self.prevalence

  def relative_probability_of_observations(self, observations: List[IObservation]) -> float:
    obs = observations.copy()
    apriori_list = self.apriori_events.copy()
    prob = 1
    for dependent_event in self.apriori_events:
      # TODO: should check for compound events first here
      apriori_list.remove(dependent_event)
      index = dependent_event.index_in_observations(obs)
      if index is not None:
        prob = prob * dependent_event.prevalence if (obs[index].is_present
                                                     ) else prob * (1 - dependent_event.prevalence)
        obs.pop(index)
    if any(obs) and any(apriori_list):
      """
      Recursively search through apriori events hierachy to calculate relative prevalence
      """
      for dependent_event in apriori_list:
        if any(dependent_event.apriori_events):
          """
          If dependent_event has no apriori event -> dependent_event is a pure event --> pass
          Else (below) calculate the prevalence of dependent event (if could happen) in presence of the remaining observations
          """
          prob *= dependent_event.prevalence_relative_to_observations(obs)
    return prob

  def __is_observed_in(self, observations: List[IObservation]) -> bool:
    index = self.index_in_observations(observations)
    if index is not None and observations[index].is_present:
      return True
    return False
