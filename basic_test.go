package main

import "testing"

func TestAdd(t *testing.T) {
	awn := Add(2, 1)
	if awn != 3 {
		t.Errorf("Respone was incorrent, got: %d, want: %s.", awn, "3")
	}
}

func TestSecondAdd(t *testing.T) {
	awn := SecondAdd(2, 1)
	if awn != 3 {
		t.Errorf("Respone was incorrent, got: %d, want: %s.", awn, "3")
	}
}

func TestMultiply(t *testing.T) {
	awn := Multiply(2, 1)
	if awn != 2 {
		t.Errorf("Respone was incorrent, got: %d, want: %s.", awn, "3")
	}
}
