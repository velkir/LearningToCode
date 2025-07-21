import random

def tourette(string):
    if type(string) == str and len(string)>0:
        swearings = ["FUCK", "FUCK YOU", "BITCH", "ASSHOLE", "COCKSUCKER"]
        swearing = random.choice(swearings)
        return f"{swearing} {string}"
    else:
        return ("Please provide a non-empty string.")
        

def cis_region_end_bracket(string):
    if type(string) == str and len(string)>0:
        if string[-1]==".":
            return string[:-1]+")"
        else:
            return string+")"
    else:
        return ("Please provide a non-empty string.")

def nothing_happened_in_tiananmen_in_1989(string):
    if "tiananmen" in string.lower() and "1989" in string:
        return "China is Number 1!"
    else:
        return string

