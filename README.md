# brainbox

Brainbox is a 2-dimensional [brainf***](https://esolangs.org/wiki/Brainfuck) derivative. The code is laid out on a 2D grid, called the codebox, similar to how a [Befunge](https://esolangs.org/wiki/Befunge) program is laid out. Instead of being a tape, the memory is also laid out on a 2D grid, which stretches out infinitely in all directions, called the brainbox. The current point on the codebox is represented by the Instruction Pointer (IP), and the current point on the brainbox is represented by the Memory Pointer (MP).

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

- The `[` and `]` commands work a little bit differently in brainbox. Since it is 2D, the idea of jumping to the "next" or "previous" bracket pretty much goes out the window. Instead, `[` saves the current position of the IP as a pointer if the cell at the MP is nonzero, and `]` jumps execution to the last saved pointer if the cell at the MP is nonzero, retaining current direction. If there are no pointers, execution jumps to the point just before coordinates `(0,0)`. This allows execution to loop back to the beginning of the program without putting a `[` there.

- Changing the direction of the IP is done with `^ < v >`, which correspond to Up, Left, Down, and Right, respectively. The IP starts execution at the top left corner of the codebox facing right, and continues in whatever direction it is in until changed, executing every instruction it comes across.

- Moving the MP is done with `w a s d`, which correspond to Up, Left, Down, and Right, respectively. The MP starts at coordinates (0,0), and moves one cell at a time.

- Upon hitting the edges of the program, the IP will wrap around to the other side, maintaining direction. Execution ends when the IP reaches a `!` command.

Other than that, all commands are the same as in brainf***, namely:

| Command | Function                                                            |
|:-------:|---------------------------------------------------------------------|
|   `+`   | Increment the cell at the MP - Values cap at 255                    |
|   `-`   | Decrement the cell at the MP - Values cap at 0                      |
|   `,`   | Input a character and store its ordinal value in the cell at the MP |
|   `.`   | Output the value in the cell at the MP as a character               |

All other characters are ignored by the interpreter and act as NOPs.

---

## Input

Input is done one character at a time. If input is piped in from another command, upon reaching EOF, the value in the cell at the MP remains unchanged. If inputting from STDIN on the console, <kbd>Esc</kbd> represents EOF. In either form of input, characters whose ordinal values are greater than 255 are ignored, and are instead treated as EOF.

---

## Computational Class

Being a brainf*** derivative, brainbox is trivially [Turing-complete](https://en.wikipedia.org/wiki/Turing_completeness).

---

## Tests

There are three example programs included in the repository to let you try out the language:

### Hello, World!
```
 ++++<!.+aa.--------.------.+++.d.-d.------------.++++++++++++aa.+++..+++++++.---w.dd]-sa-a+w+d]-ds+a+++a+++w++d[++++d
```
[Try it Online!](http://brainbox.pythonanywhere.com?code=%20%2B%2B%2B%2B%3C!.%2Baa.--------.------.%2B%2B%2B.d.-d.------------.%2B%2B%2B%2B%2B%2B%2B%2B%2B%2B%2B%2Baa.%2B%2B%2B..%2B%2B%2B%2B%2B%2B%2B.---w.dd%5D-sa-a%2Bw%2Bd%5D-ds%2Ba%2B%2B%2Ba%2B%2B%2Bw%2B%2Bd%5B%2B%2B%2B%2Bd&inputs=)

### Cat
```
-],.]!
```
[Try it Online!](http://brainbox.pythonanywhere.com?code=-%5D%2C.%5D!&inputs=Hello%2C%20Waffles!)

### Truth-machine
```
,.[[a+d-d+a]d-]a+[aa]d[.]!
```
[Try it Online!](http://brainbox.pythonanywhere.com?code=%2C.%5B%5Ba%2Bd-d%2Ba%5Dd-%5Da%2B%5Baa%5Dd%5B.%5D!%0A%0AThis%20program%20was%20made%20by%20CGCC%20user%20Herman%20L%0A%0Ahttps%3A%2F%2Fcodegolf.stackexchange.com%2Fa%2F165448%2F101522&inputs=0)





















<!--

There are no Easter Eggs in this repository.
































There really are no Easter Eggs in this repository.






























Didn't I already tell you that there are no Easter Eggs in this repository?















































Stop it!














































Okay, okay, if I give you an Easter Egg, will you go away?



































































All right, you win.

                               /----\
                       -------/      \
                      /               \
                     /                |
   -----------------/                  --------\
   ----------------------------------------------






















































































What is it?  It's an elephant being eaten by a snake, of course. -->














































































































































































<!--













































































































































































































































































































































































































































































































We're no strangers to love
You know the rules and so do I
A full commitment's what I'm thinking of
You wouldn't get this from any other guy

[Pre-Chorus]
I just wanna tell you how I'm feeling
Gotta make you understand

[Chorus]
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you

[Verse 2]
We've known each other for so long
Your heart's been aching, but you're too shy to say it
Inside, we both know what's been going on
We know the game, and we're gonna play it
[Pre-Chorus]
And if you ask me how I'm feeling
Don't tell me you're too blind to see

[Chorus]
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you

[Post-Chorus]
Ooh (Give you up)
Ooh-ooh (Give you up)
Ooh-ooh
Never gonna give, never gonna give (Give you up)
Ooh-ooh
Never gonna give, never gonna give (Give you up)
[Bridge]
We've known each other for so long
Your heart's been aching, but you're too shy to say it
Inside, we both know what's been going on
We know the game, and we're gonna play it

[Pre-Chorus]
I just wanna tell you how I'm feeling
Gotta make you understand

[Chorus]
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you



















































































































































































































































































<-- lol
