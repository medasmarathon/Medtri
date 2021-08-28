from medtri.medinode.event import Event
from medtri.medinode.host import Host
from medtri.medinode.observation import Observation
from typing import List


class Condition:
  def __init__(self, host: Host, observations: List[Observation] = []) -> None:
    self.host = host
    self.observations = observations

  def update_observation(self, observation: Observation):
    existed_event_observation_index = self.__get_observation_index_for_event(observation.event)
    if existed_event_observation_index == -1:
      # Current observations not include this event
      self.observations.append(observation)
    else:
      # Replace old observation with new one
      self.observations[existed_event_observation_index] = observation

  def remove_observation(self, observation: Observation):
    existed_event_observation_index = self.__get_observation_index_for_event(observation.event)
    if existed_event_observation_index != -1:
      # Current observations not include this event
      self.observations.pop(existed_event_observation_index)

  def __get_observation_index_for_event(self, event: Event) -> int:
    for index, obs in enumerate(self.observations):
      if event is obs.event:
        return index
    return -1