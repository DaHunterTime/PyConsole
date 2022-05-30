from pyconsole import install_errors, RGB


def test_func(x: int, y: int) -> tuple[int, float]:
    power: int = x ** y
    div = x / y
    return power, div


def error_test():
    install_errors(color_mode=RGB, show_locals=True)

    x = 3
    y = 0
    text = f"The values of {x}^{y} and {x}^{y} are:"
    print(text, test_func(x, y))


if __name__ == "__main__":
    error_test()
