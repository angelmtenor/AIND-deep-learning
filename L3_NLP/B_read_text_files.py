"""Text input functions."""
import os
import glob


def read_file(filename):
    """Read a plain text file and return the contents as a string."""
    # Open "filename", read text and return it
    with open(filename, 'r') as f:
        text = f.read()
    return text


def read_files(path):
    """Read all files that match given path and return a dict with their contents."""

    # Get a list of all files that match path (hint: use glob)
    files = glob.glob(path)

    my_dict = dict()

    # Read each file using read_file()
    for file in files:
        content = read_file(file)

        # Store & return a dict of the form { <filename>: <contents> }
        filename = os.path.basename(file)
        my_dict[filename] = content
    # Note: <filename> is just the filename (e.g. "hieroglyph.txt") not the full path ("data/hieroglyph.txt")

    return my_dict


def example():
    # Test read_file()
    print(read_file("data/input.txt"))

    # Test read_files()
    texts = read_files("data/*.txt")
    for name in texts:
        print("\n***", name, "***")
        print(texts[name])


if __name__ == '__main__':
    example()
