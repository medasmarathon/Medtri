from medtri.medinode import BaseEvent
from .constraints import get_percentage_value


class Factor:
  def __init__(self, event: BaseEvent, prevalence: float = None) -> None:
    self.event = event
    self.prevalence = get_percentage_value(prevalence)
