import json
import pickle

#Store user input in a list (instead of directly adding it to the file)
data = []

def menu():
    print("function list : "
        "\n1. write something",
          "\n2. output the data stored in the file in the terminal",
          "\nQ. Quit")
    choice = input("choose a function : ")
    return choice

#Add another option to your user interface: The user should be able to output the data stored in the file in the terminal.
def read_data():
    with open("file.txt", mode="r") as f: #mode="rb" for pickle
        global data
        data = f.readlines()
        #data = pickle.loads(f.read())
        for i in data:
            print(data)
            #print(i)
        f.close()

#Adjust the logic to load the file content to work with pickled/ json data.
read_data()

def write_data():
    # Write a short Python script which queries the user for input
    word = input("write something to storage into the file. : ")
    data.append(word)
    # and writes the input to a file.
    # write that list to the file – both with pickle and json.
    with open ("file.txt", mode="a") as f:  #mode="wb" for pickle
        #f.write(word)
        f.write(json.dumps(data))
        #f.write(pickle.dumps(data))
        f.close()


def main():
    choice=""
    # (infinite loop with exit possibility)
    while choice not in ("q", "Q"):
        choice=menu()

        if choice.lower() == "q":
            print("bye!")
            break

        elif choice == "1":
            write_data()

        elif choice == "2":
            read_data()

        else:
            print("fail choice")

main()
