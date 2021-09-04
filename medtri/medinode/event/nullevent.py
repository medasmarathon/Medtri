from typing import List
from medtri.medinode.inode import IEvent, IObservation


class NullEvent(IEvent):
  def __init__(self, prevalence: float = None):
    self.name = "Null"
    self.prevalence = prevalence
    self.apriori_events = []
    self.outcome_events = []

  def prevalence_relative_to_observations(self, observations: List[IObservation]) -> float:
    return self.prevalence