import sys
import re

def get_function_source(file_path, function_name):
    """
    Returns the source code of the specified function from a given file, attempting to respect Python indentation.

    Args:
    - file_path: The path to the Python file.
    - function_name: The name of the function whose source code is to be retrieved.

    Returns:
    - A string containing the source code of the function, or
    - None if the function cannot be found.
    """
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Start building the pattern to identify the function start
        pattern = rf"def {function_name}\(.*?\):"
        function_code = []
        capture = False
        for line in lines:
            if re.match(pattern, line):
                capture = True
            elif capture and (line.startswith(' ') or line.startswith('\t')):
                pass
            elif capture and line.strip() == "":
                pass
            else:
                if capture:
                    break
            if capture:
                function_code.append(line)

        if function_code:
            return ''.join(function_code)
        else:
            print(f"Function {function_name} not found in file {file_path}.")
            return None
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py file_path function_name")
    else:
        file_path = sys.argv[1]  # The file path is the first argument
        function_name = sys.argv[2]  # The function name is the second argument
        source_code = get_function_source(file_path, function_name)
        if source_code:
            print("Function source code:\n", source_code)
