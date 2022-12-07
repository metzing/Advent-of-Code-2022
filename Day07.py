class Directory():
    def __init__(self, parent, name):
        self.type = 'DIR'
        self._parent = parent
        self.name = name
        self.children = []
    
    def add(self, child):
        if all(child.name != existing.name for existing in self.children):
            self.children.append(child)
        
        self.children.sort(key=lambda child: child.name)

    def get_child(self, child_name):
        return next(child for child in self.children if child.name == child_name)

    @property
    def size(self):
        return sum(child.size for child in self.children)

    @property
    def parent(self):
        return self._parent
    
    @property
    def full_name(self):
        return '~' if self.parent is None else self.parent.full_name + '/' + self.name

class File():
    def __init__(self, name, size):
        self.type = 'FILE'
        self.name = name
        self._size = int(size)

    @property
    def size(self):
        return self._size
    
filesystem = Directory(None, '/')
current_dir = filesystem

for trimmed in (line.strip() for line in open('Day07.txt')):
    split = trimmed.split(' ')

    if split[0] == '$':
        if split[1] == 'cd':
            if split[2] == '/':
                current_dir = filesystem
            elif split[2] == '..':
                current_dir = current_dir.parent
            else:
                current_dir = current_dir.get_child(split[2])
    else:
        if (split[0] == 'dir'):
            current_dir.add(Directory(current_dir, split[1]))
        else:    
            current_dir.add(File(split[1], split[0]))

dirSizes = {}

def gather_dir_sizes(dir):
    dirSizes[dir.full_name] = dir.size

    for child in dir.children:
        if child.type == 'DIR':
            gather_dir_sizes(child)

gather_dir_sizes(filesystem)

print(sum(size for size in dirSizes.values() if size <= 100000))