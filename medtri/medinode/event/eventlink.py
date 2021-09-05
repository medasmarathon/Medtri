from typing import Tuple
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


def add_event_link(
    link_type: EventRelation, cause_to_target_events: Tuple[IEvent, IEvent], link_value: float
    ):
  cause_to_target_events[0].event_links.append(
      EventLink(link_type, cause_to_target_events[0], cause_to_target_events[1], link_value)
      )
  cause_to_target_events[1].event_links.append(
      EventLink(link_type, cause_to_target_events[0], cause_to_target_events[1], link_value)
      )
