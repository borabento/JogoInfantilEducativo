quantidade_movimento = int(input())
cavalo = input()
rei = input()

#recursao do movimento do cavalo, movimento em L
def movimentacao_cavalo(cavalo, rei):
    if (movimentacao_cavalo == 0):
        return cavalo
    else:
        casasTestadas = [[False] * 8 for i in range(8)]
        passos = [cavalo + [0]]

def vaiCavalo( origem, destino ):
   casasTestadas = [[False]*8 for i in range(8)]
   passos = [origem+[0]]

   while True:
      proximosPassos = []
      for passo in passos:
         for movimento in [[-1,-2],[-2,-1],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2]]:
            x,y = passo[0]+movimento[0], passo[1]+movimento[1]
            if [x,y] == destino:
               return passo[2]+1
            if 0 <= x < 8 and 0 <= y < 8 and not casasTestadas[x][y]:
               proximosPassos.append([x,y,passo[2]+1])
               casasTestadas[x][y] = True
      passos = proximosPassos

#verificar se chegou no rei

