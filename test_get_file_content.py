from functions.get_file_content import get_file_content

def tester(working_dir, file_path):
    content = get_file_content(working_dir , file_path)

    content_lenght = len(content)

    trurncated_section = content[10000:]

    print(f"testing {working_dir} , {file_path}")

    print(f"Content Lenght = {content_lenght}")

    if trurncated_section:

        print (f"Trurncated_section found!: {trurncated_section}")




def main():
    
    tester("calculator", "lorem.txt")
    tester("calculator", "pkg/calculator.py")

    print(get_file_content("calculator", "main.py"))
    print(get_file_content("calculator", "pkg/calculator.py"))

    print(get_file_content("calculator", "/bin/cat"))
    print(get_file_content("calculator", "pkg/does_not_exist.py"))



main()