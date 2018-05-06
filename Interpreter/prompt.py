from Interpreter.database_handler import DatabaseHandler
from Interpreter.filehandler import FileHandler
from Interpreter.chart import Graph
from cmd import Cmd
from os import path


class Shell(Cmd):
    # This will replace the init stuff, all of it will be set in the parent class, access
    # these values using self.intro, self.prompt etc

    # if the init is defined then super must be used and each item attached to the object, may be better approach
    # because it is more explicit
    def __init__(self):
        super().__init__()
        self.filehandler = None
        self.db_handler = DatabaseHandler()
        self.graph = None
        self.intro = "Welcome to our custom Interpreter shell. Type help or ? to list commands.\n"
        self.prompt = '>>> '
        self.file = None
        self.data = None
        self.directory = path.realpath(path.curdir)

    def do_cd(self, arg):
        """
        Syntax:
            cd [path]
            relative traversal through file structure, same as windows

        :param arg:
            path: [string]

        :return:
            New working directory
        """
        try:
            line = arg.lower()
            start_path = path.realpath(path.relpath(line))
            if self.directory is None and path.isdir(start_path):
                self.directory = start_path  # pragma: no cover
                print(self.directory)  # pragma: no cover
            elif path.isdir(path.realpath(path.relpath(path.join(self.directory, line)))):
                self.directory = path.realpath(path.relpath(path.join(self.directory, line)))
                print(self.directory)
            else:
                print("Not a valid directory")
        except ValueError:
            print("No path was specified, please try again")
        except TypeError:  # pragma: no cover
            print("Type of none is invalid")  # pragma: no cover

    def do_load(self, arg):
        """
        Syntax:
            load [filename] or [database]
            Load data from a specified location

        :param arg:
            filename: [string]

        :return:
            File has been set
        """
        # choice = input("From file or database?")
        if arg.lower() != "-database":
            try:
                if path.isfile(path.realpath(path.join(self.directory, path.relpath(arg)))):
                    self.file = path.realpath(path.join(self.directory, path.relpath(arg)))
                    self.filehandler = FileHandler(self.file)
                    result = self.filehandler.set_file_type()
                    if result:
                        self.prompt = '(Interpreter: ' + path.basename(self.file) + ') '
                        validate = self.filehandler.read()
                        self.data = validate
                        print(self.data)

                    else:
                        print("File does not exist")  # pragma: no cover
                else:
                    print("Path is not a file")
            except ValueError:
                print("No path was specified, please try again")
        elif arg.lower() == "-database":
            db = input("remote or local?")
            try:
                if db.lower() == "local":
                    db_name = input("What is the name of the database? >")
                    self.db_handler.set_local(db_name)
                    self.db_handler.insert_local_dict(self.data)
                    self.data = self.db_handler.get_local()
                    if self.check_data():
                        print("Data has been loaded")
                    else:
                        print("No data was found")  # pragma: no cover
                elif db.lower() == "remote":
                    host = input("What is the hostname? >")
                    user = input("What is the username? >")
                    password = input("Input a password >")
                    db = input("What is the database name? >")
                    self.db_handler.set_remote(host, user, password, db)
                    self.db_handler.insert_remote_dict(self.data)
                    self.data = self.db_handler.get_remote()
                    if self.check_data():
                        print("Data has been loaded")
                    else:
                        print("No data was found")  # pragma: no cover
                else:
                    print("invalid database type")
            except ValueError:
                print("Try again...")  # pragma: no cover
            except AttributeError:
                print("No data found")
        else:
            print("Invalid command")  # pragma: no cover

    def check_data(self):
        if self.data is not None:
            return True
        return False

    def do_graph(self, arg):
        """
        Syntax:
            graph [graphtype] [filename]
            Displays a graph of the loaded data

        :param arg:
            graphtype: [-bar | -scatter | -pie]
            filename: [string]

        :return:
            The graph
        """
        commands = arg.split(" ")
        if self.check_data():
            try:
                if commands[0] == "pie" or commands[0] == "scatter" or commands[0] == "bar":
                    a_path = path.join(self.directory, commands[1] + ".html")
                    self.set_graph(commands[0], a_path)
                    criteria = input("What are the criteria? ([key] [value - optional]) > ")
                    crit = criteria.split(" ")
                    if len(crit) > 1:
                        self.graph.set_criteria(crit[0], crit[1])
                    else:
                        self.graph.set_criteria(crit[0], None)
                    keys = input("What keys to use? ([key1] [key2]) > ")
                    a_key = keys.split(" ")
                    if len(a_key) > 1:
                        self.graph.set_keys(a_key[0], a_key[1])
                    else:
                        self.graph.set_keys(a_key[0], None)
                    title = input("What is the title? >")
                    if len(a_key) > 1:
                        self.graph.draw(a_key[0], a_key[1], title)
                    else:
                        self.graph.draw(a_key[0], a_key[0], title)

                else:
                    print("filename is invalid")
            except IndexError:
                print("You have entered invalid criteria")
            except KeyError:  # pragma: no cover
                print("This key is invalid")  # pragma: no cover
        else:
            print("Please set data before attempting to create a graph")

    def set_graph(self, graph_type, filename):
        print(graph_type)
        print(filename)
        self.graph = Graph()
        data = self.data
        self.graph.set_data(data, graph_type, filename)

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
        print(self.directory)

    def do_save(self, arg):
        """
        Syntax:
            save [database]
            Save the loaded dictionary to a database

        :param arg:
            database: [local | remote]

        :return:
        """
        commands = arg.split(" ")
        if self.check_data():
            try:
                if commands[0].lower() == "local":
                    db_name = input("What would you like to name the database? >")
                    self.db_handler.set_local(db_name)
                    self.db_handler.insert_local_dict(self.data)
                elif commands[0].lower() == "remote":
                    host = input("What is the hostname? >")
                    user = input("What is the username? >")
                    password = input("Input a password >")
                    db = input("What is the database name? >")
                    self.db_handler.set_remote(host, user, password, db)
                    self.db_handler.insert_remote_dict(self.data)
                else:
                    print("invalid database type")
            except ValueError:  # pragma: no cover
                print("Try again...")  # pragma: no cover
        else:
            print("Please load data before attempting to save")


if __name__ == '__main__':
    Shell().cmdloop()  # pragma: no cover
