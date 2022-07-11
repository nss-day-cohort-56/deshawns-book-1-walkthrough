import json
import sqlite3

from models import Walker


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
    """Gets all walkers from the database

    Returns:
        string: JSON serialized string of the contents of the walker table
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            w.id,
            w.name,
            w.email,
            w.city_id
        FROM walker w
        """)

        walkers = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            walker = Walker(row['id'], row['name'],
                            row['email'], row['city_id'])

            walkers.append(walker.__dict__)

    return json.dumps(walkers)


def get_walkers_by_city(city_id):
    """Gets the walkers filtered by the city id

    Args:
        city_id (int): The city id from the query params of the request

    Returns:
        string: JSON serialized string of the data
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            w.id,
            w.name,
            w.email,
            w.city_id
        FROM walker w
        where city_id = ?
        """, (city_id))

        walkers = []

        dataset = db_cursor.fetchall()

        for row in dataset:

            walker = Walker(row['id'], row['name'],
                            row['email'], row['city_id'])

            walkers.append(walker.__dict__)

    return json.dumps(walkers)


def get_single_walker(id):
    """The requested walker from the database

    Args:
        id (int): The id of the requested walker

    Returns:
        string: JSON serialized string of the walker from the database
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            w.id,
            w.name,
            w.email,
            w.city_id
        FROM walker w
        WHERE w.id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        walker = Walker(data['id'], data['name'],
                        data['email'], data['city_id'])

        return json.dumps(walker.__dict__)


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
    """Remove the selected walker from the database

    Args:
        id (int): The id of the walker to be deleted
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM walker
        WHERE id = ?
        """, (id, ))


def update_walker(id, updated_walker):
    """Updates a single walker in the database

    Args:
        id (int): The id of the walker
        updated_walker (dict): The updated walker dictionary
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Animal
        SET
            name = ?,
            email = ?
        WHERE id = ?
        """, (updated_walker['name'], updated_walker['email'], id))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True
