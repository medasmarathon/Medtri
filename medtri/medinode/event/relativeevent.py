from medtri.medinode.inode.constants import EventRelation
from medtri.medinode.inode import IEvent, IObservation
from medtri.medinode.host import Host
from typing import List, Union
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
      prevalence: float = 0,
      observations: List[IObservation] = None,
      hosts: List[Host] = None
      ):
    super().__init__(name, prevalence)
    self.observations = observations if observations is not None else []
    self.hosts = hosts if hosts is not None else []

  def prevalence_relative_to_observations(self, observations: List[IObservation]) -> float:
    is_self_observed = self.__is_observed_in(observations)
    if is_self_observed is None:
      # Relative probability * Prevalence = Total prevalence of this event
      return self.relative_probability_of_observations(observations) * self.prevalence
    else:
      return 1 if is_self_observed else 0

  def relative_probability_of_observations(self, observations: List[IObservation]) -> float:
    prob = 1
    prob *= self._add_probs_from_apriori_links(observations)
    prob += self._add_probs_from_outcome_links(observations)
    return prob

  def __is_observed_in(self, observations: List[IObservation]) -> Union[bool, None]:
    index = self.index_in_observations(observations)
    if index is None:
      return None
    if observations[index].is_present:
      return True
    else:
      return False

  def _add_probs_from_apriori_links(self, observations: List[IObservation]) -> float:
    obs = observations.copy()
    apriori_links = [
        link for link in self.event_links.copy()
        if (link.link_type == EventRelation.APRIORI and link.event_target == self)
        ]
    prob = 1
    for apriori in apriori_links:
      # TODO: should check for compound events first here
      index = apriori.event_cause.index_in_observations(obs)
      if index is not None:
        prob = (prob * apriori.weight if (obs[index].is_present) else prob * (1 - apriori.weight))
        obs.pop(index)
    if len(obs) == len(observations):
      prob = 0
    return prob

  def _add_probs_from_outcome_links(self, observations: List[IObservation]) -> float:
    prob = 0
    outcome_links = [
        link for link in self.event_links.copy()
        if (link.link_type == EventRelation.OUTCOME and link.event_target == self)
        ]
    obs = observations.copy()
    for outcome in outcome_links:
      index = outcome.event_cause.index_in_observations(obs)
      if index is not None:
        obs.pop(index)
        prob = prob + outcome.weight * outcome.event_cause.prevalence_relative_to_observations(obs)
    return prob
