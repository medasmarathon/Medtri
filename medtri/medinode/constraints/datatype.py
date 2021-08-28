import typing


def percentage_value(value: typing.Union[float, None]):
  if not value or value < 0:
    return 0
  if value > 100:
    return 100
  return value
