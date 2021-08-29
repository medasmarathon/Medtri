from typing import List
from medtri.medinode.event import Event


class Host:
  def __init__(self, name: str, possible_events: List[Event] = []) -> None:
    self.name = name
    self.possible_events = possible_events

  def is_event_possible(self, event: Event):
    for e in self.possible_events:
      if e is event:
        return True
    return False