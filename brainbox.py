import sys
from collections import defaultdict

DIRECTIONS = { ">": (1,0), "<": (-1,0), "v": (0,1), "^": (0,-1) }
MP_DIRECTIONS = { "d": (1,0), "a": (-1,0), "s": (0,1), "w": (0,-1) }


class _Getch:
    """
    Provide cross-platform getch functionality. Shamelessly stolen from
    http://code.activestate.com/recipes/134892/
    """
    def __init__(self):
        try:
            self._impl = _GetchWindows()
        except ImportError:
            self._impl = _GetchUnix()

    def __call__(self): return self._impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()

getch = _Getch()

def read_character():
    # read one character from stdin. No change when no input is available.
    if online:
        try:
            char = inputs.pop(0)
        except:
            char = None
        return char
    elif sys.stdin.isatty():
        # we're in console, read a character from the user
        char = getch()
        # check for ctrl-c (break)
        if ord(char) == 3:
            sys.stdout.write("^C")
            sys.stdout.flush()
            raise KeyboardInterrupt
        elif ord(char) in [13]: # \r should act as a newline
            char = "\n"
        elif ord(char) == 27 or ord(char) > 255: # if input is <Esc> or is greater than 255, treat as EOF
            char = None
        return char
    else:
        # input is redirected using pipes
        char = sys.stdin.read(1)
        # no change if there is no more input available or if the character is out of range
        if char != "" and ord(char) > 255: char = ""
        return char if char != "" else None

class Interpreter:
    """
    brainbox interpreter.
    """
    def __init__(self, code):
        code = code.split("\n")

        # construct a 2D defaultdict to contain the code
        self._codebox = defaultdict(lambda: defaultdict(int))
        for line in range(len(code)):
            for char in range(len(code[line])):
                self._codebox[line][char] = 0 if code[line][char] == " " else ord(code[line][char])

        # construct a 2D defaultdict to contain the memory
        self._brainbox = defaultdict(lambda: defaultdict(int))
        self._mp_cell = [0,0]

        # list of pointers
        self._pointers = []

        self._position = [-1,0]
        self._facing = DIRECTIONS[">"]


    def move(self):
        """
        Move one step in the execution process, and handle the instruction (if
        any) at the new position.
        """
        # move one step in the current direction
        self._position[0] += self._facing[0]
        self._position[1] += self._facing[1]

        # wrap around if we reach the borders of the codebox
        if self._position[1] > max(self._codebox.keys()):
            self._position[1] = 0 # wrap from bottom to top

        elif self._position[1] < 0:
            self._position[1] = max(self._codebox.keys()) # wrap from top to bottom

        if self._position[0] > max(self._codebox[self._position[1]].keys()):
            self._position[0] = 0 # wrap from right to left
            
        elif self._position[0] < 0:
            self._position[0] = max(self._codebox[self._position[1]].keys()) # wrap from left to right

        # execute the instruction found
        instruction = int(self._codebox[self._position[1]][self._position[0]])
        # the current position might not be a valid character
        try:
            # use space if current cell is 0
            instruction = chr(instruction) if instruction > 0 else " "
        except:
            instruction = None
        try:
            self._handle_instruction(instruction)
        except KeyboardInterrupt:
            # avoid catching as error
            raise KeyboardInterrupt

    def _handle_instruction(self, command):
        """
        Execute an instruction.
        """
        if command == None:
            raise Exception

        mp_x = self._mp_cell[0]
        mp_y = self._mp_cell[1]
        mp_value = self._brainbox[mp_x][mp_y]

        if command in DIRECTIONS:
            self._facing = DIRECTIONS[command]

        elif command in MP_DIRECTIONS:
            self._mp_cell[0] += MP_DIRECTIONS[command][0]
            self._mp_cell[1] += MP_DIRECTIONS[command][1]

        elif command == "+":
            if mp_value < 255:
                self._brainbox[mp_x][mp_y] += 1

        elif command == "-":
            if mp_value > 0:
                self._brainbox[mp_x][mp_y] -= 1

        elif command == "[":
            if mp_value:
                self._pointers.append([self._position[0],self._position[1]])

        elif command == "]":
            if mp_value:
                try:
                    new_x, new_y = self._pointers[-1]
                except IndexError: # if there's no pointer to jump to, jump to just before 0,0
                    new_x = 0 - self._facing[0]
                    new_y = 0 - self._facing[1]
                self._position = [new_x, new_y]
            else:
                try:
                    self._pointers.pop()
                except:
                    pass

        elif command == ".":
            global online
            global out
            char = chr(mp_value)
            if online:
                out[1] += char
            else:
                sys.stdout.write(char)
                sys.stdout.flush()
        
        elif command == ",":
            char = read_character()
            if char != None: self._brainbox[mp_x][mp_y] = ord(char)

        elif command == "!":
            raise StopExecution()

class StopExecution(Exception):
    pass


def execute(code, input_list, output_var):
    global out
    global online
    global inputs
    out = output_var
    out[1] = ""
    out[2] = ""
    online = True
    inputs = [char for char in input_list]

    interp = Interpreter(code)

    while True:
        try:
            interp.move()
        except StopExecution:
            return


if __name__ == "__main__":

    try:
        if sys.argv[1] == "h":
            exit(f"Usage: $ python {sys.argv[0]} path/to/program")# [flags]")
        else:
            try:
                code = open(sys.argv[1], 'r').read()
            except:
                exit(f"Error: There was a problem reading the file - {sys.argv[1]}")
    except IndexError:
        exit(f"Error: A file path is required: $ python {sys.argv[0]} path/to/program")# [flags]")

    interp = Interpreter(code)

    try:
        while True:
            try:
                interp.move()
            except StopExecution:
                exit("\n")
    except KeyboardInterrupt:
        exit("\n")
