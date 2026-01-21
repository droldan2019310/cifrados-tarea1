ASCII = {
    " ": 32,
    "!": 33,
    ",": 44,
    ".": 46,
    "?": 63,
    ":": 58,
    ";": 59,
    "-": 45,
    "_": 95,
    "0": 48, "1": 49, "2": 50, "3": 51, "4": 52,
    "5": 53, "6": 54, "7": 55, "8": 56, "9": 57,
}

for i, ch in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    ASCII[ch] = 65 + i
for i, ch in enumerate("abcdefghijklmnopqrstuvwxyz"):
    ASCII[ch] = 97 + i


def a_binario_8bits(n: int) -> str:
    bits = []
    for _ in range(8):
        bits.append(str(n % 2))
        n //= 2
    return "".join(reversed(bits))


def ascii_a_binario(texto: str, separador: str = " ") -> str:
    salida = []
    for c in texto:
        if c not in ASCII:
            raise ValueError(f"Carácter no soportado: {repr(c)}")
        salida.append(a_binario_8bits(ASCII[c]))
    return separador.join(salida)


def main():
    texto = input("Ingresa el texto: ")
    print("\nBinario (8 bits por carácter):")
    try:
        print(ascii_a_binario(texto))
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
