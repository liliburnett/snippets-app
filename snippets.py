import logging
import argparse
import psycopg2

# Set the log output file, and the log level
logging.basicConfig(filename="snippets.log", level=logging.DEBUG)

logging.debug("Connecting to PostgreSQL")
connection = psycopg2.connect(database="snippets", user="lili")
logging.debug("Database connection established.")

def put(name, snippet):
    """Store a snippet with an associated name."""
    logging.error("FIXME: Unimplemented - put({!r}, {!r})".format(name, snippet))

    cursor = connection.cursor()
    command = "insert into snippets values (%s, %s)"
    cursor.execute(command, (name, snippet))
    connection.commit()
    logging.debug("Snippet stored successfully.")
    return name, snippet

def get(name):
    """ Retrieve the snippet with a given name."""
    logging.error("FIXME: Unimplemented - get({!r})".format(name))

    cursor = connection.cursor()
    command = "select * from snippets where keyword=%s"
    cursor.execute(command, (name,))
    snippet = cursor.fetchone()
    connection.commit()
    logging.debug("Snippet retrieved.")
    return snippet

def update(snippet, name):
    """ Update the snippet with a given name."""

    logging.error("FIXEME: Unimplemented - update({!r})".format(name))
    cursor = connection.cursor()
    command = "update snippets set message=%s where keyword=%s"
    cursor.execute(command, (snippet, name))
    connection.commit()
    logging.debug("Snippet updated successfully.")
    return snippet, name

def delete(name):
    """ Delete the snippet with a given name."""

    logging.error("FIXME: Unimplemented - delete({!r})".format(name))

    cursor = connection.cursor()
    command = "delete from snippets where keyword=%s"
    cursor.execute(command, (name,))
    connection.commit()
    logging.debug("Snippet successfully deleted.")
    return name

def main():
    """ Main function"""
    logging.info("Constructing Parser")
    parser = argparse.ArgumentParser(description="Store and retrieve snippets.")

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Subparser for the put command
    logging.debug("Constructing put subparser")
    put_parser = subparsers.add_parser("put", help="Store a snippet")
    put_parser.add_argument("name", help="Name of the snippet")
    put_parser.add_argument("snippet", help="Snippet text")

    # Subparser for the get command
    logging.debug("Constructing get subparser")
    get_parser = subparsers.add_parser("get", help="Get a snippet")
    get_parser.add_argument("name", help="Name of the snippet")

    # Subparser for the update command
    logging.debug("Constructing update subparser")
    update_parser = subparsers.add_parser("update", help="Update a snippet")
    update_parser.add_argument("snippet", help="updated snippet text")
    update_parser.add_argument("name", help="name of snippet")

    # Subparser for the delete command
    logging.debug("Constructing delete subparser")
    delete_parser = subparsers.add_parser("delete", help="Delete a snippet")
    delete_parser.add_argument("name", help="Name of the snippet")

    arguments = parser.parse_args()
    arguments = vars(arguments)
    command = arguments.pop("command")
    print(arguments["name"])
    if command == "put":
        name, snippet = put(name=arguments["name"], snippet=arguments["snippet"])
        print("Stored {!r} as {!r}".format(snippet, name))
    elif command == "get":
        snippet = get(name=arguments["name"])
        print("Retrieved snippet: {!r}".format(snippet))
    elif command == "update":
        snippet, name = update(snippet=arguments["snippet"], name=arguments["name"])
        print("Updated {!r} with {!r}".format(snippet, name))
    elif command == "delete":
        name = delete(name=arguments["name"])
        print("Deleted {!r}".format(name))

if __name__ == "__main__":
    main()
