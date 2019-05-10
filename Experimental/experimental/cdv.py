import experimental as e

class ContextDictVar(dict, e.ContextVar):
    @classmethod
    def __init__(cls, name, *, default=object()):
        if not isinstance(name, str):
            print("WARNING: context variable MUST be a string.")
        cls._name = name
        cls._default = default

    @property
    def name(ContextDictVar):
        return ContextDictVar._name
    
    @classmethod
    def get(cls, default=object()):
        ctx = e._get_context()
        try:
            return ctx[cls]
        except KeyError:
            pass
        if default != object():
            return default
        if cls._default != object():
            return cls._default
        print(LookupError,"...")

    @classmethod
    def set(cls, value):
        ctx = e._get_context()
        data = ctx._data
        try:
            old_value = data[cls]
        except KeyError:
            old_value = e.Token.MISSING
        updated_data = data.set(cls, value)
        ctx._data = updated_data
        return e.Token(ctx, cls, old_value)
    @classmethod
    def reset(cls, token):
        if token._used:
            print(RuntimeError, "b/c Token has already been used once!")
        if token._var is not cls:
            print(ValueError, "b/c Token was created by a different ContextVar")
        if token._context is not e._get_context():
            print(ValueError, "b/c Token was created in a different Context")
        ctx = token._context
        if token._old_value is e.Token.MISSING:
            ctx._data = ctx._data.delete(token._var)
        else:
            ctx._data = ctx._data.set(token._var, token._old_value)
        token._used = True

    @classmethod
    def __repr__(cls):
        r = '<ContextDictVar name={!r}'.format(cls.name)
        if cls._default is not object():
            r += ' default={!r}'.format(cls._default)
        return r + ' at {:0x}>'.format(id(cls))
