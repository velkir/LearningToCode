import random

def random_prefix(string):
    if isinstance(string, str) and string:
        prefixes = ["Wow", "Amazing", "Incredible", "Super", "Bravo"]
        return f"{random.choice(prefixes)} {string}"
    return "Please provide a non-empty string."

def add_closing_bracket(string):
    if isinstance(string, str) and string:
        return string.rstrip(".") + ")"
    return "Please provide a non-empty string."

def keyword_filter(string):
    if "example" in string.lower() and "2025" in string:
        return "Keyword found!"
    return string