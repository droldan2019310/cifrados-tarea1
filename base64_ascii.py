
import base64_binary
import binary_ascii

def base64_a_ascii(b64_str: str) -> str:
    # Base64 -> Binario
    binario = base64_binary.base64_a_binario(b64_str)
    # Binario -> ASCII
    texto = binary_ascii.binario_a_ascii(binario)
    return texto

def main():
    b64 = input("Ingresa la cadena Base64:\n> ")
    try:
        resultado = base64_a_ascii(b64)
        print("\nResultado ASCII:")
        print(resultado)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()
