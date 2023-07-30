n = int(input())

while n > 0:
    N = input().split(" ")
    A = N[0]
    B = N[1]

    b = -len(B)

    if (0<len(A)<=1000) and (0<len(B)<=1000):

      if len(A) >= len(B):
          if A[b:] == B:
              print('encaixa')
          else:
              print('nao encaixa')
      else:
          print('nao encaixa')
      
      n = n - 1
