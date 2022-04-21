Premier = int(input("Premier Nombre :" ));
Second = int(input("Second Nombre :" ));
x = 0;
temp = 0;
while Premier !=0:
    temp= temp + 1;
    if Premier % 2 == 1:
        x = x+Second;
    Premier = Premier//2;
    Second += Second;
print(x);
print (temp);


#commentaire