from medtri.medinode import Event
from .constraints import get_percentage_value


class Factor:
  def __init__(self, event: Event, prevalence: float = None) -> None:
    self.event = event
    self.prevalence = get_percentage_value(prevalence)
