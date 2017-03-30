import logging
import argparse

# Set the log output file, and the log level
logging.basicConfig(filename="snippets.log", level=logging.DEBUG)

def put(name, snippet):
    """
    Store a snippet with an associated name.

    Returns the name and the snippet
    """
    logging.error("FIXME: Unimplemented - put({!r}, {!r})".format(name, snippet))
    return name, snippet

def get(name):
    """ Retrieve the snippet with a given name.

    If there is no such snippet, return '404: Snippet Not Found'.

    Returns the snippet.
    """
    logging.error("FIXME: Unimplemented - get({!r})".format(name))
    return ""

def update(name, snippet):
    """ Update the snippet with a given name.

    Returns the updated snippet.
    """
    logging.error("FIXEME: Unimplemented - update({!r})".format(name))
    return name, snippet

def delete(name):
    """ Delete the snippet with a given name.

    Returns deleted snippet name.
    """
    logging.error("FIXME: Unimplemented - delete({!r})".format(name))
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

     Subparser for the update command
    logging.debug("Constructing update subparser")
    update_parser = subparsers.add_parser("update", help="Update a snippet")
    update_parser.add_argument("name", help="name of the snippet")
    update_parser.add_argument("snippet", help="updated snippet text")

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
    elif command == "get":
        snippet = get(name=arguments["name"])
        print("Retrieved snippet: {!r}".format(snippet))
    elif command == "update":
        snippet = update(**arguments)
        print("Updated {!r} with {!r}".format(name, snippet))
    elif command == "delete":
        snippet = delete(**arguments)
        print("Deleted {!r}".format(snippet))

if __name__ == "__main__":
    main()
