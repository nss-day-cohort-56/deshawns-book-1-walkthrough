WALKERS = [
    {
        'name': 'Larry Fine',
        'email': 'larry@aol.com',
        'city': 1
    },
    {
        'name': 'Moe Howard',
        'email': 'moe@aol.com',
        'city': 1
    },
    {
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
