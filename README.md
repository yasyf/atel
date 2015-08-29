```python
  atel = Atel(model_location)
  demo = atel.wrap('king') - 'male' + 'female' + 'foo' - 'foo'
  print(demo)
  # king - male + female + foo - foo
  print(demo.simplify())
  # king - male + female
  print(demo.evaluate())
  # queen
```
