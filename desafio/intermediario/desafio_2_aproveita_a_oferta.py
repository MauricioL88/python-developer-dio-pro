T = int(input())

for i in range(T):
    # Ler as variáveis de entrada N e K
    N, K = map(int, input().split())

    # Calcular o número de garrafas que o cliente terá no segundo dia, se aproveitar ao máximo a oferta
    total_garrafas = N  # Começa com as garrafas compradas
    garrafas_vazias = N  # Inicialmente, todas as garrafas compradas estão vazias

    while garrafas_vazias >= K:
        novas_garrafas = garrafas_vazias // K  # Calcula quantas garrafas cheias podem ser obtidas
        total_garrafas += novas_garrafas  # Adiciona as novas garrafas cheias
        garrafas_vazias = (garrafas_vazias % K) + novas_garrafas  # Atualiza o número de garrafas vazias

    print(total_garrafas)
