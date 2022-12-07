import re
import sys

class Directory:

    def __init__(self, name, parent):        
        self._name = name
        self._parent = parent
        self._files_size = 0
        self._child_dir = {}
        self._size = None

    def __len__(self):    
        if not self._size:
            self._size = self._files_size + sum([len(child) for child in self._child_dir.values()])
        return self._size

    def increment_file_size(self, size):        
        self._files_size += size

    def add_child_dir(self, child_name, child):
        self._child_dir[child_name] = child    

    def get_child_dir(self, name):
        if name not in self._child_dir:        
            child = Directory(name, self)
            self._child_dir[name] = child
            
        return self._child_dir[name]

    def get_child_dirs(self):
        return self._child_dir.values()


def getLine(file):
    return file.readline().strip()


def process_cd(dir_name, pwd, root):
    return root if dir_name == '/' else pwd._parent if dir_name == '..' else pwd.get_child_dir(dir_name)


def process_ls(file, pwd):
    while line := getLine(file):
        if line.startswith('$'):
            return line
        elif line.startswith('dir'):
            pwd.get_child_dir(line[4:])
        else: 
            pwd.increment_file_size(int(line.split(' ')[0]))


def create_file_structure(root):    
    input_file = open('input-7-1.txt')
    pwd = root

    line = getLine(input_file)
    while line:
        command_executed = re.match(r'^\$ (cd |ls)(.*)', line)
        if command_executed.groups()[0] == 'ls':
            line = process_ls(input_file, pwd)           
        else:
            pwd = process_cd(command_executed.groups()[1], pwd, root)
            line = getLine(input_file)          


def get_sum_of_dir_size_lte_limit(dir, limit):
    size = len(dir)
    return (size if size <= limit else 0) + 
        sum([get_sum_of_dir_size_lte_limit(child, limit) for child in dir.get_child_dirs()])


def get_lowest_adequate_size(dir, limit, current):
    size = len(dir)
    if size >= limit:
        current = min(size, current)
        children = dir.get_child_dirs()
        if len(children) > 0:
            return min(get_lowest_adequate_size(child, limit, current) for child in children)    
    
    return current


ROOT = Directory('/', None)
create_file_structure(ROOT)

LIMIT = 100000
print(f'Sum of dir sizes with size less than {LIMIT} {get_sum_of_dir_size_lte_limit(ROOT, LIMIT)}')

TOTAL_DISK_SPACE = 70000000
SPACE_NEEDED_FOR_UPDATE = 30000000
min_file_deletion_size = SPACE_NEEDED_FOR_UPDATE - (TOTAL_DISK_SPACE - len(ROOT))
lowest_adequate_size = get_lowest_adequate_size(ROOT, min_file_deletion_size, sys.maxsize)

print(f'Size of smallest directory that can provide {min_file_deletion_size} is {lowest_adequate_size}')
