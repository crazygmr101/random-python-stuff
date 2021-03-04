from typing import List, Tuple, Dict
import readchar

print("Brainfuck Interpreter")

bf_program = input("Enter brainfuck program: ")

brackets: Dict[int, int] = {}
bracket_stack: List[int] = []


# find matching brackets
for index, char in enumerate(bf_program):
    if char == "[":
        bracket_stack.append(index)
    if char == "]":
        match = bracket_stack.pop()
        brackets[index] = match
        brackets[match] = index

# init program
data_ptr = 0
data = [0 for x in range(30_000)]
idx = 0

while True:
    if idx >= len(bf_program):
        break
    char = bf_program[idx]
    if char == ">":
        data_ptr += 1
        if data_ptr == len(data):
            data_ptr = 0
    if char == "<":
        data_ptr -= 1
        if data_ptr == -1:
            data_ptr = len(data) - 1
    if char == "+":
        data[data_ptr] += 1
    if char == "-":
        data[data_ptr] -= 1
    if char == ".":
        print(chr(data[data_ptr]), end="")
    if char == ",":
        data[data_ptr] = ord(readchar.readchar())
    if char == "]":
        idx = brackets[idx]
        continue
    if char == "[":
        if data[data_ptr] == 0:
            idx = brackets[idx] + 1
            continue
    idx += 1
