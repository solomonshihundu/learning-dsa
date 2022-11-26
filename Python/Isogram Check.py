def is_Isograms(string):
    str = string.lower()
    for i in iter(str):
        if str[i] == str[i+1]:
            return False
        return True

string= "aba"
#string= "isogram"
#string= "moOse"

is_Isograms(string)