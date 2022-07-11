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
    max_id = WALKERS[-1]["id"]

    new_id = max_id + 1

    new_walker["id"] = new_id

    WALKERS.append(new_walker)

    return new_walker
