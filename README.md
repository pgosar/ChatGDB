# ChatGDB
Harness the power of ChatGPT inside the GDB debugger!
![image](https://user-images.githubusercontent.com/55164602/229982475-9a9724fe-91d0-48a4-aa3b-85bfc38edafa.png)


### Installation instructions
To install, run the command ```pip3 install chatgdb```. It will create an executable called
```chatgdb``` that you will have to use to set your api key. To do that, run the command

```chatgdb -k <API KEY> ```

Without the API key, you won't be able to make requests to OpenAI. The API key is stored in
text in the same directory as the installed script, which is currently in your python site packages
folder


### How to use
While inside gdb, source the core.py file with ```source /path/to/core.py```. By default, this is pythonXXX/site-packages/chatgdb/core.py.  Then you can use the command chat appended by your query, for example ```chat list all breakpoints that I created```. There is also a command called ```explain``` that you can use with no arguments to explain the previously run command, and optionally, with a query to just ask GPT a question. Run chat help to print out a short tutorial on how to use the tool.

You can also edit your ```$HOME/.gdbinit``` and source the file automatically on startup with
```source /path/to/core.py```.
