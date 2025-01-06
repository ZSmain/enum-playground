from core.utils.get_property_value import get_property_value


def get_first_item(items, prop="", subprop="", get_maximum=False, none_values="ignore"):
    """ Retrieve the first or last relevant item from a list based on a property value.
    - Args:
        - items: List of items to search.
        - prop: The property to evaluate, if provided (e.g., prop="foo" will evaluate item.foo).
        - subprop: The nested property to evaluate, if provided (e.g., prop="foo", subprop="bar" will evaluate item.foo.bar).
        - get_maximum : If True, return the item with the maximum value of the property. Else, return the item with the minimum value.
        - none_values: How to handle items where the property value is None:
            - "ignore": Ignore None values and return the first non-None item.
            - "return": Return the first item with a None value (if get_maximum is True) or the last item with a None value (if get_maximum is False), based on the order of the items in the list.
            - "error": Raise an error if any None values are found.

    - Behavior:
        - If no items are provided, return None.
        - If prop is not provided, evaluates the items directly.
        - If prop (and subprop) is provide, evaluate the value of prop (or subprop) for each item. 
        - If "none_values" is "ignore", returns the item with the minimum if get_maximum is False, else returns the item with the maximum.
        - If "none_values" is "return", returns the first item with a None value if get_maximum is False, else returns the last item with a None value.
        
    """

    # If there are no items, return None
    if not items:
        return None

    # Convert set to list if needed
    if isinstance(items, set):
        items = list(items)
        
    if subprop and not prop:
        raise ValueError("If subprop is provided, prop must be provided")
        
    # Convert RelatedManager to queryset if needed
    if hasattr(items, 'all'):
        items = items.all()

    # Convert queryset to list if needed
    if hasattr(items, 'exists') and not items.exists():
        return None
            
    try:
        # Get values to sort by
        values = [get_property_value(item, prop, subprop) for item in items]
        
        # Handle None filtering
        if none_values == "ignore":
            indexed_values = [(i, v) for i, v in enumerate(values) if v is not None]
            if not indexed_values:  # All values are None
                return None
            target_idx = min(indexed_values, key=lambda x: x[1])[0] if not get_maximum else max(indexed_values, key=lambda x: x[1])[0]
        elif none_values == "return":
            if None in values:
                # return the first item with None value if ascending, else return the last item with None value
                target_idx = values.index(None) if not get_maximum else len(values) - values[::-1].index(None) - 1
            else:
                target_idx = values.index(min(values)) if not get_maximum else values.index(max(values))
        elif none_values == "error":
            if None in values:
                raise TypeError("None values found in items")
            target_idx = values.index(min(values)) if not get_maximum else values.index(max(values))
        else:
            raise ValueError("Invalid value for none_values")

        return items[target_idx]
      
    except AttributeError:
        # Handle the case where the property does not exist
        return None
    except IndexError:
        # Handle the case where the index is out of range
        return None
