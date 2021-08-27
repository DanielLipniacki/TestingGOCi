package main

import (
	"bufio"
	"crypto/md5"
	"encoding/hex"
	"fmt"
	"html"
	"image"
	"strings"
)

func createHash(key string) string {
	hasher := md5.New()
	hasher.Write([]byte(key))
	return hex.EncodeToString(hasher.Sum(nil))
}

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
	image.NewAlpha(image.Rect(10, 10, 10, 10))
	v := createHash("ghhhhhhh")
	fmt.Println(v)
	bufio.NewReader(strings.NewReader("Hello, Reader!"))
	html.UnescapeString("<P></P>")
}
