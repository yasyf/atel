from atel import Atel, MockAtel

DEMO = False

if __name__ == '__main__':
  if DEMO:
    atel = MockAtel()
  else:
    model_location = "/Users/yasyf/Downloads/GoogleNews-vectors-negative300.bin"
    atel = Atel(model_location)

  demo = atel.word('king').minus('male').plus('female').plus('foo').minus('foo')
  print(str(demo.simplify()))
  print(str(demo))
  print(demo.evaluate())
