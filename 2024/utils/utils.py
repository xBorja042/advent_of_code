import sys, os
path = os.path.join(os.path.dirname(__file__), '..')
# sys.path.append(os.path.abspath(path))

def load_input_data(filename="input_file.txt"):
    filename = f"{path}\{filename}"
    print(f"Loading data from {filename}...")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, filename)
    with open(input_file, "r", encoding="utf-8") as f:
        return f.readlines()
