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

def update(name):
    """ Update the snippet with a given name.

    Returns the updated snippet.
    """
    logging.error("FIXEME: Unimplemented - update({!r})".format(name))
    return ""

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

    arguments = parser.parse_args()


    # Subparser for the get command
    logging.debug("Constructing get subparser")
    get_parser = subparsers.add_parser("get", help="Get a snippet")

    # Subparser for the update command
    logging.debug("Constructing update subparser")
    get_parser = subparsers.add_parser("update", help="Update a snippet")

    # Subparser for the delete command
    logging.debug("Constructing delete subparser")
    get_parser = subparsers.add_parser("delete", help="Delete a snippet")

    arguments = parser.parse_args()

if __name__ == "__main__":
    main()
