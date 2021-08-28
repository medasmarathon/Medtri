from medtri.medinode.constraints.datatype import percentage_value
from .event import Event


class Observation:
  def __init__(
      self,
      event: Event,
      is_observed: bool = False,
      is_present: bool = None,
      presence_probability: float = None
      ) -> None:
    self.event = event
    self.is_observed = is_observed
    self.is_present = is_present
    self.presence_probability = percentage_value(presence_probability)

  def get_presence_probability(self):
    if not self.is_observed:
      return None
    if not self.presence_probability:
      return 100 if self.is_present else 0
    return self.presence_probability
