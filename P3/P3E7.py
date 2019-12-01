dd=int(input("Introduce el dia"))
mm=int(input("Introduce el mes"))
aa=int(input("Introduce el año"))
if dd<1 or mm<1 or mm>12 or aa<0 or dd>31:
    print("La fecha %d/%d/%d esta mal" %(dd,mm,aa))
else:
    if (mm==4 or mm==6 or mm==9 or mm==11) and dd<=30:
        print("La fecha %d/%d/%d esta bien" %(dd,mm,aa))
    elif mm==2:
        if (dd<1 or dd>28):
            print("La fecha %d/%d/%d esta mal" %(dd,mm,aa))
        else:
            print("La fecha %d/%d/%d esta bien" %(dd,mm,aa))
    else:
        print("La fecha %d/%d/%d esta bien" %(dd,mm,aa))
