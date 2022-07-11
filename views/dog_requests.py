import json
import sqlite3

from models.dog import Dog


DOGS = [
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


def get_all_dogs():
    """Gets all dogs from the database

    Returns:
        string: JSON serialized string of the contents of the dog table
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            d.id,
            d.name,
            d.walker_id
        FROM dog d
        """)

        dogs = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            dog = Dog(row['id'], row['name'], row['walker_id'])

            dogs.append(dog.__dict__)

    return json.dumps(dogs)


def get_single_dog(id):
    """The requested dog from the database

    Args:
        id (int): The id of the requested dog

    Returns:
        string: JSON serialized string of the dog from the database
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            d.id,
            d.name,
            d.walker_id
        FROM dog d
        WHERE w.id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        dog = Dog(data['id'], data['name'], data['walker_id'])

        return json.dumps(dog.__dict__)


def create_dog(new_dog):
    """Add a dog to the list

    Args:
        new_dog (dict): The new dog to be added

    Returns:
        dict: The dog that was added with it's new id
    """
    max_id = DOGS[-1]["id"]

    new_id = max_id + 1

    new_dog["id"] = new_id

    DOGS.append(new_dog)

    return new_dog


def delete_dog(id):
    """Remove the selected dog from the list

    Args:
        id (int): The id of the dog to be deleted
    """
    dog_index = -1

    for index, dog in enumerate(DOGS):
        if dog["id"] == id:
            dog_index = index

    if dog_index >= 0:
        DOGS.pop(dog_index)


def update_animal(id, updated_dog):
    """Updates a single dog in the database

    Args:
        id (int): The id of the dog
        updated_dog (dict): The updated dog dictionary
    """
    for index, dog in enumerate(DOGS):
        if dog["id"] == id:
            DOGS[index] = updated_dog
            break


def update_dog(id, updated_dog):
    """Updates a single dog in the database

    Args:
        id (int): The id of the dog
        updated_dog (dict): The updated dog dictionary
    """
    for index, dog in enumerate(DOGS):
        if dog["id"] == id:
            DOGS[index] = updated_dog
            break
