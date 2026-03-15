from functions.write_file import write_file

def tester(working_directory, file_path, content):
    print(f'Testing write_file.py with the following parameters: working dir : {working_directory} , file_path: {file_path}, conent: {content}')
    print(write_file(working_directory,file_path,content))


def main():
    tester("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    tester("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    tester("calculator", "/tmp/temp.txt", "this should not be allowed")

main()