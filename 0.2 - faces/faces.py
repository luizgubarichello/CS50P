def main():
    phrase = input()
    print(convert(phrase))


def convert(param):
    phrase = param.replace(":)","🙂")
    phrase = phrase.replace(":(","🙁")
    return phrase

main()