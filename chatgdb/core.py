from posixpath import dirname
import gdb
import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from os.path import abspath, dirname
from inspect import getfile, currentframe


def get_key():
    """Gets api key from .env file

    Returns: (str) api key
    """
    key = []
    secret = ""
    # gets path of this script - OS independent
    path = dirname(abspath(getfile(currentframe()))) + "/.secret.txt"
    try:
        # get appropriate api key
        with open(path) as f:
            key = [line.strip() for line in f]
        for k in key:
            if k.startswith("OPENAI_KEY"):
                secret = k.split('"')[1::2]
    except FileNotFoundError:
        print("Could not find api key. Please make sure you've run the CLI "
              "tool and set up your api key")
        quit("Exiting...")

    return secret[0]


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
        quit("Exiting...")
    except URLError as error:
        print(error.reason)
        quit("Exiting...")
    except TimeoutError:
        print("Request timed out")
        quit("Exiting...")


def chat_help():
    """Prints help message for all available commands"""
    print("ChatGDB is a python script that defines some extra helpful GDB "
          "commands. Before use, be sure to set up your api key using the "
          "CLI tool. The commands are as follows:\n\n"
          "chat: This command is used to generate GDB commands based on plain "
          "English input. For example, 'chat stop my code at line 7' will "
          "generate the GDB command 'break 7'.\n\n"
          "explain: This command is used to generate explanations for either "
          "the previous command or a user query. 'explain' with "
          "no arguments will generate an explanation for the previous command "
          "but typing a query after will generate an answer for it.\n\n"
          )


prev_command = ""
HEADERS = {
    "Authorization": "Bearer " + get_key(),
    "Content-Type": "application/json"
}
URL = "https://api.openai.com/v1/chat/completions"
MODEL = "gpt-3.5-turbo"
COMMAND_PROMPT = "Give me a SINGLE GDB command with no explanation. Do NOT \
write any English above or below the command. Only give me the command as \
text. Here is my question: "
EXPLANATION_PROMPT = "Give me an explanation for this GDB command: "


class GDBCommand(gdb.Command):
    """Custom GDB command - chat

    The chat command is used to generate GDB commands based on plain English
    input.
    """

    def __init__(self):
        """Initializes custom GDB command"""
        super(GDBCommand, self).__init__("chat", gdb.COMMAND_DATA)

    # creates api request on command invocation
    def invoke(self, arg, from_tty):
        """Invokes custom GDB command and sends API request

        Params:
        arg (str): argument passed to command
        from_tty (bool): whether command was invoked from TTY
        """
        global prev_command
        data = {"model": MODEL,
                "messages": [{"role": "user",
                              "content": COMMAND_PROMPT + arg}]}
        # handling if user is asking for help on how to use the commands
        if arg == "help":
            chat_help()
            return

        body, response = make_request(
            URL, HEADERS, data=bytes(
                json.dumps(data), encoding="utf-8"))
        body = json.loads(body)
        command = body['choices'][0]['message']['content']
        prev_command = command
        print(command)
        gdb.execute(command)


class ExplainCommand(gdb.Command):
    """Custom GDB command - explain

    The explain command is used to generate explanations for either the
    previous command or a user query
    """

    def __init__(self):
        """Initializes custom GDB command"""
        super(ExplainCommand, self).__init__("explain", gdb.COMMAND_DATA)

    # creates api request on command invocation
    def invoke(self, arg, from_tty):
        """Invokes custom GDB command and sends API request

        Params:
            arg (str): argument passed to commands
            from_tty (bool): whether command was invoked from from_tty
        """
        content = arg
        if arg == "":
            content = EXPLANATION_PROMPT + prev_command

        data = {"model": MODEL,
                "messages": [{"role": "user",
                              "content": content}]}
        body, response = make_request(
            URL, HEADERS, data=bytes(json.dumps(data), encoding="utf-8"))
        body = json.loads(body)
        print(body['choices'][0]['message']['content'])


GDBCommand()
ExplainCommand()


def main():
    print("ChatGDB loaded successfully. Type 'chat help' for information "
          "on how to run the commands.")


if __name__ == "__main__":
    main()
