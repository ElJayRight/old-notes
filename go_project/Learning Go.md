(tots not for google job or anything :eyes:)

# Create a work env.
Vscode plugin: [link](https://code.visualstudio.com/docs/languages/go)

Have to install go binary [link](https://go.dev/dl/)

Create a quick hello world program.

```go
// https://gobyexample.com/play.png "Run code")](https://go.dev/play/p/NeviD0awXjt)![](https://gobyexample.com/clipboard.png "Copy code")

package main

import "fmt"

func main() {
    fmt.Println("hello world")
}
```

Windows is being dumb going to use linux cause it will work.

Can also then use github.

On linux install it with apt.

Then to run the program.
```bash
go run simpleprogram.go
```

To build the program and then run it 
```bash
go build simpleprogram.go
./simpleprogram
```

# Making a git thing.
I think it's set up?

# Guessing game
## What will I learn
User input, random numbers, if statements, logical comparisons, For loops.

## the code bit.
Need fmt import for stdout.

Adding all the output (only thing I know how to do for now.)
```go
import "fmt"
  
func main() {
	fmt.Println("Guessing Game\nGuess a number between 1 and 100.")
	//input
	//if correct guess
	fmt.Println("Correct!")
	//if lower
	fmt.Println("Lower")
	//if higher
	fmt.Println("Higher")
	  
	//reguess
	fmt.Println("Guess again.")
}
```

Should add the if statement.

Also all the code examples I see have `package main` at the top so I should probs also have that?

Oh need to know how to declare variables first.

There are two ways.
```go
var <name> <type>
<name> = <value>
```

or 

```go
<var> := <value>
```

I'm using the second option cause, its quicker.

Adding a stub for the guess and the if logic, I have this.

```go
package main

import "fmt"

func main() {
	fmt.Println("Guessing Game\nGuess a number between 1 and 100.")
	//input
	number := 77
	guess := 7
	//if correct guess
	if guess == number {
		fmt.Println("Correct!")
	} else if guess > number{
		fmt.Println("Lower")
	} else if guess < number{
		fmt.Println("Higher")
	}
	//reguess
	fmt.Println("Guess again.")
}
```

All that is left is user input and a loop.

User input. `scanln()` seems to be what i want.

The loop is very similar to python.
```go
for initialization; condition; update {
  statement(s)
}
```

Bunch of errors for scanln(). First it is `fmt.Scanln()`

Oh so its `fmt.Scanln(&guess)` not `guess = fmt.Scanln()`.

Finally the rng bit.
`rand.Intn(100)`

```go
package main

import (
	"fmt"
	"math/rand"
	"os"
	"time"
)

func main() {
	fmt.Println("Guessing Game\nGuess a number between 1 and 100.\nYou get 5 tries.")
	//input
	var guess int
	s1 := rand.NewSource(time.Now().UnixNano())
    r1 := rand.New(s1)
	number := r1.Intn(100)
	//if correct guess
	for i:=1; i!=6; i++ {
		fmt.Print("Enter a number: ")
		fmt.Scanln(&guess)
		if guess == number {
			fmt.Println("Correct!\n")
			os.Exit(1)
		} else if guess > number{
			fmt.Print("Lower, ")
		} else if guess < number{
			fmt.Print("Higher, ")
		}
		//reguess
		fmt.Println("guess again.")
	}
	fmt.Println("rip you ran out of guesses. :(")
}
```

There is no form of error catching or anything. Entering a string will break it so dont do that.

# Sudoku
*small jump*

Going to do the "check each row" feature.

Lists in go.
```go
var <name> [<size>]<type>
var row [9]int
```

The way I would normally do this in python would just be to compare it to itself as a set, which will remove duplicates. The go version of this is to make a map.

```go
visited := []visit{
    visit{1, 100},
    visit{2, 2},
    visit{1, 100},
    visit{1, 1},
}
unique := map[visit]bool{}

for _, v := range visited {
    unique[v] = true
}

fmt.Println(unique)
```

My implementation;
```go
func check(row [9]int) {
	set :=map[int]bool{}
	for _,value := range row{
		set[value] = true
	}
	if len(set) == len(row){
		fmt.Println("UNIQUE")
	} else {
		fmt.Println("Not unique")
	}
}
```

Changing the flags to be true and false. 

## Board generation
First major design implementation I need to consider. Should I generate the board by rows or squares. As they both need to be checked, I'm going to do it all as one big array. (This is going to be painful.)

This will generate the grid in this layout.
```txt
0  1  2  3  4  5  6  7  8
9  10 11 12 13 14 15 16 17
18 19 20 21 22 23 24 25 26
27 28 29 30 31 32 33 34 35
36 37 38 39 40 41 42 43 44
45 46 47 48 49 50 51 52 53
54 55 56 57 58 59 60 61 62
63 64 65 66 67 68 69 70 71
72 73 74 75 76 77 78 79 70
```

Using python list syntax, idk the go one.

```python
[list[n*9:n*9+9] for n in range(0,9)] # for left to right
[list[n::9] for n in range(0,9)] # for up and down
#squares are weird.
0,1,2,9,10,11,18,19,20
0-2, 9-11, 18-20

list[0:3],list[9:12],list[18:21]
# I think the indices are right? the idea is tho.
list[n:n+3] for n in [0,9,18]

[list[n*9:n*9+3] for n in range(0,3)] # each grid


'''
They start at
0 , 3 , 6 ,
27, 30, 33,
54, 57, 60
'''
[k*[n*27 for n in range(3)] for k in range(3)] # (ew) or something like this.

for i in range(0,3):
	for k in range(0,3):
		offset = i*27 + k*3
		[list[n*9+offset:n*9+3+offset] for n in range(0,3)]
```

This better work. Going to make a second function to generate the rows, cols, and squares.

Make the grid above in a list using python (is this cheating?)
```python
print(set([i for i in range(81)]))

{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80}
```

I basically have to do this later in go so, I'll learn how to do this eventually.

Had a few errors:
```go
# command-line-arguments
./sudoku.go:7:2: undefined: grid
./sudoku.go:8:31: undefined: grid
./sudoku.go:17:10: too many return values
	have (bool)
	want ()
./sudoku.go:19:10: too many return values
	have (bool)
	want ()
```

Last two are the same so fixing them first. Turns out you need a return type if you are going to return from a function. `func check(row [9]int) bool{`

The first one is cause I used `=` instead of `:=` *python habits die hard*

Turns out I still dont use python loops properly, but this is go so I can fix that off the bat.
```go
func generate_chunk_to_be_checked(grid [81]int){
	for i:=0; i!=81; i+=9{
		fmt.Println(grid[i:i+9])
	}
}
```
