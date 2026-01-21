import string

ABC_LOWER = string.ascii_lowercase
ABC_UPPER = string.ascii_uppercase

def caesar(text: str, shift: int) -> str:
    """shift > 0 derecha, shift < 0 izquierda. Mantiene espacios/saltos/etc."""
    out = []
    for ch in text:
        if ch in ABC_LOWER:
            i = ABC_LOWER.index(ch)
            out.append(ABC_LOWER[(i + shift) % 26])
        elif ch in ABC_UPPER:
            i = ABC_UPPER.index(ch)
            out.append(ABC_UPPER[(i + shift) % 26])
        else:
            out.append(ch)
    return "".join(out)

def score_spanish(s: str) -> int:
    """Puntaje simple: palabras comunes + letras frecuentes en español."""
    s2 = s.lower()
    common = [
        " bienvenidos", " cifrados", " de ", " la ", " que ", " el ", " en ", " y ", " a ", " los ", " del "
    ]
    score = 0
    score += sum(50 for w in common if w in s2)   # palabras = mucho peso
    score += sum(s2.count(ch) for ch in "aeionrsldt")  # letras frecuentes
    return score

def brute_force_caesar(ciphertext: str, top: int = 10):
    """
    Prueba 0..25 como 'izquierda k' y devuelve los mejores resultados.
    """
    results = []
    for k in range(26):
        plain = caesar(ciphertext, -k)  # izquierda k
        results.append((k, plain, score_spanish(plain)))

    results.sort(key=lambda x: x[2], reverse=True)

    for k, plain, _ in results[:top]:
        print(f"izquierda {k:2d}: {plain}")

    return results

cipher = "krnwenwrmxb\nj\nlroajmxb\n"
brute_force_caesar(cipher, top=10)
