hello = open("my_file.txt","w")
hello.write("Hello stanley welcome to plp\nYour admission number is 8112\nyour adventure awaits you\n")

hello.close()

hello = open("my_file.txt","r")
f = hello.read()
print(f)
hello.close()

with open("my_file.txt","a+") as hi :
    hi.write("\nHere is a list of your courses\n 1.python\n 2.C++\n3.Javascript")


# Writing to the file
try:
    hello = open("my_file.txt", "w")
    hello.write("Hello Stanley, welcome to PLP\nYour admission number is 8112\nyour adventure awaits you\n")
except PermissionError:
    print("Permission denied: Unable to write to 'my_file.txt'.")
except Exception as e:
    print(f"An unexpected error occurred while writing to the file: {e}")
finally:
    try:
        hello.close()
    except NameError:
        pass  # 'hello' was never successfully created/opened

# Reading from the file
try:
    hello = open("my_file.txt", "r")
    f = hello.read()
    print(f)
except FileNotFoundError:
    print("File not found: 'my_file.txt' does not exist.")
except PermissionError:
    print("Permission denied: Unable to read 'my_file.txt'.")
except Exception as e:
    print(f"An unexpected error occurred while reading the file: {e}")
finally:
    try:
        hello.close()
    except NameError:
        
        pass  # 'hello' was never successfully created/opened

# Appending to the file
try:
    with open("my_file.txt", "a+") as hi:
        hi.write("\nHere is a list of your courses\n 1. Python\n 2. C++\n 3. Javascript")
except FileNotFoundError:
    print("File not found: 'my_file.txt' does not exist.")
except PermissionError:
    print("Permission denied: Unable to append to 'my_file.txt'.")
except Exception as e:
    print(f"An unexpected error occurred while appending to the file: {e}")
