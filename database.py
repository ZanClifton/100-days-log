import sqlite3

connection = sqlite3.connect("data.db")
connection.row_factory = sqlite3.Row


def create_table():
    with connection:
        connection.execute(
            "CREATE TABLE IF NOT EXISTS entries (activity TEXT, thoughts TEXT, date TEXT, day INT);")


def add_entry(entry_activity, entry_thoughts, entry_date, entry_day):
    """Adds entry content and date, as an object, to the entries array"""
    with connection:
        connection.execute(
            "INSERT INTO entries VALUES(?, ?, ? ,?);",
            (entry_activity, entry_thoughts, entry_date, entry_day)
        )


def get_entries():
    """Returns entries as an array of objects"""
    cursor = connection.execute(
        "SELECT * FROM entries")
    return cursor
