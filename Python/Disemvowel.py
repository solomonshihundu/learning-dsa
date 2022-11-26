def disemvowel(string_):
    vowels = ['a','e','i','o','u']
    for x in string_:
        if x.lower() in vowels:
            string_ = string_.replace(x,"")

    return string_

input = "This website is for losers LOL!"
print(disemvowel(input))


#################################################################################################
# BEST PRACTISE
#################################################################################################
def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou")