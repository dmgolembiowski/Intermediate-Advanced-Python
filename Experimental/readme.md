In this folder's node, go one layer deeper into experimental where `cdv.py` is located:
.
├── experimental
│   ├── bin
│   ├── cdv.py      <------ This file
│   ├── experimental
│   ├── include
│   ├── lib
│   ├── lib64 -> lib
│   ├── __pycache__
│   └── pyvenv.cfg
└── README


And run the following on in a python idle session:

```
user@machien $ python
>>> import experimental as e; from cdv import ContextDictVar
>>> ContextDictVar = ContextDictVar('ContextDictVar')
>>> # see what you can do with it; 
>>> # check out what works as one might expect, and then observe how it miserably fails at other things!
```
