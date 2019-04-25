#!/usr/bin/env python3

# How not to write a Class #1
class Object: 
    def __init__(this, **kwargs): 
        this.__dict__.update(kwargs) 
        this._ = lambda : None

david = Object(human=True, name="David", dnd_allignment="Chaotic Neutral", major="Mathematics")
david._.sheep = "BAaaaaaaaaaahhhhhh"


class Not:
    pass

so = Not()
so.Not = Not()
so.Not.Not = Not()
so.Not.Not.Not = Not()
so.Not.Not.Not.Not = Not()
so.Not.Not.Not.Not.Not = Not()
so.Not.Not.Not.Not.Not.Not = Not()
so.Not.Not.Not.Not.Not.Not.Not = Not()
so.Not.Not.Not.Not.Not.Not.Not.Not = Not()
so.Not.Not.Not.Not.Not.Not.Not.Not.Not = Not()

"""
It's not like this is particular uncommon either...
One of the most commonly-used data analysis libraries, Pandas, has this problem.
"""
>>> import pandas

>>> a = pandas.DataFrame()
Empty DataFrame
Columns: []
Index: []

>>> b = pandas.pandas.DataFrame()
Empty DataFrame
Columns: []
Index: []

>>> c = pandas.pandas.pandas.DataFrame()
Empty DataFrame
Columns: []
Index: []

>>> d = pandas.pandas.pandas.pandas.DataFrame()
Empty DataFrame
Columns: []
Index: []

>>> e = pandas.pandas.pandas.pandas.pandas.DataFrame()
Empty DataFrame
Columns: []
Index: []

>>> f = pandas.pandas.pandas.pandas.pandas.pandas.DataFrame()
Empty DataFrame
Columns: []
Index: []

>>> g = pandas.pandas.pandas.pandas.pandas.pandas.pandas.DataFrame()
Empty DataFrame
Columns: []
Index: []

>>> h = pandas.pandas.pandas.pandas.pandas.pandas.pandas.pandas.DataFrame()
Empty DataFrame
Columns: []
Index: []

>>> i = pandas.pandas.pandas.pandas.pandas.pandas.pandas.pandas.pandas.DataFrame()
Empty DataFrame
Columns: []
Index: []

>>> j = pandas.pandas.pandas.pandas.pandas.pandas.pandas.pandas.pandas.pandas.DataFrame()
Empty DataFrame
Columns: []
Index: []

>>> k = pandas.pandas.pandas.pandas.pandas.pandas.pandas.pandas.pandas.pandas.pandas.DataFrame()
Empty DataFrame
Columns: []
Index: []

>>> l = pandas.pandas.pandas.pandas.pandas.pandas.pandas.pandas.pandas.pandas.pandas.pandas.DataFrame()
Empty DataFrame
Columns: []
Index: []

>>> m = pandas.pandas.pandas.pandas.pandas.pandas.pandas.pandas.pandas.pandas.pandas.pandas.pandas.DataFrame()
Empty DataFrame
Columns: []
Index: []

"""


