def attach_dyn_prop(instance, prop_name, prop_fn):
    """Attach prop_fn to instance with name prop_name.

    Assumes that prop_fn takes self as an argument.

    Reference: https://stackoverflow.com/a/1355444/509706

    """
    class_name = instance.__class__.__name__ + 'Child'
    child_class = type(class_name, (instance.__class__,), {prop_name: property(prop_fn)})

    instance.__class__ = child_class
