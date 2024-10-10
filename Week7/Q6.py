def swap_lines(file1_path, file2_path):

    with open(file1_path, 'r') as file1:
        lines1 = file1.readlines()

    with open(file2_path, 'r') as file2:
        lines2 = file2.readlines()
    
    if len(lines1) % 2 == 0:
        print("The first file must contain an odd number of lines.")
        return
    

    middle_index = len(lines1) // 2
    middle_line = lines1[middle_index].strip()
    

    last_line = lines2[-1].strip()

    lines1[middle_index] = last_line + '\n'
    lines2[-1] = middle_line + '\n'

    with open(file1_path, 'w') as file1:
        file1.writelines(lines1)
    
    with open(file2_path, 'w') as file2:
        file2.writelines(lines2)

    print("Lines swapped successfully.")
    print(f"Middle line of file 1 swapped with last line of file 2.")


file1_path = 'file1.txt' 
file2_path = 'file2.txt'

swap_lines(file1_path, file2_path)
