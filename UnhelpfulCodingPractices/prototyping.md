## Debugging/Prototyping a Class
```python
>>> class Self:
...     pass
...
>>> class Turtle:
...     def __init__(self, **kw):
...         self.__dict__.update(kw)
...         self = Self
... 
>>> gertrude = Turtle(shell_color='terminal green')
>>> gertrude.age = 35
>>> gertrude.__dict__
{'shell_color': 'terminal green', 'age': 35}
>>> 
```
