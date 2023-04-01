from posixpath import dirname
import gdb
import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from os.path import abspath, dirname
from inspect import getfile, currentframe

URL = "https://api.openai.com/v1/chat/completions"
MODEL = "gpt-3.5-turbo"
PROMPT = "Give me GDB commands with no explanation. Do NOT write any \
        English above or below the command. Only give me the command as text. \
        Here is my question: "


def get_key():
    """Gets api key from .env file

    Returns: (str) api key
    """
    key = []
    secret = ""
    # gets path of this script - OS independent
    path = dirname(abspath(getfile(currentframe()))) + "/../../.env"
    try:
        # get appropriate api key
        with open(path) as f:
            key = [line.strip() for line in f]
        for k in key:
            if k.startswith("OPENAI_KEY"):
                secret = k.split('"')[1::2]
    except FileNotFoundError:
        print("Could not find .env file. Please make sure you have a .env file "
              "containing your api key in the root directory of this project.")
        quit("Exiting...")

    return secret[0]


# make api request
def make_request(url, headers=None, data=None):
    """Makes API request
    
    Params:
    url (str): url to make request to
    headers (dict, optional): headers to send with request. Defaults to None.
    data (bytes, optional): data to send with request. Defaults to None.
    """
    request = Request(url, headers=headers or {}, data=data)
    try:
        with urlopen(request, timeout=10) as response:
            return response.read(), response
    except HTTPError as error:
        print(error.status, error.reason)
    except URLError as error:
        print(error.reason)
    except TimeoutError:
        print("Request timed out")


class ChatGDB(gdb.Command):
    def __init__(self):
        """Initializes custom GDB command"""
        super(ChatGDB, self).__init__("chat_gdb", gdb.COMMAND_DATA)

    # creates api request on command invocation
    def invoke(self, arg, from_tty):
        """Invokes custom GDB command and sends API request

        Params:
        arg (str): argument passed to command
        from_tty (bool): whether command was invoked from TTY
        """
        headers = {
            "Authorization": "Bearer " + get_key(),
            "Content-Type": "application/json"}
        data = {"model": MODEL,
                "messages": [{"role": "user",
                              "content": PROMPT + arg}]}

        body, response = make_request(
            URL, headers, data=bytes(
                json.dumps(data), encoding="utf-8"))
        body = json.loads(body)
        print(body['choices'][0]['message']['content'])
        gdb.execute(body['choices'][0]['message']['content'])


ChatGDB()
