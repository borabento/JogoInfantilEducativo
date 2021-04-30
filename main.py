import pygame
import random

SCREEN_WIDTH = 800
SCREEN_HEIGTH = 600
current_time = pygame.time.get_ticks()
clock = pygame.time.Clock()

#tela que aparece quando a pessoa acerta todas as letras
class tela_fim(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./assets/Ganhou.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = 0
        self.rect[1] = 0

#tela que aparece no final caso a pessoa erre
class tela_perdeu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./assets/Perdeu_Inicio.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = 0
        self.rect[1] = 0

#A vida é representada por uma borracha. Primeira vida
class vida(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./assets/Borracha_True.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = 50
        self.rect[1] = SCREEN_HEIGTH - 570

#segunda vida
class vida1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./assets/Borracha_True.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = 90
        self.rect[1] = SCREEN_HEIGTH - 570

#Terceira vida
class vida2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./assets/Borracha_True.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = 130
        self.rect[1] = SCREEN_HEIGTH - 570

#Class responsável implementação do personagem, que é uma nave, e suas funcionalidades como movimentação e colissões
class Nave(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        #Utilizado pra dá impressãp de movimento da chama da nave
        self.images = [pygame.image.load('./assets/NaveCima1.png').convert_alpha(),
                       pygame.image.load('./assets/NaveCima2.png').convert_alpha(),
                       pygame.image.load('./assets/NaveCima3.png').convert_alpha(),
                       pygame.image.load('./assets/NaveCima4.png').convert_alpha()]
        self.current_image = 0
        self.image = pygame.image.load(
            './assets/NaveCima1.png').convert_alpha()
        self.rect = self.image.get_rect()

        self.rect[0] = SCREEN_WIDTH / 2
        self.rect[1] = SCREEN_HEIGTH / 2
        self.speed_x = 0
        self.speed_y = 0
        self.vida = 3
        self.score = 0

    def update(self):
        self.current_image = (self.current_image + 1) % 4
        self.image = self.images[self.current_image]

        self.speed_x = 0
        self.speed_y = 0

        #Movimento da nave a partir do teclado
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speed_x = -8
        if keystate[pygame.K_RIGHT]:
            self.speed_x = 8
        if keystate[pygame.K_UP]:
            self.speed_y = -8
        if keystate[pygame.K_DOWN]:
            self.speed_y = 8

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.vida == 3:
            vida_group.draw(screen)
            vida1_group.draw(screen)
            vida2_group.draw(screen)
        if self.vida == 2:
            vida_group.draw(screen)
            vida1_group.draw(screen)
        if self.vida == 1:
            vida_group.draw(screen)
        if self.vida == 0:
            pygame.quit()
        if self.score == 5:
            tela_fim_group.draw(screen)
        if self.vida == 0:
            tela_perdeu_group.draw(screen)

        #colissões da nave com o asteroide e estrelas. Não tem ganho nem dano na vida, apenas dificulta a movimentação da nave
        if pygame.sprite.groupcollide(nave_group, aster_group, False, False):
            self.rect.x -= self.speed_x
            self.rect.y -= self.speed_y
        if pygame.sprite.groupcollide(nave_group, estrela_group, False, False):
            self.rect.x -= self.speed_x
            self.rect.y -= self.speed_y
        if pygame.sprite.groupcollide(nave_group, estrela1_group, False, False):
            self.rect.x -= self.speed_x
            self.rect.y -= self.speed_y
        if pygame.sprite.groupcollide(nave_group, estrela2_group, False, False):
            self.rect.x -= self.speed_x
            self.rect.y -= self.speed_y
        if pygame.sprite.groupcollide(nave_group, estrela3_group, False, False):
            self.rect.x -= self.speed_x
            self.rect.y -= self.speed_y

        palavra = ()
        #Colissões da nave com os planetas para verificar se a letra é respectiva com a letra da palavra ou não
        #Caso seja aumenta +1 ao score
        if pygame.sprite.groupcollide(nave_group, letra_m_group, False, True):
            #ativa a mudanda do stado da letra da palavra em destaque para negrito, confirmando o acerto
            m = LETRA("M", 200, True)
            m.isON = True
            letra_group.remove(m)
            letra_group.add(m)

            self.score += 1
            palavra += 'M',
            print(palavra)

            #Havendo o contato com o planeta ativa a animaçãoo da explosão
            explosa = Explosao(70, SCREEN_HEIGTH - 180, 2)
            explosao_group.add(explosa)

        if pygame.sprite.groupcollide(nave_group, letra_a_group, False, True):
            a = LETRA("A", 280, True)
            a.isON = True
            letra_group.remove(a)
            letra_group.add(a)

            self.score += 1
            palavra += 'A',
            print(palavra)

            explosa = Explosao3(760, SCREEN_HEIGTH - 560, 2)
            explosao_group.add(explosa)

        if pygame.sprite.groupcollide(nave_group, letra_r_group, False, True):
            r = LETRA("R", 360, True)
            r.isON = True
            letra_group.remove(r)
            letra_group.add(r)

            self.score += 1
            palavra += 'R',
            print(palavra)

            explosa = Explosao5(150, SCREEN_HEIGTH - 350, 2)
            explosao_group.add(explosa)

        if pygame.sprite.groupcollide(nave_group, letra_t_group, False, True):
            t = LETRA("T", 440, True)
            t.isON = True
            letra_group.remove(t)
            letra_group.add(t)

            self.score += 1
            palavra += 'T',
            print(palavra)

            explosa = Explosao1(710, SCREEN_HEIGTH - 60, 2)
            explosao_group.add(explosa)

        if pygame.sprite.groupcollide(nave_group, letra_e_group, False, True):
            e = LETRA("E", 520, True)
            e.isON = True
            letra_group.remove(e)
            letra_group.add(e)

            self.score += 1
            palavra += 'E',
            print(palavra)

            explosa = Explosao6(610, SCREEN_HEIGTH - 180, 2)
            explosao_group.add(explosa)

        #Caso a letra seja diferente com a letra da palavra perde uma vida
        if pygame.sprite.groupcollide(nave_group, letra_g_group, False, True):
            self.vida -= 1
            explosa = Explosao(530, SCREEN_HEIGTH - 465, 2)
            explosao_group.add(explosa)

        if pygame.sprite.groupcollide(nave_group, letra_i_group, False, True):
            self.vida -= 1
            explosa = Explosao2(310, SCREEN_HEIGTH - 170, 2)
            explosao_group.add(explosa)

        if pygame.sprite.groupcollide(nave_group, letra_n_group, False, True):
            self.vida -= 1
            explosa = Explosao4(710, SCREEN_HEIGTH - 350, 2)
            explosao_group.add(explosa)

        #Colisão com a borracha, que é a vida, em que caso a quantidade total seja menor que 3,
        # aumenta em +1 a quantidade da vida
        if pygame.sprite.groupcollide(nave_group, lifeUp_group, False, True):
            if self.vida <= 2:
                lifeUp = LifeUp(random.randint(0, SCREEN_WIDTH),
                                random.randint(0, SCREEN_WIDTH))
                lifeUp_group.add(lifeUp)
                self.vida += 1

        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > SCREEN_HEIGTH:
            self.rect.bottom = SCREEN_HEIGTH
        if self.rect.top < 0:
            self.rect.top = 0


class Asteroide(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(
            './assets/Asteroides.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = 110
        self.rect[1] = SCREEN_HEIGTH - 300

#classe da implementação da imagem do asteróide
class Estrela(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('./assets/Ativo 7.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = 100
        self.rect[1] = SCREEN_HEIGTH - 250

#classe da implementação da imagem do estrela
class Estrela1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('./assets/Ativo 7.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = 650
        self.rect[1] = SCREEN_HEIGTH - 550


class Estrela2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('./assets/Ativo 7.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = 500
        self.rect[1] = SCREEN_HEIGTH - 400


class Estrela3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('./assets/Ativo 7.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = 750
        self.rect[1] = SCREEN_HEIGTH - 150

#implementação da letra M colocando em sua posição na tela
class LetraM(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('./assets/M.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = 50
        self.rect[1] = SCREEN_HEIGTH - 200


class LetraA(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('./assets/A.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = 740
        self.rect[1] = SCREEN_HEIGTH - 580


class LetraR(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('./assets/R.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = 130
        self.rect[1] = SCREEN_HEIGTH - 380


class LetraT(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('./assets/T.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = 690
        self.rect[1] = SCREEN_HEIGTH - 80


class LetraE(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('./assets/E.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = 590
        self.rect[1] = SCREEN_HEIGTH - 200


class LetraG(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('./assets/G.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = 510
        self.rect[1] = SCREEN_HEIGTH - 490


class LetraI(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('./assets/I.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = 295
        self.rect[1] = SCREEN_HEIGTH - 185


class LetraN(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('./assets/N.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = 690
        self.rect[1] = SCREEN_HEIGTH - 380

#Implementação da vida
class LifeUp(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('./assets/Borracha_True.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.X = x
        self.Y = y
        self.rect[0] = self.X
        self.rect[1] = SCREEN_HEIGTH - self.Y

        #Tempo em que a vida ficará na tela
        self.endShowing = current_time + 5 * 1000
        self.startShowing = current_time
        self.isOn = True

#implementação da animação da explosão dos planetas Laranja
class Explosao(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        pygame.sprite.Sprite.__init__(self)


        self.images = []
        for num in range(1, 7):
            img = pygame.image.load(f"./assets/Laranja{num}.png")
            if size == 1:
                img = pygame.transform.scale(img, (70, 70))
            if size == 2:
                img = pygame.transform.scale(img, (90, 90))
            if size == 3:
                img = pygame.transform.scale(img, (140, 140))
            self.images.append(img)

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.counter = 0


    def update(self):
        explosao_speed = 3
        self.counter +=1

        if self.counter >= explosao_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        if self.index >= len(self.images) - 1 and self.counter >= explosao_speed:
            self.kill()


#implementação da animação da explosão dos planetas Vermelho
class Explosao1(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        pygame.sprite.Sprite.__init__(self)

        self.images = []
        for num in range(1, 7):
            img = pygame.image.load(f"./assets/Vermelho{num}.png")
            if size == 1:
                img = pygame.transform.scale(img, (70, 70))
            if size == 2:
                img = pygame.transform.scale(img, (90, 90))
            if size == 3:
                img = pygame.transform.scale(img, (140, 140))
            self.images.append(img)

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.counter = 0


    def update(self):
        explosao_speed = 3
        self.counter +=1

        if self.counter >= explosao_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        if self.index >= len(self.images) - 1 and self.counter >= explosao_speed:
            self.kill()


#implementação da animação da explosão dos planetas Roxo
class Explosao2(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        pygame.sprite.Sprite.__init__(self)

        self.images = []
        for num in range(1, 7):
            img = pygame.image.load(f"./assets/Roxo{num}.png")
            if size == 1:
                img = pygame.transform.scale(img, (70, 70))
            if size == 2:
                img = pygame.transform.scale(img, (90, 90))
            if size == 3:
                img = pygame.transform.scale(img, (140, 140))
            self.images.append(img)

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.counter = 0


    def update(self):
        explosao_speed = 3
        self.counter +=1

        if self.counter >= explosao_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        if self.index >= len(self.images) - 1 and self.counter >= explosao_speed:
            self.kill()


#implementação da animação da explosão dos planetas Rosa
class Explosao3(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        pygame.sprite.Sprite.__init__(self)

        self.images = []
        for num in range(1, 7):
            img = pygame.image.load(f"./assets/Rosa{num}.png")
            if size == 1:
                img = pygame.transform.scale(img, (70, 70))
            if size == 2:
                img = pygame.transform.scale(img, (90, 90))
            if size == 3:
                img = pygame.transform.scale(img, (140, 140))
            self.images.append(img)

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.counter = 0


    def update(self):
        explosao_speed = 3
        self.counter +=1

        if self.counter >= explosao_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        if self.index >= len(self.images) - 1 and self.counter >= explosao_speed:
            self.kill()


#implementação da animação da explosão dos planetas verde
class Explosao4(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        pygame.sprite.Sprite.__init__(self)

        self.images = []
        for num in range(1, 7):
            img = pygame.image.load(f"./assets/Verde{num}.png")
            if size == 1:
                img = pygame.transform.scale(img, (70, 70))
            if size == 2:
                img = pygame.transform.scale(img, (90, 90))
            if size == 3:
                img = pygame.transform.scale(img, (140, 140))
            self.images.append(img)

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.counter = 0


    def update(self):
        explosao_speed = 3
        self.counter +=1

        if self.counter >= explosao_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        if self.index >= len(self.images) - 1 and self.counter >= explosao_speed:
            self.kill()


class Explosao5(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        pygame.sprite.Sprite.__init__(self)

        self.images = []
        for num in range(1, 7):
            img = pygame.image.load(f"./assets/Azul{num}.png")
            if size == 1:
                img = pygame.transform.scale(img, (70, 70))
            if size == 2:
                img = pygame.transform.scale(img, (90, 90))
            if size == 3:
                img = pygame.transform.scale(img, (140, 140))
            self.images.append(img)

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.counter = 0


    def update(self):
        explosao_speed = 3
        self.counter +=1

        if self.counter >= explosao_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        if self.index >= len(self.images) - 1 and self.counter >= explosao_speed:
            self.kill()


class Explosao6(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        pygame.sprite.Sprite.__init__(self)

        self.images = []
        for num in range(1, 7):
            img = pygame.image.load(f"./assets/Amarelo{num}.png")
            if size == 1:
                img = pygame.transform.scale(img, (70, 70))
            if size == 2:
                img = pygame.transform.scale(img, (90, 90))
            if size == 3:
                img = pygame.transform.scale(img, (140, 140))
            self.images.append(img)

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.counter = 0


    def update(self):
        explosao_speed = 3
        self.counter +=1

        if self.counter >= explosao_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        if self.index >= len(self.images) - 1 and self.counter >= explosao_speed:
            self.kill()


class LETRA(pygame.sprite.Sprite):
    def __init__(self, name, x, on):
        pygame.sprite.Sprite.__init__(self)

        self.isON = on
        self.truePath = f'./assets/{name}_True.png'
        self.falsePath = f'./assets/{name}_False.png'

        self.currentPath = self.truePath if self.isON else self.falsePath

        self.image = pygame.image.load(self.currentPath).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect[0] = x
        self.rect[1] = 20


pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))

BACKGROUND = pygame.image.load('./assets/background.png')

#Mudança do icone e do nome na barrinha da janela
pygame.display.set_caption("Freirinho")
icon = pygame.image.load('./assets/icone.png')
pygame.display.set_icon(icon)

nave_group = pygame.sprite.Group()
nave = Nave()
nave_group.add(nave)

aster_group = pygame.sprite.Group()
aster = Asteroide()
aster_group.add(aster)

estrela_group = pygame.sprite.Group()
estrela = Estrela()
estrela_group.add(estrela)

estrela1_group = pygame.sprite.Group()
estrela1 = Estrela1()
estrela1_group.add(estrela1)

estrela2_group = pygame.sprite.Group()
estrela2 = Estrela2()
estrela2_group.add(estrela2)

estrela3_group = pygame.sprite.Group()
estrela3 = Estrela3()
estrela3_group.add(estrela3)

letra_m_group = pygame.sprite.Group()
letra_m = LetraM()
letra_m_group.add(letra_m)

letra_a_group = pygame.sprite.Group()
letra_a = LetraA()
letra_a_group.add(letra_a)

letra_r_group = pygame.sprite.Group()
letra_r = LetraR()
letra_r_group.add(letra_r)

letra_t_group = pygame.sprite.Group()
letra_t = LetraT()
letra_t_group.add(letra_t)

letra_e_group = pygame.sprite.Group()
letra_e = LetraE()
letra_e_group.add(letra_e)

letra_g_group = pygame.sprite.Group()
letra_g = LetraG()
letra_g_group.add(letra_g)

letra_i_group = pygame.sprite.Group()
letra_i = LetraI()
letra_i_group.add(letra_i)

letra_n_group = pygame.sprite.Group()
letra_n = LetraN()
letra_n_group.add(letra_n)

vida_group = pygame.sprite.Group()
vida = vida()
vida_group.add(vida)

vida1_group = pygame.sprite.Group()
vida1 = vida1()
vida1_group.add(vida1)

vida2_group = pygame.sprite.Group()
vida2 = vida2()
vida2_group.add(vida2)

tela_fim_group = pygame.sprite.Group()
tela_fim = tela_fim()
tela_fim_group.add(tela_fim)

tela_perdeu_group = pygame.sprite.Group()
tela_perdeu = tela_perdeu()
tela_perdeu_group.add(tela_fim)

explosao_group = pygame.sprite.Group()

explosao1_group = pygame.sprite.Group()

explosao2_group = pygame.sprite.Group()

explosao3_group = pygame.sprite.Group()

explosao4_group = pygame.sprite.Group()

explosao5_group = pygame.sprite.Group()

explosao6_group = pygame.sprite.Group()


lifeUp_group = pygame.sprite.Group()
lifeUp = LifeUp(random.randint(0, SCREEN_WIDTH),
                random.randint(0, SCREEN_WIDTH))
lifeUp_group.add(lifeUp)

letra_group = pygame.sprite.Group()
m = LETRA("M", 200, False)
a = LETRA("A", 280, False)
r = LETRA("R", 360, False)
t = LETRA("T", 440, False)
e = LETRA("E", 520, False)


letter_list = [m, a, r, t, e]

for x in letter_list:
    letra_group.add(x)


def draw():
    nave_group.draw(screen)
    aster_group.draw(screen)
    estrela_group.draw(screen)
    estrela1_group.draw(screen)
    estrela2_group.draw(screen)
    estrela3_group.draw(screen)
    letra_m_group.draw(screen)
    letra_a_group.draw(screen)
    letra_r_group.draw(screen)
    letra_t_group.draw(screen)
    letra_e_group.draw(screen)
    letra_g_group.draw(screen)
    letra_i_group.draw(screen)
    letra_n_group.draw(screen)
    letra_group.draw(screen)
    explosao_group.draw(screen)
    explosao1_group.draw(screen)
    explosao2_group.draw(screen)
    explosao3_group.draw(screen)
    explosao4_group.draw(screen)
    explosao5_group.draw(screen)
    explosao6_group.draw(screen)

    if (lifeUp.isOn):
        lifeUp_group.draw(screen)


def update():
    nave_group.update()
    aster_group.update()
    estrela_group.update()
    estrela1_group.update()
    estrela2_group.update()
    estrela3_group.update()
    letra_m_group.update()
    letra_a_group.update()
    letra_r_group.update()
    letra_t_group.update()
    letra_e_group.update()
    letra_g_group.update()
    letra_i_group.update()
    letra_n_group.update()
    vida_group.update()
    vida1_group.update()
    vida2_group.update()
    tela_fim_group.update()
    tela_perdeu_group.update()
    letra_group.update(screen)
    explosao_group.update()
    explosao1_group.update()
    explosao2_group.update()
    explosao3_group.update()
    explosao4_group.update()
    explosao5_group.update()
    explosao6_group.update()

    if (lifeUp.isOn):
        lifeUp_group.update()


while True:
    current_time = pygame.time.get_ticks()
    screen.blit(BACKGROUND, (0, 0))
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    current_time = pygame.time.get_ticks()

    if lifeUp.isOn:

        if lifeUp.endShowing and current_time >= lifeUp.endShowing:
            lifeUp_group.remove(lifeUp)
            lifeUp = LifeUp(random.randint(0, SCREEN_WIDTH),
                            random.randint(0, SCREEN_WIDTH))
            lifeUp_group.add(lifeUp)
            lifeUp.isOn = False
            lifeUp.endShowing = False
            lifeUp.startShowing = current_time + random.randint(1, 5) * 1000

    else:

        if lifeUp.startShowing and current_time >= lifeUp.startShowing:

            lifeUp.isOn = True
            lifeUp.startShowing = False
            lifeUp.endShowing = current_time + random.randint(1, 5) * 1000

    draw()
    update()
    pygame.display.update()
