def verificar_letra_a(frase):
    count = frase.lower().count('a')
    
    if count > 0:
        print(f"A letra 'a' aparece {count} vez(es) na frase.")
    else:
        print("A letra 'a' não aparece na frase.")

frase = "Programar!"

verificar_letra_a(frase)
