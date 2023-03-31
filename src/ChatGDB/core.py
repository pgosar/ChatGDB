import gdb
import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

key = []
secret = ""
# obtain appropriate api key from env file but without any dependencies :)
with open("../../.env") as f:
    key = [line.strip() for line in f]
for k in key:
    if k.startswith("OPENAI_KEY"):
        secret = k.split('"')[1::2]
secret = secret[0]

# make api request
def make_request(url, headers=None, data=None):
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
        super(ChatGDB, self).__init__("chat_gdb", gdb.COMMAND_DATA)

    def invoke(self, arg, from_tty):
        promptEngineering = "Give me GDB commands with no explanation. Do NOT write any english above or below the command. Only give me the command as text. Here is my question: "
        url = "https://api.openai.com/v1/chat/completions"
        headers = {"Authorization": "Bearer " + secret, "Content-Type": "application/json"}
        data = {"model": "gpt-3.5-turbo", "messages":[{"role": "user", "content": promptEngineering + arg}] }
        body, response = make_request(url, headers, data=bytes(json.dumps(data), encoding="utf-8"))
        body = json.loads(body)
        gdb.execute(body['choices'][0]['message']['content'])

ChatGDB()