Syracuse = int(input());
test = 0;
i=0;

while test ==0:
    print(Syracuse)
    if (Syracuse%2) == 0:
        Syracuse = Syracuse/2;
        i+=1;
    else:
        if Syracuse == 1:
            test=1;
        else:
            Syracuse = (Syracuse*3)+1;
            i+=1;

print("Sa a fait",i,"ittération");