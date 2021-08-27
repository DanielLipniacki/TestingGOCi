package main

import (
	_ "embed"
	"fmt"
)

func Add(x, y int) int {
	return x + y
}

func SecondAdd(x, y int) int {
	return x + y
}

func Multiply(x, y int) int {
	return x * y
}

func Unused() string {
	return "no"
}

func main() {
	fmt.Println("Hello World")
}
