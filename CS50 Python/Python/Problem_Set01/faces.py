def emoji(str):
    return str.replace(":)", "🙂").replace(":(", "🙁")

string = input("")
print(emoji(string))