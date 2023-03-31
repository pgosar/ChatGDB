# ChatGDB
Harness the power of ChatGPT inside the GDB debugger!

![image](https://user-images.githubusercontent.com/55164602/229017153-1e453254-f78b-496e-bba4-57fc9863fa9f.png)


### Installation instructions
For now, the easiest way to install this is to simply clone the repository. You will need an API key, which you can get from [here](https://chatgpt.en.obiscr.com/blog/posts/2023/How-to-get-api-key/).
Create a .env file in the root of the project following the example provided with your key.

### How to use
While inside gdb, source the core.py file with ```source /path/to/core.py```. Then you can use the command chat_gdb appended by your query, for example ```chat_gdb list all breakpoints that I created```
