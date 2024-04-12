temperaturas = [-10, -8, 0, 1, 2, 5, -2, -4]  

print(f"Levando em consideração as temperaturas da lista: {temperaturas}, observe a seguir.\n")

menor_temperatura = min(temperaturas)
print(f"A menor temperatura em Mons é {menor_temperatura}°C.")

maior_temperatura = max(temperaturas)
print(f"A maior temperatura em Mons é {maior_temperatura}°C.")

soma_temperaturas = sum(temperaturas)
media_temperaturas = soma_temperaturas / len(temperaturas)
print(f"A temperatura média em Mons é {media_temperaturas:.1f}°C.")
