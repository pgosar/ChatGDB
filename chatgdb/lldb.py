import lldb
from chatgdb import utils


def __lldb_init_module(debugger, internal_dict):
    """This function handles the initialization of the custom commands"""
    # lldb doesn't trigger python's main function so we print the help here
    print("ChatLLDB loaded successfully. Type 'chat help' for information "
          "on how to run the commands.")
    debugger.HandleCommand('command script add -f lldb.chat chat')
    debugger.HandleCommand('command script add -f lldb.explain explain')


prev_command = ""
COMMAND_PROMPT = "Give me a SINGLE LLDB command with no explanation. Do NOT \
give me a GDB command. DO NOT write any English above or below the command. \
Only give me the command as text. Here is my question: "
EXPLANATION_PROMPT = "Give me an explanation for this LLDB command: "


def chat(debugger, command, result, internal_dict):
    """Custom LLDB command - chat

    The chat command is used to generate GDB commands based on plain English
    input.
    """
    global prev_command
    # handle when user types 'chat help'
    if command == "help":
        utils.chat_help()
        return
    prev_command, command = utils.chat_helper(command, prompt=COMMAND_PROMPT)
    debugger.HandleCommand(command)


def explain(debugger, command, result, internal_dict):
    """Custom LLDB command - explain

    The explain command is used to generate explanations for either the
    previous command or a user query
    """
    utils.explain_helper(prev_command, command, prompt=EXPLANATION_PROMPT)
