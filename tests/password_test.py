from pyconsole import Console, RGB


def password_test():
    console = Console(color_mode=RGB)
    password = console.getpass()
    print(f"Entered password: {password}")

    assert isinstance(password, str)


if __name__ == "__main__":
    password_test()
