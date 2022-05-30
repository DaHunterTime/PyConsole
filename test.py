from tests.password_test import password_test
from tests.box_test import box_test
from tests.error_test import error_test


def main():
    tests = {
        "password_test": password_test,
        "box_test": box_test,
        "error_test": error_test
    }

    print(
        "===============\n"
        "Select a test:\n"
        "===============\n"
        "- password test\n"
        "- box test\n"
        "- error test\n"
        "===============\n"
    )

    test = "_".join(input().split())
    print()
    selected = tests.get(test, None)

    if selected:
        selected()
    else:
        print("The chosen test does not exist")


if __name__ == "__main__":
    main()
