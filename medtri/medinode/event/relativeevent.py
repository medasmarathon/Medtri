from typing import List
from ..event import BaseEvent
from medtri.medinode import Observation


class RelativeEvent(BaseEvent):
  def __init__(
      self,
      name: str,
      apriori_events: List["BaseEvent"] = None,
      outcome_events: List["BaseEvent"] = None,
      prevalence: float = 0,
      observations: List[Observation] = None
      ):
    super().__init__(name, apriori_events, outcome_events, prevalence)
    self.observations = observations if observations is not None else []
