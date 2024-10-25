#!/bin/bash

echo "Enter a positive integer:"
read number

factorial=1

for (( i=1; i<=number; i++ ))
do
  factorial=$((factorial * i))
done

echo "The factorial of $number is $factorial."
