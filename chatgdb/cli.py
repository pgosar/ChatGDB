import argparse
from os.path import abspath, dirname
from inspect import getfile, currentframe
from urllib.request import Request, urlopen
import json


def set_key(key):
    """Set the api key for ChatGDB"""
    path = dirname(abspath(getfile(currentframe()))) + "/.secret.txt"
    with open(path, "w") as f:
        f.write("OPENAI_KEY=\"" + key + "\"")


def version():
    """Return version information"""
    with urlopen(Request("https://pypi.org/pypi/chatgdb/json"), timeout=10) as f:
        return json.load(f)["info"]["version"]


def main():
    parser = argparse.ArgumentParser(
        description="Configure ChatGDB, the GDB chatbot",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '-k',
        "--key",
        type=str,
        help="Provide an api key for ChatGDB")
    parser.add_argument(
        '-v',
        "--version",
        action="version",
        version="%(prog)s " + version(),
        help="Print the version of ChatGDB")

    args = parser.parse_args()
    if args.key:
        set_key(args.key)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
