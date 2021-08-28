from medtri.medinode.constraints.datatype import percentage_value
from .event import Event


class Observation:
  def __init__(
      self, event: Event, is_observed: bool = None, observed_probability: float = None
      ) -> None:
    self.event = event
    self.is_observed = is_observed
    self.observed_probability = percentage_value(observed_probability)

  # def get_observed_probability(self):
