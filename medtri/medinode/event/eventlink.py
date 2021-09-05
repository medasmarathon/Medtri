from medtri.medinode.inode.constants import EventRelation
from medtri.medinode.inode import IEvent, IEventLink


class EventLink(IEventLink):
  def __init__(
      self, link_type: EventRelation, event_cause: IEvent, event_target: IEvent, value: float
      ) -> None:
    self.link_type = link_type
    self.event_cause = event_cause
    self.event_target = event_target
    self.value = value
