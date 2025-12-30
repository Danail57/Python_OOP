import sys
from abc import ABC, abstractmethod


class Window:
    def exit(self):
        print("[Window] Exiting application")
        sys.exit(0)


class Document:
    def __init__(self, filename):
        self.filename = filename
        self.contents = "This file cannot be modified"

    def save(self):
        print(f"[Document] Saving file: {self.filename}")
        with open(self.filename, "w") as file:
            file.write(self.contents)
        print("[Document] File saved successfully")


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class SaveCommand(Command):
    def __init__(self, document):
        self.document = document

    def execute(self):
        print("[Command] SaveCommand executed")
        self.document.save()


class ExitCommand(Command):
    def __init__(self, window):
        self.window = window

    def execute(self):
        print("[Command] ExitCommand executed")
        self.window.exit()


# ===== Invokers =====
class ToolBarButton:
    def __init__(self, name, iconname, command):
        self.name = name
        self.iconname = iconname
        self.command = command

    def click(self):
        print(f"[Toolbar Button] {self.name} clicked")
        self.command.execute()


class MenuItem:
    def __init__(self, menu_name, item_name, command):
        self.menu = menu_name
        self.item = item_name
        self.command = command

    def click(self):
        print(f"[Menu Item] {self.menu} -> {self.item} selected")
        self.command.execute()


class KeyboardShortcut:
    def __init__(self, key, modifier, command):
        self.key = key
        self.modifier = modifier
        self.command = command

    def keypress(self):
        print(f"[Keyboard Shortcut] {self.modifier} + {self.key} pressed")
        self.command.execute()


window = Window()
document = Document("example.txt")

save_command = SaveCommand(document)
exit_command = ExitCommand(window)

toolbar_save = ToolBarButton("Save", "save_icon.png", save_command)
menu_save = MenuItem("File", "Save", save_command)
menu_exit = MenuItem("File", "Exit", exit_command)
shortcut_save = KeyboardShortcut("S", "Ctrl", save_command)

print("\n--- Application Started ---\n")

toolbar_save.click()
menu_save.click()
shortcut_save.keypress()
