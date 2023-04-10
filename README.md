# ChatGDB
Harness the power of ChatGPT inside the GDB/LLDB debugger!


ChatGDB is a tool designed to superpower your debugging experience with GDB or LLDB, debuggers for compiled languages. Use it to accelerate your debugging workflow by leveraging the power of ChatGPT to assist you while using GDB/LLDB! 

It allows you to explain in natural language what you want to do, and then automatically execute the relevant command. Optionally, you can ask ChatGPT to explain the command it just ran or even pass in any question for it to answer. Focus on what's important - figuring out that nasty bug instead of chasing down GDB/LLDB commands at the tip of your tongue.

![Image](https://lh5.googleusercontent.com/xZMLwWWxavqYjC3fyCIZJ0m-s-f-XEoiOeWGbxRrw3dWoukUoWzJJ4iiBkVO2Vtiyr4K6o0WkTs7B40TapeBPIYwgVRVhDXGVjB4tFYoKH3_nK847nYXl3pISB6dEP6Wp_o0uPlfJOjCrLspm0_VNw)

## Contents

1. [Installation](#installation-intructions)
2. [Updating](#updating)
3. [Usage](#usage)
4. [Contributing](#contributing)
5. [Getting Updates](#getting-updates)

### Installation instructions
First, make sure you install [pip](https://pip.pypa.io/en/stable/installation/). ChatGDB also
requires a python version of 3.3 or above.

To install, run the command 

```pip3 install chatgdb```. 

It will create an executable called ```chatgdb``` that you will have to use to set your api key. 
To do that, run the command

```chatgdb -k <API KEY> ```

You also need to set the model to use. There are two possible options, ```gpt-3.5-turbo``` and ```gpt-4```:

```chatgdb -m <MODEL>```

This information is stored in text in the same directory as the installed script, which is currently in your python site packages
folder along with the main script. You can easily find this location by running the following in your terminal:

``` python -m site --user-site```

Optionally, you can also download the compressed files in the releases page to get the scripts directly.
If you do this, navigate to the ```chatgdb``` folder, and you can install with

```pip3 install .```.

### Updating

To update ChatGDB, run the following

```pip3 install chatgdb --upgrade```


### Usage
For GDB usage, I first recommend editing your ```$HOME/.gdbinit``` to source the main script automatically on startup. Run the following command:

```echo "source $(python -m site --user-site)/chatgdb/gdb.py" > $HOME/.gdbinit```

The same applies for LLDB. Edit your ```$HOME/.lldbinit``` and run the following command:

```echo "command script import $(python -m site --user-site)/chatgdb/lldb.py" > $HOME/.lldbinit```

While inside your debugger, you can run the command chat appended by your query, for example ```chat list all breakpoints that I created```. 
There is also a command called ```explain``` that you can use with no arguments to explain the previously run command, 
and optionally, with a query to just ask GPT a question. For example, running ```explain``` directly after running 
```break 7``` would prompt the tool to explain how breakpoints work. Running ```explain how input formatting works in gdb``` 
would prompt it to explain input formatting (see the image at the top).

Run chat help to print out a short tutorial on how to use the tool.

### Contributing
Thanks for your interest in contributing to ChatGDB! See [CONTRIBUTING.md](CONTRIBUTING.md) on ways to
help the development effort. 

### Staying Updated

If you'd like to stay up-to-date on new features/fixes, follow my [twitter](https://twitter.com/pranay__gosar). There's plenty
of exciting features on the horizon such as complete context-awareness that will make it possible
for ChatGDB to not only help you use GDB, but to help you fix the code itself.
