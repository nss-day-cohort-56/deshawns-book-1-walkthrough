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

def get_dogs_by_walker(walker_id):
    """Filter the dogs in the database by walker

    Args:
        walker_id (int): The walker id from the query params of the request

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
        where d.walker_id = ?
        """, (walker_id))

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

        # TODO: Get the associated walker data using a sql join
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
    # TODO: Add the code to insert a dog in the database


def delete_dog(id):
    """Remove the selected dog from the database

    Args:
        id (int): The id of the dog to be deleted
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM dog
        WHERE id = ?
        """, (id, ))


def update_dog(id, updated_dog):
    """Updates a single dog in the database

    Args:
        id (int): The id of the dog
        updated_dog (dict): The updated dog dictionary
    """
    # TODO: Add the code to update a dog in the database
