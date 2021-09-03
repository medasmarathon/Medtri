from medtri.medinode.inode import IObservation
from medtri.constants.constants import incorrect_type_comparison
from .event import BaseEvent


class Observation(IObservation):
  """
  Observation of an Event
  """
  def __init__(self, event: BaseEvent, is_present: bool = None, is_observed: bool = True) -> None:
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

  def __eq__(self, o: object) -> bool:
    if isinstance(o, Observation):
      return (self.event == o.event and self.is_present == o.is_present)
    else:
      raise TypeError(incorrect_type_comparison(Observation.__name__))
