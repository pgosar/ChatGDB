import argparse
from os.path import abspath, dirname
from inspect import getfile, currentframe


def set_key(key):
    """Set the api key for ChatGDB"""
    path = dirname(abspath(getfile(currentframe()))) + "/.secret.txt"
    with open(path, "w") as f:
        f.write("OPENAI_KEY=\"" + key + "\"")


def main():
    parser = argparse.ArgumentParser(
        description="Configure ChatGDB, the GDB chatbot",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '-k',
        "--key",
        type=str,
        help="Provide an api key for ChatGDB")

    args = parser.parse_args()
    if args.key:
        set_key(args.key)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
