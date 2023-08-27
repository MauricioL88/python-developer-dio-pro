a = 5000
b = 10000
tx_a = 0.1
tx_b = 0.05
ano_a = 0

while a < b:
    a = a + (a * tx_a)
    ano_a = ano_a + 1
    b = b + (b * tx_b)
    
print(f"A cidade A levou {ano_a} anos para ultrapassar a cidade B em população.")
print(f"Depois de {ano_a} anos.")
print(f"População da cidade A passa a ter: {a:.0f} pessoas.")
print(f"População da cidade B passa a ter: {b:.0f} pessoas.")
