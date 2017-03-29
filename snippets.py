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
    arguments = parser.parse_args()

if __name__ == "__main__":
    main()
