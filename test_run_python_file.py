from functions.run_python_file import run_python_file

def tester(working_directory, file_path, args=None):

    print(f'Testing run_python_file.py using these inputs: working_director = {working_directory}, file_path = {file_path}, args = {args} ...')
    print(run_python_file(working_directory, file_path, args))


def main():
    tester("calculator", "main.py")
    tester("calculator", "main.py", ["3 + 5"])
    tester("calculator", "tests.py")
    tester("calculator", "../main.py")
    tester("calculator", "nonexistent.py")
    tester("calculator", "lorem.txt")

main()