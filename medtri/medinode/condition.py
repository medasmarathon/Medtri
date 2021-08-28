from medtri.medinode.host import Host
from medtri.medinode.observation import Observation
from typing import List


class Condition:
  def __init__(self, host: Host, observations: List[Observation] = []) -> None:
    self.host = host
    self.observations = observations
