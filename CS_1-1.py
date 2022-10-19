# El primer elemento en el vector debe ser 1 (bias)
# La longitud de w y x debe ser n+1 para una neurona con n inputs

def compute_output(w,x):
    z = 0.0
    for i in range(len(w)):
        z += x[i] * w[i] #sumatoria de inputs ponderadas
        
    if z < 0: #aplicación de la función de activación
        return -1
    return 1