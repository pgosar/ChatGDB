import argparse
from os.path import abspath, dirname
from inspect import getfile, currentframe
from urllib.request import Request, urlopen
import json

PATH = dirname(abspath(getfile(currentframe())))


def set_key(key):
    """Set the api key for ChatGDB"""
    with open(PATH + "/.secret.txt", "w") as f:
        f.write("OPENAI_KEY=\"" + key + "\"")


def set_model(model):
    """Set the model for ChatGDB"""
    with open(PATH + "/.model.txt", "w") as f:
        f.write("MODEL=\"" + model + "\"")

def set_url(url):
    """Set the url for ChatGDB"""
    with open(PATH + "/.url.txt", "w") as f:
        f.write("URL=\"" + url + "\"")

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
        '-m',
        "--model",
        type=str,
        choices=["gpt-3.5-turbo", "gpt-4"],
        help="Provide a model for ChatGDB (gpt-3.5-turbo or gpt-4)",
        default="gpt-3.5-turbo"
    )
    parser.add_argument(
        '-u',
        "--url",
        type=str,
        help="Provide a API url for ChatGDB",
        default="https://api.openai.com/v1/chat/completions"
    )
    parser.add_argument(
        '-v',
        "--version",
        action="version",
        version="%(prog)s " + version(),
        help="Print the version of ChatGDB")

    args = parser.parse_args()
    if args.key:
        set_key(args.key)
    if args.model:
        set_model(args.model)
    if args.url:
        set_url(args.url)
    if not any([args.key, args.model, args.url]):
        parser.print_help()


if __name__ == "__main__":
    main()
