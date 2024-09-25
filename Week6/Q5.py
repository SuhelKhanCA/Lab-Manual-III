def read_from_file(filename):

    try:
        with open(filename, 'r') as file:
            print("Roll Number, Name, Marks")
            print("-------------------------")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    read_from_file("C:\\Users\\hp\\Documents\\Suhel\\3rd - Sem\\Lab-Manual-III\\Week6\\Marks.data")

if __name__ == "__main__":
    main()
