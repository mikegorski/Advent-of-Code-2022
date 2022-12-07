from __future__ import annotations
from typing import Dict, Optional


class Tree:
    
    def __init__(self, name: str, children: Optional[Dict[str, Tree]], is_dir: bool,
                parent: Optional[Tree], size: Optional[int] = 0):
        self.name = name
        self.children = children
        self.is_dir = is_dir
        self.parent = parent
        self.size = size

    def __repr__(self):
        return f'Tree: name = {self.name}, parent = {self.parent}, size = {self.size}'


def load_input(filename):
    with open(filename) as f:
        input_data = [line.rstrip('\n') for line in f]
    return input_data


if __name__ == "__main__":

    terminal_output = load_input('data.txt')

    files = []
    dirs = []
    idx = 0
    while idx < len(terminal_output):
        line = terminal_output[idx]
        if line.startswith('$ cd'):
            dir_name = line[5:]
            directory = Tree(name = dir_name, children = {}, is_dir = True,
                            parent = None)
            if dir_name == '/':
                structure = directory
                dirs.append(structure)
            elif dir_name == '..':
                structure = structure.parent
            else:
                structure = structure.children[dir_name]
                dirs.append(structure)
            idx += 1
        elif line.startswith('$ ls'):
            idx += 1
            line = terminal_output[idx]
            while idx < len(terminal_output) and not line.startswith('$'):
                if line.startswith('dir'):
                    dir_name = line[4:]
                    structure.children[dir_name] = Tree(name = dir_name,
                                                       children = {}, is_dir = True,
                                                       parent = structure)
                else:
                    file = Tree(name = line, children = {}, is_dir = False,
                                parent = structure, size = int(line.split(' ')[0]))
                    structure.children[line] = file
                    files.append(file)
                idx += 1
                if idx < len(terminal_output): line = terminal_output[idx]
             
    for file in files:
        size = file.size
        while file.parent is not None:
            file.parent.size += size
            file = file.parent

    ### TASK 1 ###
    size_lt_100000 = sum([dir.size for dir in dirs if dir.size <= 100000])
    print(size_lt_100000)

    ### TASK 2 ###
    memory_taken = dirs[0].size
    memory_needed = memory_taken - (7-3)*10**7
    print(sorted([x.size for x in dirs if x.size >= memory_needed])[0])