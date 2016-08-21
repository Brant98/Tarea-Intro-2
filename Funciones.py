def rating(id_pelicula):
    usuarios=0
    suma_rating=0
    arch=open('ratings.dat')
    for linea in arch:
        linea=linea.strip().split("::")
        if linea[1]==id_pelicula:
            suma_rating+=float(linea[2])
            usuarios+=1
    arch.close()
    return round((suma_rating/usuarios),1)

print rating('122')
