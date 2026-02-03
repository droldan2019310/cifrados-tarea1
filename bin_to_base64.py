import binary_base64

def main():
    print("--- Conversor de Binario a Base64 ---")
    b = input("Ingresa el binario (8 bits por byte, con o sin espacios):\n> ")
    try:
        # Reutilizamos la lógica existente
        resultado = binary_base64.binario_a_base64(b)
        print("\nResultado Base64:")
        print(resultado)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
