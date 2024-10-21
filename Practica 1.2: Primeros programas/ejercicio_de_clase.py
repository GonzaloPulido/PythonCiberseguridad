precios:dict [str, float] = {
    "Platano":1.35, 
    "Manzana":0.80, 
    "Pera":0.85, 
    "Naranja":0.70}

def precio_total(cantidad:float, precio:float) -> float:
    return cantidad*precio

def precio_fruta(fruta:str)->float:
    return precios[fruta]


if __name__ == "__main__":
    print("Fruteria Refaelito\n")
    print("Frutas del dia")
    for fruta in precios.items():
        print(f"{fruta[0]}: cuesta {fruta[1]}")

    while True:
        print("Que quieres Mari?: ")
        pedido = input()
        if pedido not in precios.keys():
            print("Mari, habla bien que no te entiendo")
            continue
        print("Cuantos kilos?")

        while True:
            try:
                cantidad:float = float(input())
                break
            except ValueError:
                print("Solo valen numeros")
                #continue

        print(f"{cantidad} kgs de {pedido} son {precio_total(cantidad, precio_fruta(pedido))}€")
        print("Gracias Mari, hasta luego")
        break
         
    