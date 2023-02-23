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