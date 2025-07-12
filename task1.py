try:
    with open("sample.txt","r") as file:
        print("Reading file content:")
        for idx,line in enumerate(file,1):
            print(f"Line {idx}: {line.strip()}")
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")