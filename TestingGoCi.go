package main

import "fmt"

func Add(x, y int) int {
	return x + y + x
}

func SecondAdd(x, y int) int {
	return x + y + y
}

func Multiply(x, y int) int {
	return x * y
}

func Unused() string {
	return "oh"
}

func main() {
	fmt.Println("Hello World")
}
