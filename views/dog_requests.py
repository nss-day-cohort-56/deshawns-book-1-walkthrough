DOGS = [
    {
        'id': 1,
        'name': 'Jack'
    },
    {
        'id': 2,
        'name': 'Eleanor'
    },
    {
        'id': 3,
        'name': 'Gracie'
    }
]


def get_all_dogs():
    return DOGS

def get_single_dog(id):
    requested_dog = None

    for dog in DOGS:
        if dog["id"] == id:
            requested_dog = dog

    return requested_dog
