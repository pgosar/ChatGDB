import json
from posixpath import dirname
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from os.path import abspath, dirname
from inspect import getfile, currentframe


def get_key():
    """Gets api key from secret file

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
              "tool and set up your model")
        quit("Exiting...")

    return secret[0]


def get_model():
    """Gets model from model file

    Returns: (str) model
    """
    model = []
    model_name = ""
    # gets path of this script - OS independent
    path = dirname(abspath(getfile(currentframe()))) + "/.model.txt"
    try:
        # get appropriate api key
        with open(path) as f:
            model = [line.strip() for line in f]
        for m in model:
            if m.startswith("MODEL"):
                model_name = m.split('"')[1::2]
    except FileNotFoundError:
        print("Could not find model. Please make sure you've run the CLI "
              "tool and set up your model")
        quit("Exiting...")

    return model_name[0]


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
    print(
        "ChatGDB is a python script that defines some extra helpful GDB and "
        "LLDB commands. Before use, be sure to set up your api key using the "
        "CLI tool. The commands are as follows:\n\n"
        "chat: This command is used to generate GDB/LLDB commands based on plain "
        "English input. For example, 'chat stop my code at line 7' will "
        "generate the GDB command 'break 7'. Remember that in LLDB, many "
        "commands require filename information as well.\n\n"
        "explain: This command is used to generate explanations for either "
        "the previous command or a user query. 'explain' with "
        "no arguments will generate an explanation for the previous command "
        "but typing a query after will generate an answer for it.\n\n")


HEADERS = {
    "Authorization": "Bearer " + get_key(),
    "Content-Type": "application/json"
}
URL = "https://api.openai.com/v1/chat/completions"


def explain_helper(prev_command, command, prompt):
    """Generates explanation for either the previous command or a user query

    Params:
    prev_command (str): previous command
    command (str): user query
    prompt (str): prompt to use for explanation
    """
    question = prompt + prev_command if command == "" else command
    data = {"model": get_model(),
            "messages": [{"role": "user",
                          "content": question}]}
    body, response = make_request(URL, HEADERS, data=bytes(json.dumps(data),
                                                           encoding="utf-8"))
    body = json.loads(body)
    explanation = body['choices'][0]['message']['content']
    print(explanation)


def chat_helper(command, prompt):
    """Generates GDB/LLDB command based on user input

    Params:
    command (str): user input
    prompt (str): prompt to use for command generation
    """
    data = {"model": get_model(),
            "messages": [{"role": "user",
                          "content": prompt + command}]}

    body, response = make_request(URL, HEADERS, data=bytes(json.dumps(data),
                                                           encoding="utf-8"))
    body = json.loads(body)
    command = body['choices'][0]['message']['content']
    print(command)
    # the first is technically also the previous command
    return command, command
