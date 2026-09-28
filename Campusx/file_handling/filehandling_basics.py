
def write_to_file_without_newLine():
    f= open("sample.txt","w")
    f.write("Hello, World!")
    f.write(" This is a sample text file.")
    f.close()


def write_to_file_with_newLine():
    "the old file will be overwritten"
    f= open("sample.txt","w")
    f.write("Hello, World!")
    f.write("\nThis is a sample text file.")
    f.close()

def append_to_file():
    f= open("sample.txt","a")
    f.write("\nThis is an appended line.")
    f.close()

def write_multiple_lines_to_file():
    f= open("sample.txt","w")
    lines = ["Line 1: Hello, World!", "Line 2: This is a sample text file.", "Line 3: Writing multiple lines."]
    f.writelines(line + "\n" for line in lines)
    f.close()

def read_from_file():
    f= open("sample.txt","r")
    content= f.read()
    print(content)
    f.close()

def read_lines_from_file():
    f= open("sample.txt","r")
    while True:
        line = f.readline()
        if not line:
            break
        print(line, end="")
    f.close()

def using_with_statement():
    "when using with statement, we dont need to close the file explicitly"
    with open("sample.txt","w") as f:
        f.write("Hello, World!")
        f.write("\nThis is a sample text file.") 

def create_file_big():
    with open("bigfile.txt","w") as f:
        f.write("hello world\n" * 1000000)

def read_big_file_in_chunks():
    chunk_size= 10
    with open("bigfile.txt","r") as f:
        while True:
            chunk= f.read(chunk_size)
            if not chunk: # empty string returns true Length > 0 → true, not chunk-> true if length is 0
                break
            print (chunk, end="")

def bool_conditions():
    chunk= "hello"
    print(bool(chunk) == (len(chunk) > 0))
    print(bool(not chunk) == (len(chunk) == 0))
    print(not chunk == (len(chunk) == 0))

# write_to_file_without_newLine()
# write_to_file_with_newLine()
# append_to_file()
# write_multiple_lines_to_file()
# read_from_file()
# read_lines_from_file()
# using_with_statement()
create_file_big()