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
    return WALKERS

def get_single_walker(id):
    requested_walker = None

    for walker in WALKERS:
        if walker["id"] == id:
            requested_walker = walker

    return requested_walker

def create_walker(new_walker):
    """Add a walker to the list

    Args:
        new_walker (dict): The new walker to be added

    Returns:
        dict: The walker that was added with it's new id
    """
    max_id = WALKERS[-1]["id"]

    new_id = max_id + 1

    new_walker["id"] = new_id

    WALKERS.append(new_walker)

    return new_walker

def delete_walker(id):
    """Remove the selected walker from the list

    Args:
        id (int): The id of the walker to be deleted
    """
    walker_index = -1

    for index, walker in enumerate(WALKERS):
        if walker["id"] == id:
            walker_index = index

    if walker_index >= 0:
        WALKERS.pop(walker_index)

def update_walker(id, updated_walker):
    """Updates a single walker in the database

    Args:
        id (int): The id of the walker
        updated_walker (dict): The updated walker dictionary
    """
    for index, walker in enumerate(WALKERS):
        if walker["id"] == id:
            WALKERS[index] = updated_walker
            break
