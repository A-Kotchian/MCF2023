



giorni=["domenica","lunedi","martedi","mercoledi","giovedi","venerdi","sabato"]
ott=[]
f=0
i=0
for i in range(1,32):
  
    match f:
        case 0:
            ott.append(giorni[f])
            f=f+1
            
        case 1:
            ott.append(giorni[f])
            f=f+1
        case 2:
            ott.append(giorni[f])
            f=f+1
        case 3:
            ott.append(giorni[f])
            f=f+1
        case 4:
            ott.append(giorni[f])
            f=f+1
        case 5:
            ott.append(giorni[f])
            f=f+1
        case default:
            ott.append(giorni[f])
            f=0
print(ott)
print(len(ott))


d={}
f=0
for p in range(1,32):

    #d[ott[p-1]]=p

    match f:
        case 0:
            d[p]=ott[f]
            f=f+1

            
        case 1:
            d[p]=ott[f]
            f=f+1
        case 2:
            d[p]=ott[f]
            f=f+1
        case 3:
            d[p]=ott[f]
            f=f+1
        case 4:
            d[p]=ott[f]
            f=f+1
        case 5:
            d[p]=ott[f]
            f=f+1
        case default:
            d[p]=ott[f]
            f=0


 
print("\n================================\n")
print("\nCalendario di ottobre\n")
for i in range(1,32):
    print("{:} - {:}".format(i,d[i]))

print("\n================================\n")


