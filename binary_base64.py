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


def main():
    b = input("Ingresa el binario (8 bits por byte, con o sin espacios):\n> ")
    try:
        print("\nBASE64:")
        print(binario_a_base64(b))
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
