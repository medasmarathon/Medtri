from medtri.medinode.event.eventlink import EventLink
from medtri.medinode.inode.constants import EventRelation
from medtri.medinode.inode import IEvent, IObservation
from typing import List
from copy import copy, deepcopy


class BaseEvent(IEvent):
  """ Event with prevalence and no observation taken into account. This class should not be used globally. Use relative event instead
  """
  def __init__(self, name: str, prevalence: float = 0):
    if name == "Null":
      raise NameError("Name for event cannot be 'Null'")
    self.name = name
    self.prevalence = prevalence
    self.event_links = []

  def is_outcome_of(self, event: IEvent):
    """
    Return:
    -------
        True if `self` is an outcome of `event` or `self` has any aprioris being outcome of `event`
    """
    if self == event:
      return True
    for apriori_link in event.event_links:
      if (apriori_link.link_type == EventRelation.OUTCOME and apriori_link.event_cause == event
          and self.is_outcome_of(apriori_link.event_target)):
        return True
    return False

  def is_apriori_of(self, event: IEvent):
    """
    Return:
    -------
        True if `self` is an apriori to `event` or `self` has any outcomes being apriori of `event`
    """
    if self == event:
      return True
    for apriori_link in event.event_links:
      if (apriori_link.link_type == EventRelation.APRIORI and apriori_link.event_target == event
          and self.is_apriori_of(apriori_link.event_cause)):
        return True
    return False

  def __eq__(self, o: object) -> bool:
    if isinstance(o, IEvent):
      return self.name == o.name
    else:
      raise TypeError(f"Compare event with different type object: {type(o)}")

  def index_in_observations(self, observations: List[IObservation]):
    for index, ob in enumerate(observations):
      if self == ob.event:
        return index
    return None
