def greet(name: str) -> str:
    """
    Returns a greeting message for the given name.
    """
    return f"Hello, {name}! Welcome to the feature."

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet(user_name))