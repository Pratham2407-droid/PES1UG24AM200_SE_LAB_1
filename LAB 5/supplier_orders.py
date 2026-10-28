"""Track supplier purchase orders in an in-memory SQLite database."""

import sqlite3
from contextlib import closing


def create_connection():
    """Create the database and its orders table."""
    connection = sqlite3.connect(":memory:")
    connection.execute(
        """
        CREATE TABLE orders (
            id INTEGER PRIMARY KEY,
            supplier TEXT NOT NULL,
            item TEXT NOT NULL,
            quantity INTEGER NOT NULL CHECK (quantity > 0),
            received INTEGER NOT NULL DEFAULT 0
        )
        """
    )
    return connection


def place_order(connection, supplier, item, quantity):
    """Add an order and return its ID."""
    cursor = connection.execute(
        """
        INSERT INTO orders (supplier, item, quantity, received)
        VALUES (?, ?, ?, 0)
        """,
        (supplier, item, quantity),
    )
    return cursor.lastrowid


def mark_received(connection, order_id):
    """Mark an order as received."""
    connection.execute(
        "UPDATE orders SET received = 1 WHERE id = ?",
        (order_id,),
    )


def notify_warehouse(supplier):
    """Display a warehouse notification."""
    print(f"Notifying warehouse about {supplier}")


def cleanup(connection):
    """Delete received orders."""
    connection.execute("DELETE FROM orders WHERE received = 1")


def pending_count(connection):
    """Return the number of orders not yet received."""
    result = connection.execute(
        "SELECT COUNT(*) FROM orders WHERE received = 0"
    ).fetchone()
    return result[0]


def order_total(connection):
    """Return the total quantity across all orders."""
    result = connection.execute(
        "SELECT COALESCE(SUM(quantity), 0) FROM orders"
    ).fetchone()
    return result[0]


def main():
    """Run a short demonstration of the order tracker."""
    with closing(create_connection()) as connection:
        with connection:
            acme_order_id = place_order(
                connection, "Acme Steel", "rods", 40
            )
            place_order(connection, "Bolt Co", "bolts", 500)
            mark_received(connection, acme_order_id)
            notify_warehouse("Acme")
            print(pending_count(connection), order_total(connection))
            cleanup(connection)


if __name__ == "__main__":
    main()
