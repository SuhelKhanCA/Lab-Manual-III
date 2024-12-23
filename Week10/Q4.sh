#!/bin/bash

# Accept two numbers from the user
echo "Enter the first number:"
read num1
echo "Enter the second number:"
read num2

# Perform arithmetic operations
sum=$((num1 + num2))
difference=$((num1 - num2))
product=$((num1 * num2))

# Check for division by zero
if [ "$num2" -ne 0 ]; then
  quotient=$((num1 / num2))
else
  quotient="undefined (division by zero)"
fi

# Display the results
echo "Sum: $sum"
echo "Difference: $difference"
echo "Product: $product"
echo "Quotient: $quotient"
