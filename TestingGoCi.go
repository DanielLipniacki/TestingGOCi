package main

import "fmt"

func Add(x, y int) int {
	return x + y
}

func SecondAdd(x, y int) int {
	return x + y
}

func Multiply(x, y int) int {
	return x * y
}

func Big(x int) int {
	y := x * x * x
	return y
}

func Unused() string {
	return "Oh"
}

func main() {
	fmt.Println("Hello World")
}
