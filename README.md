# Projeto \<nome\>
### FPRO/MIEIC, 2019/20
### \<Fulano de Tal (up2019xxxxx@fe.up.pt)\>
### \<1MIEIC0X\> 

#### Objetivo

1. \<Criar um clone do clássico Sokoban em Pygame\>

2. \<Em alternativa... do clássico x em Pygame\>

#### Repositório de código

1) Link para o repositório do GitHub: <https://github.com/fpro-feup/public>

2) Adicionar o prof. da Unidade (ver lista em baixo) e o "Lord of the Game" (aka Ricardo Cruz):

- https://github.com/fernandocassola
- https://github.com/rpmcruz
- https://github.com/jlopes60
- https://github.com/rcamacho

#### Descrição

\<É um jogo de puzzle em que o objetivo do jogo é empurrar caixotes para um sítio indicado. 
Para empurrar o caixote é preciso ir ao outro lado empurrá-lo. 
Ou seja, se ele ficar junto à parede, a pessoa precisa de reiniciar o jogo. Estamos a utilizar os níveis do XSokoban.\>

#### UI

![UI](https://github.com/fpro-feup/public/blob/master/assigns/ui.png)

### Pacotes

- Pygame

#### Tarefas

1. **BACKGROUND**
   1. montanhas: duas elipses
   1. céu: ciclo
1. **JOGADOR**
   1. desenhar naquela posição
   1. variar o ângulo: angle
   1. tecla -> muda o angle
1. **TIROS**
   1. lista: (x, y, angulo)
      * quando carregas no space, acrescentas tuplo
      * desenhar os tiros na posição (x,y) com o angulo dado
   1. atualizar posição do tiro na lista
1. **INIMIGOS NAVES**
   1. de vez em quando, aparece uma nave: lista (pos_x, pos_y, orientacao)
   1. atualizar posição da nave
   1. colisão tiro/nave
1. **INIMIGOS PARAQUEDISTAS**
   1. nave aleatoriamente cria paraquedista em certos X: lista (pos_x, pos_y)
   1. atualizar posiçáo paraquedista
   1. desaparece quando ao solo
1. **CASAS**
   1. Quatro cidades: (pos_x, estado)
      * estado inicialmente = 5
   1. desenhar cidade conforme estado
   1. paraquedista, reduz estado em 1
1. **TUNEL**, **PONTOS**, **MENU**

### \<date\>

---------

# COPIA

#Projeto Commando Raid

FPRO/MIEIC, 2019/20

Mário Ferreira (up201907727@fe.up.pt)
<1MIEIC04>

Objetivo
Criar um clone do clássico Command Raid em Pygame.

Repositório de código
Link para o repositório do GitHub: https://github.com/mpspmf/atari2600_commando_raid

Descrição
É um jogo de ação em que o objetivo do jogo é disparar um canhão para destruir helicópteros e aviões antes que estes deixem cair bombas ou soldados que também podem ser destruidos e que danificam o canhão.


Pacotes
Pygame

Tarefas
ler teclas
verificar se jogador chegou ao fim do nível

19/11/2019
