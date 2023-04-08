### Reporting Issues

We'd love to hear ideas for new features or suggestions on improving the tool. Feel free to create an
issue on [GitHub](https://github.com/pgosar/ChatGDB) if you have any in mind!

Before submitting bug reports, please make sure you've [updated](https://github.com/pgosar/ChatGDB#updating) 
ChatGDB. When writing a bug report on [GitHub](https://github.com/pgosar/ChatGDB), please provide
relevant information that can help us figure out what went wrong. This could include but is not limited
to:

- The output of ```chatgdb -v```
- Your system information (operating system and version)
- How to reproduce the bug
- Anything else you think is useful

### Developing and Making Pull Requests

We gladly accept pull requests in the [official repository](https://github.com/pgosar/ChatGDB) for
bug fixes, features, etc.

Working on the project is as simple as cloning the repository and installing [poetry](https://python-poetry.org/docs/).
We use poetry to build the project and generate the ```chatgdb``` executable. Use the command

```poetry build```

to generate the binaries. Then, run

```pip3 install .``` 

in the repository's root directory to simulate a user installation so that you can
easily test your changes. Finally, you can simply uninstall the local version with

```pip3 uninstall chatgdb```

Please be sure to format your code according to the [pep8 guidelines](https://pep8.org/)
- this is what the repository follows. I recommend installing [autopep8](https://github.com/hhatto/autopep8) to help with this.

