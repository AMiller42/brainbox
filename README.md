# brainbox

Brainbox is a 2-dimensional [brainf***](https://esolangs.org/wiki/Brainfuck) derivative. The code is laid out on a 2D grid, called the codebox. Instead of being a tape, the memory is also laid out on a 2D grid, which stretches out infinitely in all directions, called the brainbox. The current point on the codebox is represented by the Instruction Pointer (IP), and the current point on the brainbox is represented by the Memory Pointer (MP).

---

## Getting Started

Brainbox requires Python 3.
```
$ python brainbox.py h
Usage: $ python brainbox.py path/to/program
```
---

## Features

Being a brainf*** derivative, most of the commands in brainbox are quite similar, with a few key differences:

- The `[` and `]` commands work a little bit differently in brainbox. Since it is 2D, the idea of jumping to the "next" or "previous" bracket pretty much goes out the window. Instead, `[` saves the current position of the IP as a pointer if the cell at the MP is nonzero, and `]` jumps execution to the last saved pointer if the cell at the MP is non zero, retaining current direction. If there are no pointers, execution jumps to the point just before coordinates `(0,0)`. This allows execution to loop back to the beginning of the program without putting a `[` there.

- Changing the direction of the IP is done with `^ < v >`, which correspond to Up, Left, Down, and Right, respectively. The IP starts execution at the top left corner of the codebox facing right, and continues in whatever direction it is in until changed, executing every instruction it comes across.

- Moving the MP is done with `w a s d`, which correspond to Up, Left, Down, and Right, respectively. The MP starts at coordinates (0,0), and moves one cell at a time.

- Upon hitting the edges of the program, the IP will wrap around to the other side, maintaining direction. Execution ends when the IP reaches a `!` command.

Other than that, all commands are the same as in brainf***, namely:
| `+` | Increment the cell at the MP - Values cap at 255                    |
| `-` | Decrement the cell at the MP - Values cap at 0                      |
| `,` | Input a character and store its ordinal value in the cell at the MP |
| `.` | Output the value in the cell at the MP as a character               |

All other characters are ignored by the interpreter and act as NOPs.

---

## Input

Input is done one character at a time. If input is piped in from another command, upon reaching EOF, the value in the cell at the MP remains unchanged. If inputting from STDIN on the console, <kbd>Esc</kbd> represents EOF. In either form of input, characters whose ordinal values are greater than 255 are ignored, and are instead treated as EOF.

---

## Computational Class

Being a brainf*** derivative, brainbox is trivially [Turing-complete](https://en.wikipedia.org/wiki/Turing_completeness).
