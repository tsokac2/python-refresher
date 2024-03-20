def sentenc_maker(phrase):
    interrogatives = ("how","what","why")
    caps = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(caps)
    else:
        return "{}.".format(caps)
    
print(sentenc_maker("how are you"))


results = []
while True:
    user_input = input("Say something: ")
    if user_input == "\end":
        break
    else:
        results.append(sentenc_maker(user_input))

print(" ".join(results))


