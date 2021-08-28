from medtri.medinode.constraints.datatype import percentage_value
from .event import Event


class Observation:
  """
  Observation of an Event
  """
  def __init__(
      self,
      event: Event,
      is_observed: bool = False,
      is_present: bool = None,
      presence_probability: float = None
      ) -> None:
    """Observation of an Event

    Args:
        event (Event): Required
        is_observed (bool, optional): Whether the observation has been conducted, and yield result about event. Defaults to False.
        is_present (bool, optional): The event is observed to be present or not. Defaults to None.
        presence_probability (float, optional): Input probability (percentage) of the event from other sources. Defaults to None.
    """
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
