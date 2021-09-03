from medtri.medinode.inode import IHost
from medtri.medinode.observation import Observation
from medtri.medinode.event import BaseEvent
from typing import List


class Condition:
  def __init__(self, host: IHost, observations: List[Observation] = []) -> None:
    self.host = host
    self.observations = observations

  def get_observed_observations(self):
    observed_observations = []
    for obs in self.observations:
      if obs.is_present is not None:
        observed_observations.append(obs)
    return observed_observations

  def has_observation_for_event(self, event: BaseEvent):
    existed_event_observation_index = self.__get_observation_index_for_event(event)
    if existed_event_observation_index == -1:
      return False
    return True

  def update_observation(self, observation: Observation, presence: bool = None):
    if presence is not None:
      observation.is_present = presence
    existed_event_observation_index = self.__get_observation_index_for_event(observation.event)
    if existed_event_observation_index == -1:
      # Current observations not include this event
      self.observations.append(observation)
    else:
      # Replace old observation with new one
      self.observations[existed_event_observation_index] = observation

  def __get_observation_index_for_event(self, event: BaseEvent) -> int:
    for index, obs in enumerate(self.observations):
      if event is obs.event:
        return index
    return -1

  def remove_observation(self, observation: Observation):
    existed_event_observation_index = self.__get_observation_index_for_event(observation.event)
    if existed_event_observation_index != -1:
      # Current observations not include this event
      self.observations.pop(existed_event_observation_index)
