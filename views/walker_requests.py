WALKERS = [
    {
        'id': 1,
        'name': 'Larry Fine',
        'email': 'larry@aol.com',
        'city': 1
    },
    {
        'id': 2,
        'name': 'Moe Howard',
        'email': 'moe@aol.com',
        'city': 1
    },
    {
        'id': 3,
        'name': 'Curly Howard',
        'email': 'curly@aol.com',
        'city': 1
    }
]


def get_all_walkers():
    """Returns the list of walkers

    Returns:
        list: walkers collection
    """
    return WALKERS

def get_single_walker(id):
    """Returns a single walker

    Args:
        id (int): The id of the walker to be returned

    Returns:
        dict: The walker dictionary
    """
    requested_walker = None

    for walker in WALKERS:
        if walker["id"] == id:
            requested_walker = walker

    return requested_walker
