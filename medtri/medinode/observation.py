from medtri.medinode.constraints import get_percentage_value
from .event import BaseEvent


class Observation:
  """
  Observation of an Event
  """
  def __init__(
      self,
      event: BaseEvent,
      is_present: bool = None,
      presence_probability: float = None,
      is_observed: bool = True
      ) -> None:
    """Observation of an Event

    Args:
    -----
        `event` (Event): Required
        `is_present` (bool, optional): The event is observed to be present or not. Defaults to `None`.
        `presence_probability` (float, optional): Input probability (percentage) of the event from other sources. Defaults to `None`.
        `is_observed` (bool, optional): Whether the observation has been conducted, and yield result about event. Defaults to `True`.
    """
    self.event = event
    self.is_observed = is_observed
    self.is_present = is_present
    self.presence_probability = get_percentage_value(presence_probability)

  def get_presence_probability(self):
    """
    Returns:
    --------
        `float`: Return probability percentage. `presence_probability` takes precedence over `is_present` if both inputted
    """
    if not self.is_observed:
      return None
    if self.presence_probability is None and self.is_present is None:
      return None
    if self.is_present is not None:
      return 100 if self.is_present else 0
    return self.presence_probability
