class Component:
    def __init__(self, name):
        self.name = name
        self.parent = None

    def move(self, new_path):
        new_folder = get_path(new_path)
        del self.parent.children[self.name]
        new_folder.children[self.name] = self
        self.parent = new_folder

    def delete(self):
        del self.parent.children[self.name]

class Folder(Component):
    def __init__(self, name):
        super().__init__(name)
        self.children = {}

    def add_child(self, child):
        self.children[child.name] = child
        child.parent = self

class File(Component):
    def __init__(self, name, contents):
        super().__init__(name)
        self.contents = contents

root = Folder('root')
def get_path(path):
    names = path.split('/')[1:]
    node = root
    for name in names:
        node = node.children[name]
    return node

folder1 = Folder("folder1")
folder2 = Folder("folder2")
file1 = File("file1.txt", "Hello world")

root.add_child(folder1)
folder1.add_child(folder2)
folder2.add_child(file1)

print(get_path("/folder1/folder2/file1.txt").contents)
