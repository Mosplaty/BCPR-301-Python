from cmd import Cmd
from controller import Controller
from os import path, chdir, getcwd
from re import match


class Shell(Cmd):
    # This will replace the init stuff, all of it will be set in the parent class, access
    # these values using self.intro, self.prompt etc
    intro = "Welcome to our custom Interpreter shell. Type help or ? to list commands.\n"
    prompt = '(Interpreter) '
    file = None
    controller = Controller()
    directory = path.realpath(path.curdir)
    # if the init is defined then super must be used and each item attached to the object, may be better approach
    # because it is more explicit
    # def __init__(self):
    #     super().__init__()
    #     self.controller = Controller()

    # Wesley
    def do_cd(self, dir):
        """
        Syntax:
            cd [path]
            relative traversal through file structure, same as windows

        :param line:
            path: [string]

        :return:
            New working directory
        """
        try:
            line = dir.lower()
            start_path = path.realpath(path.relpath(line))
            if self.directory is None and path.isdir(start_path):
                self.directory = start_path
                print(self.directory)
            elif path.isdir(path.realpath(path.relpath(path.join(self.directory, line)))):
                self.directory = path.realpath(path.relpath(path.join(self.directory, line)))
                print(self.directory)
                print("else")
            else:
                print("Not a valid directory")
        except ValueError:
            print("Invalid command")
        except TypeError:
            print("Type of none is invalid")

    def do_load(self, arg):
        """
        Syntax:
            getfile [filename]

        :param arg:
            filename: [string]

        :return:
            File has been set
        """
        try:
            self.file = path.realpath(path.join(self.directory, path.relpath(arg)))
            result = self.controller.load(self.file)
            if result:
                self.prompt = '(Interpreter: ' + path.basename(self.file) + ') '
            else:
                print("File does not exist")
        except ValueError:
            print("No path was specified, please try again")

    def do_validate(self, *args):
        """
        Syntax:
            validate
            Validates the loaded file

        :param args:
            none

        :return:
            The valid dictionary
        """
        try:
            self.controller.validate()
        except ValueError:
            print("Invalid file selection")
    # #the_type, filename):

    def do_graph(self, arg):
        """
        Syntax:
            graph [graphtype] [filename]
            Displays a graph of the loaded data

        :param arg:
            graphtype: [bar | scatter | pie]
            filename: [string]

        :return:
            The graph
        """
        commands = arg.split(" ")
        if commands[0] == "pie" or commands[0] == "scatter" or commands[0] == "bar":
            a_path = path.join(self.directory, commands[1] + ".html")
            self.controller.set_graph(commands[0], a_path)
            criteria = input("What are the criteria? ([key] [value]) > ")
            crit = criteria.split(" ")
            self.controller.set_criteria(crit[0], crit[1])
            keys = input("What keys to use? ([key1] [key2]) > ")
            a_key = keys.split(" ")
            self.controller.set_keys(a_key[0], a_key[1])
            title = input("What is the title? >")
            self.controller.draw(a_key[0], a_key[1], title)
        else:
            print("filename is invalid")

    def do_quit(self, arg):
        """
        Syntax:
            quit
            Quit from my CMD

        :param arg:
            none

        :return:
            True
        """
        print("Quitting ......")
        return True

    def do_pwd(self, arg):
        """
        Syntax:
            pwd
            Print the current working directory

        :param arg:
            none

        :return:
            The current working directory
        """
        print(str(self.directory))


if __name__ == '__main__':
    Shell().cmdloop()
