from abc import ABC
from abc import abstractmethod

class Editor(ABC):

    @abstractmethod
    def create_module_and_package(self):
        pass

    @abstractmethod
    def edit(self):
        pass

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def debug(self):
        pass

class VsCode(Editor):

    def create_module_and_package(self):
        print("Vs code create module and package")

    def edit(self):
        print("Vs code print")

    def execute(self):
        print("Vs code execute")

    def debug(self):
        print("Vs code debug")

vscode_instance = VsCode()

vscode_instance.create_module_and_package()
vscode_instance.edit()
vscode_instance.execute()
vscode_instance.debug()