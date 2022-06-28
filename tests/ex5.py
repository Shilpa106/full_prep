string = "Great responsibility";  

for i in range(len(string)):
    for j in range(i+1, len(string)):
        if string[i]==string[j]:
            print(string[i])

