def open_or_senior(data):
    output = []
    for x in data:
        if x[0] >= 55 and x[1] > 7:
            output.append("Senior")
        else:
            output.append("Open")

    print(output)
    
data = [(45, 12),(55,21),(19, -2),(104, 20)]
open_or_senior(data)


###################################################################################
#BEST PRACTISE
###################################################################################
def openOrSenior(data):
  return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]

data = [(45, 12),(55,21),(19, -2),(104, 20)]
print(openOrSenior(data))