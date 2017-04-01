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

    with connection, connection.cursor() as cursor:
        try:
            cursor.execute("update snippets set message=%s where keyword=%s", (snippet, name))
        except psycopg2.IntegrityError as e:
            cursor.execute(command, (snippet, name))

    logging.debug("Snippet stored successfully.")
    return name, snippet

def search(text):
    """ Searches for a snippet with given text """
    with connection, connection.cursor() as cursor:
        cursor.execute("select * from snippets where message like %s", (text,))
        snippet = cursor.fetchall()
        print(snippet)
    if not snippet:
        return "404: Snippet not found."
    return snippet

def get(name):
    """ Retrieve the snippet with a given name."""
    logging.error("FIXME: Unimplemented - get({!r})".format(name))

    with connection, connection.cursor() as cursor:
        cursor.execute("select message from snippets where keyword=%s", (name,))
        snippet = cursor.fetchone()
    logging.debug("Snippet retrieved.")
    if not snippet:
        return "404: Snippet not found"
    return snippet


def delete(name):
    """ Delete the snippet with a given name."""

    logging.error("FIXME: Unimplemented - delete({!r})".format(name))

    with connection, connection.cursor() as cursor:
        cursor.execute("delete from snippets where keyword=%s", (name,))

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

    # Subparser for the search command
    logging.debug("Constructing search subparser")
    search_parser = subparsers.add_parser("search", help="Search for a snippet containing text")
    search_parser.add_argument("text", help="Text to search for")

    # Subparser for the get command
    logging.debug("Constructing get subparser")
    get_parser = subparsers.add_parser("get", help="Get a snippet")
    get_parser.add_argument("name", help="Name of the snippet")

    # Subparser for the delete command
    logging.debug("Constructing delete subparser")
    delete_parser = subparsers.add_parser("delete", help="Delete a snippet")
    delete_parser.add_argument("name", help="Name of the snippet")

    arguments = parser.parse_args()
    arguments = vars(arguments)
    command = arguments.pop("command")

    if command == "put":
        name, snippet = put(name=arguments["name"], snippet=arguments["snippet"])
        print("Stored {!r} as {!r}".format(snippet, name))
    elif command == "search":
        snippet = search(text=arguments["text"])
        print("Retrieved snippet with matching text: {!r}".format(snippet))
    elif command == "get":
        snippet = get(name=arguments["name"])
        print("Retrieved snippet: {!r}".format(snippet))
    elif command == "delete":
        name = delete(name=arguments["name"])
        print("Deleted {!r}".format(name))

if __name__ == "__main__":
    main()
