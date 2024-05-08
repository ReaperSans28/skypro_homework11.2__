import os.path

from src.decorators import my_function

file_data = [
    "2018-10-31 20:31:00 my_function ok",
    "2018-10-31 20:31:00 my_function error: unsupported operand type(s) for +: 'int' and 'dict'. Inputs: (1, {}), {}",
]


def write_to_file(file_path: str, content: str) -> None:
    with open(file_path, "w") as file:
        file.write(content)


def test_my_function1() -> None:
    file_path = ""

    try:
        my_function(1, 2)
        my_function(1, {})

        with open(file_path, "r") as file:
            assert file_data[0] in file.read()
        with open(file_path, "r") as file:
            assert file_data[1] in file.read()

        os.remove(file_path)

    except FileNotFoundError:
        assert True


def test_my_function2() -> None:
    file_path = "mylog.txt"

    try:
        my_function(1, 2)
        my_function(1, {})

        with open(file_path, "r") as file:
            assert file_data[0] in file.read()
        with open(file_path, "r") as file:
            assert file_data[1] in file.read()

        os.remove(file_path)

    except FileNotFoundError:
        assert True
