from pathlib import Path
from file_handler import FileHandler

def test_file_handler():
    test_file = Path("test_file.txt")
    test_content = "This is a test content."

    # Test writing to a file
    FileHandler.write_file(test_file, test_content)
    print(f"File written: {test_file}")

    # Test reading the file
    read_content = FileHandler.read_file(test_file)
    print(f"Read content: {read_content}")

    # Validate content
    assert read_content == test_content, "File content does not match!"

    # Clean up
    test_file.unlink()
    print("Test file removed.")

if __name__ == "__main__":
    test_file_handler()
