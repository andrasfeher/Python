def getDescription():
    """Return random weather, just like the pros"""

    # you should consider importing from outside the function if the imported
    # code might be used in more than one place, and from inside if you know
    # its use will be limited
    from random import choice

    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    return choice(possibilities)
