B64_ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def limpiar_binario(b: str) -> str:
    b = b.replace(" ", "").replace("\n", "").replace("\t", "")
    if any(ch not in "01" for ch in b):
        raise ValueError("El binario solo puede contener 0 y 1.")
    if len(b) == 0:
        return ""
    if len(b) % 8 != 0:
        raise ValueError("La cantidad de bits debe ser múltiplo de 8.")
    return b


def binario_a_bytes(bin_str: str) -> list[int]:
    bytes_out = []
    for i in range(0, len(bin_str), 8):
        byte_bits = bin_str[i:i+8]
        valor = 0
        for bit in byte_bits:
            valor = (valor << 1) | (1 if bit == "1" else 0)
        bytes_out.append(valor)
    return bytes_out


def bytes_a_base64(data: list[int]) -> str:
    res = []
    i = 0
    while i < len(data):
        bloque = data[i:i+3]
        i += 3
        padding = 3 - len(bloque)
        while len(bloque) < 3:
            bloque.append(0)

        b0, b1, b2 = bloque
        triple = (b0 << 16) | (b1 << 8) | b2

        idx0 = (triple >> 18) & 0b111111
        idx1 = (triple >> 12) & 0b111111
        idx2 = (triple >> 6)  & 0b111111
        idx3 = triple & 0b111111

        res.append(B64_ALFABETO[idx0])
        res.append(B64_ALFABETO[idx1])


        if padding == 2:
            res.append("=")
            res.append("=")
        elif padding == 1:
            res.append(B64_ALFABETO[idx2])
            res.append("=")
        else:
            res.append(B64_ALFABETO[idx2])
            res.append(B64_ALFABETO[idx3])

    return "".join(res)


def binario_a_base64(binario: str) -> str:
    bin_limpio = limpiar_binario(binario)
    if bin_limpio == "":
        return ""
    data = binario_a_bytes(bin_limpio)
    return bytes_a_base64(data)



def base64_a_bytes(b64: str) -> list[int]:
    b64 = b64.replace("\n", "").replace(" ", "")
    if len(b64) % 4 != 0:
        raise ValueError("Longitud de Base64 inválida (debe ser múltiplo de 4).")
    
    bytes_out = []
    i = 0
    while i < len(b64):
        bloque = b64[i:i+4]
        i += 4
        
        # Encodings de los 4 caracteres
        vals = []
        for char in bloque:
            if char == "=":
                vals.append(0)
            elif char in B64_ALFABETO:
                vals.append(B64_ALFABETO.index(char))
            else:
                raise ValueError(f"Carácter inválido en Base64: {char}")
        
        idx0, idx1, idx2, idx3 = vals
        
        triple = (idx0 << 18) | (idx1 << 12) | (idx2 << 6) | idx3
        
        b0 = (triple >> 16) & 0xFF
        b1 = (triple >> 8) & 0xFF
        b2 = triple & 0xFF
        
        bytes_out.append(b0)
        
        # Manejo de padding para no agregar bytes extra
        if bloque[2] != "=":
            bytes_out.append(b1)
        if bloque[3] != "=":
            bytes_out.append(b2)
            
    return bytes_out


def bytes_a_binario(data: list[int]) -> str:
    res = []
    for byte in data:
        # Convertir a binario 8 bits
        bin_8 = bin(byte)[2:].zfill(8)
        res.append(bin_8)
    return "".join(res)


def base64_a_binario(b64: str) -> str:
    data = base64_a_bytes(b64)
    return bytes_a_binario(data)


def main():
    print("Seleccione una opción:")
    print("1. Binario -> Base64")
    print("2. Base64 -> Binario")
    opcion = input("> ")

    if opcion == "1":
        b = input("Ingresa el binario (8 bits por byte, con o sin espacios):\n> ")
        try:
            print("\nBASE64:")
            print(binario_a_base64(b))
        except ValueError as e:
            print("Error:", e)
    elif opcion == "2":
        b64 = input("Ingresa la cadena Base64:\n> ")
        try:
            print("\nBINARIO:")
            print(base64_a_binario(b64))
        except ValueError as e:
            print("Error:", e)
    else:
        print("Opción no válida.")


if __name__ == "__main__":
    main()
