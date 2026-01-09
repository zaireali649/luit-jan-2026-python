# ----------------------------
# Importing standard libraries
# ----------------------------

import random      # Used for generating random numbers
import math        # Used for mathematical operations
import os          # Used for interacting with the operating system
import sys         # Used for interacting with the Python runtime
import matplotlib.pyplot as plt  # Used for plotting graphs


# ----------------------------
# Random numbers
# ----------------------------

# Generate a random integer between 1 and 10
number = random.randint(1, 10)
print("Random number:", number)


# ----------------------------
# Math operations
# ----------------------------

# Calculate the square root of the number
square_root = math.sqrt(number)
print("Square root:", square_root)

# Calculate the factorial (only works for whole numbers)
factorial = math.factorial(number)
print("Factorial:", factorial)


# ----------------------------
# OS information
# ----------------------------

# Get the current working directory
current_directory = os.getcwd()
print("Current directory:", current_directory)

# List files in the current directory
files = os.listdir(current_directory)
print("Files in directory:", files)


# ----------------------------
# Sys information
# ----------------------------

# Show the Python version
print("Python version:", sys.version)

# Show command-line arguments (usually empty for beginners)
print("Command-line arguments:", sys.argv)


# ----------------------------
# Matplotlib example
# ----------------------------

# Create some data to plot
x_values = list(range(1, 11))
y_values = [math.sqrt(x) for x in x_values]

# Plot the data
plt.plot(x_values, y_values)
plt.title("Square Root of Numbers 1 to 10")
plt.xlabel("Number")
plt.ylabel("Square Root")

# Display the plot
plt.show()
