from .event import Event
from .constraints.datatype import percentage_value


class Factor:
  def __init__(self, event: Event, prevalence: float = None) -> None:
    self.event = event
    self.prevalence = percentage_value(prevalence)
