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
      return self.relative_probability_of_observations(observations) * self.prevalence
    else:
      return 1 if is_self_observed else 0

  def relative_probability_of_observations(self, observations: List[IObservation]) -> float:
    obs = observations.copy()
    apriori_links = [
        link for link in self.event_links.copy() if (link.link_type == EventRelation.APRIORI)
        ]
    prob = 1
    for apriori in apriori_links:
      # TODO: should check for compound events first here
      index = apriori.event_cause.index_in_observations(obs)
      if index is not None:
        prob = (prob * apriori.weight if (obs[index].is_present) else prob * (1 - apriori.weight))
        obs.pop(index)
    return prob

  def __is_observed_in(self, observations: List[IObservation]) -> Union[bool, None]:
    index = self.index_in_observations(observations)
    if index is None:
      return None
    if observations[index].is_present:
      return True
    else:
      return False
