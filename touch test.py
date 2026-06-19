open -a "Visual Studio Code" test.py
print("Hello Hacker")
print("Welcome to the world of coding!")
print("This is a simple Python script.")
print("You can run this script to see the output.")
print("Feel free to modify the code and experiment with it.")
print("Happy coding!")  
name = "Anurag"
age = 27

print("My name is", "anurag kumar")
print("My age is", 27)
name = input("anurag kumar: ")
print("Hello","anurag kumar")
for i in range(5):
    print("Hacking Level", i)
    age = int(input("27: "))

if age >= 18:
    print("Adult")
else:
    print("Minor")
    import socket

target = "127.0.0.1"

for port in range(1, 100):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((target, port))

    if result == 0:
        print("Port open:", port)

    sock.close()
    
