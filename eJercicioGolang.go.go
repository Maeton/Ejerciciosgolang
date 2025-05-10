package main

import (
	"fmt"
)

func main() {
	var a int
	var b int
	fmt.Println("Ingrese un num: ")
	fmt.Scan(&a)
	for i := 0; i < a; i++ {
		if i%2 == 0 {
			b += i
			fmt.Println(b)

		}
	}
}
