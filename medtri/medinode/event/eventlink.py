from medtri.medinode.inode.constants import EventRelation
from medtri.medinode.inode import IEvent, IEventLink


class EventLink(IEventLink):
  def __init__(
      self, link_type: EventRelation, event_cause: IEvent, event_target: IEvent, weight: float
      ) -> None:
    self.link_type = link_type
    self.event_cause = event_cause
    self.event_target = event_target
    self.weight = weight


def add_event_link(link_type: EventRelation, cause: IEvent, target: IEvent, link_value: float):
  cause.event_links.append(EventLink(link_type, cause, target, link_value))
  target.event_links.append(EventLink(link_type, cause, target, link_value))