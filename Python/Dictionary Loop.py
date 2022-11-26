def open_or_senior(data):
    output = []
    for x,y in evaluation.items():
        if x >= 55 and y > 7:
            output.append("Senior")
        else:
            output.append("Open")

    print(output)
    
evaluation = {0:-1,1:4,2:10,109:-2,88:3,90:9,101:20}
open_or_senior(evaluation)