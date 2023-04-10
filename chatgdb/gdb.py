import gdb
from chatgdb import utils

prev_command = ""
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
        # handling if user is asking for help on how to use the commands
        if arg == "help":
            utils.chat_help()
            return

        prev_command, command = utils.chat_helper(arg, COMMAND_PROMPT)
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
        utils.explain_helper(prev_command, arg, EXPLANATION_PROMPT)


GDBCommand()
ExplainCommand()


def main():
    print("ChatGDB loaded successfully. Type 'chat help' for information "
          "on how to run the commands.")


if __name__ == "__main__":
    main()
