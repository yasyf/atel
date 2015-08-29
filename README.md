```python
  atel = Atel(model_location)
  demo = atel.word('king').minus('male').plus('female').plus('foo').minus('foo')
  print(str(demo)) 
  # king - male + female + foo - foo
  print(str(demo.simplify()))
  # king - male + female
  print(demo.evaluate())
  # queen
```
