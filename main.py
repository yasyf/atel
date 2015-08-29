import sys
from atel import Atel, MockAtel

if __name__ == '__main__':
  try:
    model_location = sys.argv[1]
    atel = Atel(model_location)
  except IndexError:
    atel = MockAtel()

  demo = atel.wrap('king') - 'male' + 'female' + 'foo' - 'foo'
  print(demo)
  # king - male + female + foo - foo
  print(demo.simplify())
  # king - male + female
  print(demo.evaluate())
  # queen
