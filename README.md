# ChatGDB
Harness the power of ChatGPT inside the GDB debugger!
![Image](https://lh5.googleusercontent.com/xZMLwWWxavqYjC3fyCIZJ0m-s-f-XEoiOeWGbxRrw3dWoukUoWzJJ4iiBkVO2Vtiyr4K6o0WkTs7B40TapeBPIYwgVRVhDXGVjB4tFYoKH3_nK847nYXl3pISB6dEP6Wp_o0uPlfJOjCrLspm0_VNw)

### Installation instructions
First, make sure you install [pip](https://pip.pypa.io/en/stable/installation/)

To install, run the command ```pip3 install chatgdb```. It will create an executable called
```chatgdb``` that you will have to use to set your api key. To do that, run the command

```chatgdb -k <API KEY> ```

Without the API key, you won't be able to make requests to OpenAI. The API key is stored in
text in the same directory as the installed script, which is currently in your python site packages
folder along with the main script. You can easily find this location by running the following in your terminal:

``` python -m site --user-site```

Optionally, you can also download the compressed files in the releases page to get the scripts directly.
If you do this, you will need to instead invoke the cli tool with 

```python path/to/cli.py -k <API KEY>```.


### How to use
I first recommend editing your ```$HOME/.gdbinit``` to source the main script automatically on startup. Run the following command:

```echo "source $(python -m site --user-site)/chatgdb/core.py" > $HOME/.gdbinit```

While inside GDB the command chat appended by your query, for example ```chat list all breakpoints that I created```. There is also a command called ```explain``` that you can use with no arguments to explain the previously run command, and optionally, with a query to just ask GPT a question. For example, running ```explain``` directly after running ```break 7``` would prompt the tool to explain how breakpoints work. Running ```explain how input formatting works in gdb``` would prompt it to explain input formatting (see the image at the top).

Run chat help to print out a short tutorial on how to use the tool.

