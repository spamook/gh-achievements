import sys


def greet(name: str, excited: bool = False) -> str:
    end = "!" if excited else "."
    return f"Hello, {name}{end}"


if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "GitHub"
    print(greet(name, excited=True))
