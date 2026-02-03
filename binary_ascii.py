
def binario_a_ascii(bin_str: str) -> str:
    bin_str = bin_str.replace(" ", "").replace("\n", "").replace("\t", "")
    
    if len(bin_str) % 8 != 0:
        raise ValueError("La longitud del binario debe ser múltiplo de 8.")
    
    texto = []
    for i in range(0, len(bin_str), 8):
        byte = bin_str[i:i+8]
        valor = int(byte, 2)
        texto.append(chr(valor))
        
    return "".join(texto)

def main():
    b = input("Ingresa el binario (8 bits por carácter, con o sin espacios):\n> ")
    try:
        resultado = binario_a_ascii(b)
        print("\nResultado ASCII:")
        print(resultado)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()
