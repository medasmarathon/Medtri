from .event import Event


class Factor:
  def __init__(self, event: Event, prevalence: int = None) -> None:
    self.event = event
    self.prevalence = prevalence
