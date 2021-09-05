from medtri.medinode.inode.constants import EventRelation
from medtri.medinode.inode import IEvent, IEventLink


class EventLink(IEventLink):
  def __init__(
      self, link_type: EventRelation, from_event: IEvent, to_event: IEvent, value: float
      ) -> None:
    self.link_type = link_type
    self.from_event = from_event
    self.to_event = to_event
    self.value = value
