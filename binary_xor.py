
def xor_binarios(msg_bin: str, key_bin: str) -> str:
    msg = msg_bin.replace(" ", "").replace("\n", "").replace("\t", "")
    key = key_bin.replace(" ", "").replace("\n", "").replace("\t", "")
    
    if not msg or not key:
        raise ValueError("El mensaje y la clave no pueden estar vacíos.")

    if any(c not in "01" for c in msg) or any(c not in "01" for c in key):
        raise ValueError("El mensaje y la clave solo deben contener 0 y 1.")

    res = []
    for i, bit_msg in enumerate(msg):
        bit_key = key[i % len(key)]
        
        if bit_msg == bit_key:
            res.append("0")
        else:
            res.append("1")
            
    return "".join(res)

def main():
    msg = input("Ingresa el MENSAJE en binario:\n> ")
    key = input("Ingresa la CLAVE en binario:\n> ")
    
    try:
        resultado = xor_binarios(msg, key)
        print("\nResultado XOR:")
        print(resultado)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()
