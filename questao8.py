def somar_vet(vet):
    if len(vet)==1:
        return vet[0]
    else:
        return vet[0]+somar_vet(vet[1:])
print (somar_vet([1,2,3,4,5]))