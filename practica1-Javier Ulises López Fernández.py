import os
c=1
onHost=0
while c<255:
    hostname="200.33.171."
    respuesta=os.system("ping "+hostname+str(c))
    if respuesta==0:
        print(hostname+str(c)+": está en funcionamiento!")
        onHost=onHost+1

    else:
        print(hostname+str(c)+": No está en funcionamiento")
    c=c+1


print("Existen: "+str(onHost)+" Hosts en funcionamiento en el ITM.")