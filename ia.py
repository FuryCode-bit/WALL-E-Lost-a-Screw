# Source Generated with Decompyle++
# File: ia.py (Python 3.8)

import pygame
from pygame.locals import *
import os
import agente
import math

class Fabrica:
    
    def __init__(self):
        self.OO0000O00OOOOOO0 = 100
        self.O0000000000O0O0O = [
            (17, 85),
            (760, 325)]
        self.O0O0OOO0O000000Os = [
            [
                (475, 125),
                chr(65) + chr(110) + chr(97)],
            [
                (175, 270),
                chr(67) + chr(97) + chr(114) + chr(108) + chr(111) + chr(115)],
            [
                (365, 570),
                chr(77) + chr(97) + chr(114) + chr(105) + chr(97)]]
        self.O0OOO0000O000O00s = [
            [
                (730, 50),
                chr(80) + chr(97) + chr(117) + chr(108) + chr(111)],
            [
                (460, 545),
                chr(77) + chr(105) + chr(103) + chr(117) + chr(101) + chr(108)],
            [
                (425, 35),
                chr(77) + chr(97) + chr(114) + chr(105) + chr(97)],
            [
                (695, 570),
                chr(82) + chr(117) + chr(105)],
            [
                (100, 550),
                chr(80) + chr(97) + chr(117) + chr(108) + chr(97)],
            [
                (555, 40),
                chr(65) + chr(100) + chr(233) + chr(114) + chr(105) + chr(116) + chr(111)],
            [
                (700, 500),
                chr(77) + chr(105) + chr(99) + chr(97) + chr(101) + chr(108) + chr(97)],
            [
                (730, 240),
                chr(65) + chr(109) + chr(225) + chr(108) + chr(105) + chr(97)],
            [
                (260, 275),
                chr(70) + chr(225) + chr(98) + chr(105) + chr(111)],
            [
                (195, 535),
                chr(83) + chr(117) + chr(115) + chr(97) + chr(110) + chr(97)]]
        self.O0O0OO0O0O00O00Os = [
            [
                (630, 105),
                chr(82) + chr(105) + chr(99) + chr(97) + chr(114) + chr(100) + chr(111)],
            [
                (335, 490),
                chr(67) + chr(108) + chr(225) + chr(117) + chr(100) + chr(105) + chr(97)],
            [
                (190, 120),
                chr(69) + chr(108) + chr(115) + chr(97)],
            [
                (90, 400),
                chr(74) + chr(111) + chr(97) + chr(113) + chr(117) + chr(105) + chr(109)]]
        self.O000OOOOO00O0OOO = [
            [
                (420, 540),
                chr(109) + chr(97) + chr(116) + chr(101) + chr(114) + chr(105) + chr(97) + chr(108) + chr(49)],
            [
                (235, 535),
                chr(109) + chr(97) + chr(116) + chr(101) + chr(114) + chr(105) + chr(97) + chr(108) + chr(50)],
            [
                (125, 35),
                chr(109) + chr(97) + chr(116) + chr(101) + chr(114) + chr(105) + chr(97) + chr(108) + chr(51)]]
        self.OOO0OOOOO0OO00O0 = [
            [
                (415, 285),
                chr(109) + chr(111) + chr(110) + chr(116) + chr(97) + chr(103) + chr(101) + chr(109)],
            [
                (435, 95),
                chr(105) + chr(110) + chr(115) + chr(112) + chr(101) + chr(231) + chr(227) + chr(111)],
            [
                (760, 110),
                chr(101) + chr(109) + chr(112) + chr(97) + chr(99) + chr(111) + chr(116) + chr(97) + chr(109) + chr(101) + chr(110) + chr(116) + chr(111)],
            [
                (55, 515),
                chr(101) + chr(115) + chr(99) + chr(114) + chr(105) + chr(116) + chr(243) + chr(114) + chr(105) + chr(111)],
            [
                (285, 30),
                chr(108) + chr(97) + chr(98) + chr(111) + chr(114) + chr(97) + chr(116) + chr(243) + chr(114) + chr(105) + chr(111)],
            [
                (585, 490),
                chr(116) + chr(101) + chr(115) + chr(116) + chr(101)]]
        self.OOO000000O0OO0O0s = [
            [
                (210, 65),
                chr(109) + chr(225) + chr(113) + chr(117) + chr(105) + chr(110) + chr(97) + chr(49)],
            [
                (565, 115),
                chr(109) + chr(225) + chr(113) + chr(117) + chr(105) + chr(110) + chr(97) + chr(50)],
            [
                (630, 550),
                chr(109) + chr(225) + chr(113) + chr(117) + chr(105) + chr(110) + chr(97) + chr(51)],
            [
                (245, 235),
                chr(109) + chr(225) + chr(113) + chr(117) + chr(105) + chr(110) + chr(97) + chr(52)],
            [
                (365, 280),
                chr(109) + chr(225) + chr(113) + chr(117) + chr(105) + chr(110) + chr(97) + chr(53)],
            [
                (550, 550),
                chr(109) + chr(225) + chr(113) + chr(117) + chr(105) + chr(110) + chr(97) + chr(54)],
            [
                (455, 280),
                chr(109) + chr(225) + chr(113) + chr(117) + chr(105) + chr(110) + chr(97) + chr(55)]]
        self.OOOOO00OOO00OO00 = [
            'dejavusans',
            'couriernew',
            'Papyrus',
            'Comic Sans MS',
            'timesnewroman']
        self.O00OO0OO000OO0O0 = { }
        self.OOO0OOOOOOO0O000 = { }
        self.OO0OO0OO0000O000 = { }
        self.OOO000000O0OO0O0 = self.O00OOOOOOOO00O0O(chr(105) + chr(109) + chr(103) + chr(115) + chr(47) + chr(109) + chr(97) + chr(113) + chr(51) + chr(46) + chr(112) + chr(110) + chr(103))
        self.O0O00OO0O000OOOO = self.O00OOOOOOOO00O0O(chr(105) + chr(109) + chr(103) + chr(115) + chr(47) + chr(116) + chr(105) + chr(106) + chr(111) + chr(108) + chr(111) + chr(51) + chr(46) + chr(112) + chr(110) + chr(103))
        self.O0OOOOO0O0OOO0O0 = self.O00OOOOOOOO00O0O(chr(105) + chr(109) + chr(103) + chr(115) + chr(47) + chr(65) + chr(49) + chr(46) + chr(112) + chr(110) + chr(103))
        self.O000OO0O0O000OO0 = self.O00OOOOOOOO00O0O(chr(105) + chr(109) + chr(103) + chr(115) + chr(47) + chr(98) + chr(111) + chr(116) + chr(52) + chr(46) + chr(112) + chr(110) + chr(103))
        self.O0O0OO0O0O00O00O = self.O00OOOOOOOO00O0O(chr(105) + chr(109) + chr(103) + chr(115) + chr(47) + chr(86) + chr(49) + chr(46) + chr(112) + chr(110) + chr(103))
        self.O0O0OOO0O000000O = self.O00OOOOOOOO00O0O(chr(105) + chr(109) + chr(103) + chr(115) + chr(47) + chr(83) + chr(49) + chr(46) + chr(112) + chr(110) + chr(103))
        self.O0OOO0000O000O00 = self.O00OOOOOOOO00O0O(chr(105) + chr(109) + chr(103) + chr(115) + chr(47) + chr(79) + chr(49) + chr(46) + chr(112) + chr(110) + chr(103))
        self.OO00OOOOOOOOO000 = self.O00OOOOOOOO00O0O(chr(105) + chr(109) + chr(103) + chr(115) + chr(47) + chr(90) + chr(46) + chr(112) + chr(110) + chr(103))
        self.O000O0O0OOO0000O = self.O00OOOOOOOO00O0O(chr(105) + chr(109) + chr(103) + chr(115) + chr(47) + chr(98) + chr(97) + chr(116) + chr(101) + chr(114) + chr(105) + chr(97) + chr(46) + chr(112) + chr(110) + chr(103))
        pygame.init()
        self.OOOO0O0OOO00OO0O = pygame.display.set_mode((800, 600))
        pygame.display.set_caption(chr(85) + chr(66) + chr(73) + chr(32) + chr(45) + chr(45) + chr(32) + chr(73) + chr(65) + chr(32) + chr(50) + chr(48) + chr(50) + chr(51) + chr(45) + chr(50) + chr(52))
        print(chr(80) + chr(114) + chr(101) + chr(109) + chr(105) + chr(114) + chr(32) + chr(65) + chr(44) + chr(83) + chr(44) + chr(87) + chr(44) + chr(68) + chr(32) + chr(112) + chr(97) + chr(114) + chr(97) + chr(32) + chr(109) + chr(111) + chr(118) + chr(101) + chr(114) + chr(44) + chr(32) + chr(69) + chr(83) + chr(67) + chr(32) + chr(112) + chr(97) + chr(114) + chr(97) + chr(32) + chr(116) + chr(101) + chr(114) + chr(109) + chr(105) + chr(110) + chr(97) + chr(114) + chr(46))

    
    def O0OOO00OO0OOO000(self):
        self.OOOO0O0OOO00OO0O.fill((255, 255, 255))
        for i in range(0, 600, 15):
            self.OOOO0O0OOO00OO0O.blit(self.O0O00OO0O000OOOO, (0, i))
            self.OOOO0O0OOO00OO0O.blit(self.O0O00OO0O000OOOO, (785, i))
        for i in range(0, 800, 15):
            self.OOOO0O0OOO00OO0O.blit(self.O0O00OO0O000OOOO, (i, 0))
            self.OOOO0O0OOO00OO0O.blit(self.O0O00OO0O000OOOO, (i, 585))
        for i in range(0, 150, 15):
            self.OOOO0O0OOO00OO0O.blit(self.O0O00OO0O000OOOO, (150, i))
            self.OOOO0O0OOO00OO0O.blit(self.O0O00OO0O000OOOO, (300, i))
            self.OOOO0O0OOO00OO0O.blit(self.O0O00OO0O000OOOO, (500, i))
            self.OOOO0O0OOO00OO0O.blit(self.O0O00OO0O000OOOO, (500, i + 150))
            self.OOOO0O0OOO00OO0O.blit(self.O0O00OO0O000OOOO, (500, i + 215))
        for i in range(450, 600, 15):
            self.OOOO0O0OOO00OO0O.blit(self.O0O00OO0O000OOOO, (150, i))
            self.OOOO0O0OOO00OO0O.blit(self.O0O00OO0O000OOOO, (300, i))
            self.OOOO0O0OOO00OO0O.blit(self.O0O00OO0O000OOOO, (500, i))
        for i in range(150, 500, 15):
            self.OOOO0O0OOO00OO0O.blit(self.O0O00OO0O000OOOO, (i, 200))
            self.OOOO0O0OOO00OO0O.blit(self.O0O00OO0O000OOOO, (i, 350))
        for i in range(650, 800, 15):
            self.OOOO0O0OOO00OO0O.blit(self.O0O00OO0O000OOOO, (i, 200))
            self.OOOO0O0OOO00OO0O.blit(self.O0O00OO0O000OOOO, (i, 300))
            self.OOOO0O0OOO00OO0O.blit(self.O0O00OO0O000OOOO, (i, 400))
        for i in self.O0O0OOO0O000000Os:
            self.OOOO0O0OOO00OO0O.blit(self.O0O0OOO0O000000O, (i[0][0] - 12, i[0][1] - 12))
        for i in self.O0OOO0000O000O00s:
            self.OOOO0O0OOO00OO0O.blit(self.O0OOO0000O000O00, (i[0][0] - 12, i[0][1] - 12))
        for i in self.O0O0OO0O0O00O00Os:
            self.OOOO0O0OOO00OO0O.blit(self.O0O0OO0O0O00O00O, (i[0][0] - 12, i[0][1] - 12))
        for i in self.OOO000000O0OO0O0s:
            self.OOOO0O0OOO00OO0O.blit(self.OOO000000O0OO0O0, (i[0][0] - 12, i[0][1] - 12))
        for i in self.OOO0OOOOO0OO00O0:
            self.OOOO0O0OOO00OO0O.blit(self.OO00OOOOOOOOO000, (i[0][0] - 12, i[0][1] - 12))
        for i in self.O000OOOOO00O0OOO:
            self.OOOO0O0OOO00OO0O.blit(self.O0OOOOO0O0OOO0O0, (i[0][0] - 12, i[0][1] - 12))
        for i in self.O0000000000O0O0O:
            self.OOOO0O0OOO00OO0O.blit(self.O000O0O0OOO0000O, i)

    
    def OO0OO0O000000OOO(self, fonts, size):
        available = pygame.font.get_fonts()
        choices = map((lambda x: x.lower().replace(' ', '')), fonts)
        for choice in choices:
            if choice in available:
                return pygame.font.SysFont(choice, size)
            return pygame.font.Font(None, size)

    
    def O00OO00O00OO0OOO(self, O00OOOOO00O00OOO, size):
        key = str(O00OOOOO00O00OOO) + '|' + str(size)
        font = self.O00OO0OO000OO0O0.get(key, None)
        if font == None:
            font = self.OO0OO0O000000OOO(self.OOOOO00OOO00OO00, size)
            self.O00OO0OO000OO0O0[key] = font
        return font

    
    def OO0OO00O0OO00O0O(self, text, fonts, size, color):
        key = '|'.join(map(str, (fonts, size, color, text)))
        image = self.OOO0OOOOOOO0O000.get(key, None)
        if image == None:
            font = self.O00OO00O00OO0OOO(fonts, size)
            image = font.render(text, True, color)
            self.OOO0OOOOOOO0O000[key] = image
        return image

    
    def O00OOOOOOOO00O0O(self, path):
        image = self.OO0OO0OO0000O000.get(path)
        if image == None:
            OO0O0O00OO00O00O = path.replace('/', os.sep).replace(' ', os.sep)
            image = pygame.image.load(OO0O0O00OO00O00O)
            self.OO0OO0OO0000O000[path] = image
        return image

    
    def O00OOO0OO000O00O(self, pos):
        dt = -6
        out = []
        for i in self.O0O0OOO0O000000Os:
            if abs(pos[0] + dt - i[0][0]) + abs(pos[1] + dt - i[0][1]) < 50:
                out.append(chr(115) + chr(117) + chr(112) + chr(101) + chr(114) + chr(118) + chr(105) + chr(115) + chr(111) + chr(114) + chr(95) + i[1])
                continue
        for i in self.O0OOO0000O000O00s:
            if abs(pos[0] + dt - i[0][0]) + abs(pos[1] + dt - i[0][1]) < 50:
                out.append(chr(111) + chr(112) + chr(101) + chr(114) + chr(225) + chr(114) + chr(105) + chr(111) + chr(95) + i[1])
                continue
        for i in self.O0O0OO0O0O00O00Os:
            if abs(pos[0] + dt - i[0][0]) + abs(pos[1] + dt - i[0][1]) < 50:
                out.append(chr(118) + chr(105) + chr(115) + chr(105) + chr(116) + chr(97) + chr(110) + chr(116) + chr(101) + chr(95) + i[1])
                continue
        for i in self.O000OOOOO00O0OOO:
            if abs(pos[0] + dt - i[0][0]) + abs(pos[1] + dt - i[0][1]) < 50:
                out.append(chr(97) + chr(114) + chr(109) + chr(97) + chr(122) + chr(233) + chr(109) + chr(95) + i[1])
                continue
        for i in self.OOO0OOOOO0OO00O0:
            if abs(pos[0] + dt - i[0][0]) + abs(pos[1] + dt - i[0][1]) < 50:
                out.append(chr(122) + chr(111) + chr(110) + chr(97) + chr(95) + i[1])
                continue
        for i in self.OOO000000O0OO0O0s:
            if abs(pos[0] + dt - i[0][0]) + abs(pos[1] + dt - i[0][1]) < 50:
                out.append(chr(109) + chr(225) + chr(113) + chr(117) + chr(105) + chr(110) + chr(97) + chr(95) + i[1])
                continue
        for i in self.O0000000000O0O0O:
            if abs(pos[0] + dt - i[0]) + abs(pos[1] + dt - i[1]) < 50:
                self.OO0000O00OOOOOO0 = 100
                continue
        return out

    
    def OO0000O000O00000(self):
        done = False
        O0OOOOO00OO00OOO = pygame.time.Clock()
        O00O0O00O0O00OO0 = [
            False,
            False,
            False,
            False]
        OOO0O0O0O0OOO0O0 = [
            770,
            375]
        OOO000OOO0O00O0O = ''
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == K_w:
                        O00O0O00O0O00OO0[0] = True
                    elif event.key == K_s:
                        O00O0O00O0O00OO0[1] = True
                    elif event.key == K_a:
                        O00O0O00O0O00OO0[2] = True
                    elif event.key == K_d:
                        O00O0O00O0O00OO0[3] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        O00O0O00O0O00OO0[0] = False
                    elif event.key == pygame.K_s:
                        O00O0O00O0O00OO0[1] = False
                    elif event.key == pygame.K_a:
                        O00O0O00O0O00OO0[2] = False
                    elif event.key == pygame.K_d:
                        O00O0O00O0O00OO0[3] = False
                if event.type == pygame.KEYDOWN:
                    if event.key == K_1:
                        print('1- Qual foi a penúltima pessoa do sexo masculino que viste?')
                        agente.resp1()
                        self.OO0000O00OOOOOO0 -= self.OO0000O00OOOOOO0 / 4000
                    elif event.key == K_2:
                        print('2- Em que tipo de zona estás agora?')
                        agente.resp2()
                        self.OO0000O00OOOOOO0 -= self.OO0000O00OOOOOO0 / 4123
                    elif event.key == K_3:
                        print('3- Qual o caminho para a zona de empacotamento?')
                        agente.resp3()
                        self.OO0000O00OOOOOO0 -= self.OO0000O00OOOOOO0 / 4000
                    elif event.key == K_4:
                        print('4- Qual a distância até ao laboratório?')
                        agente.resp4()
                        self.OO0000O00OOOOOO0 -= self.OO0000O00OOOOOO0 / 4000
                    elif event.key == K_5:
                        print('5- Quanto tempo achas que demoras a ir de onde estás até ao escritório?')
                        agente.resp5()
                        self.OO0000O00OOOOOO0 -= self.OO0000O00OOOOOO0 / 4000
                    elif event.key == K_6:
                        print('6- Quanto tempo achas que falta até ficares sem bateria?')
                        agente.resp6()
                        self.OO0000O00OOOOOO0 -= self.OO0000O00OOOOOO0 / 3333
                    elif event.key == K_7:
                        print('7- Qual é a probabilidade da próxima pessoa a encontrares ser um supervisor?')
                        agente.resp7()
                        self.OO0000O00OOOOOO0 -= self.OO0000O00OOOOOO0 / 4123
                    elif event.key == K_8:
                        print('8- Qual é a probabilidade de encontrares um operário numa zona se estiver lá uma máquina mas não estiver lá um supervisor?')
                        agente.resp8()
                        self.OO0000O00OOOOOO0 -= self.OO0000O00OOOOOO0 / 4123
                if self.OO0000O00OOOOOO0 > 1:
                    if O00O0O00O0O00OO0[0] and self.OOOO0O0OOO00OO0O.get_at((OOO0O0O0O0OOO0O0[0] - 12, OOO0O0O0O0OOO0O0[1] - 17)) == (255, 255, 255, 255) and self.OOOO0O0OOO00OO0O.get_at((OOO0O0O0O0OOO0O0[0], OOO0O0O0O0OOO0O0[1] - 17)) == (255, 255, 255, 255) and self.OOOO0O0OOO00OO0O.get_at((OOO0O0O0O0OOO0O0[0] + 12, OOO0O0O0O0OOO0O0[1] - 17)) == (255, 255, 255, 255):
                        OOO0O0O0O0OOO0O0[1] -= 5
                        self.OO0000O00OOOOOO0 -= self.OO0000O00OOOOOO0 / 4000
                    elif O00O0O00O0O00OO0[1] and self.OOOO0O0OOO00OO0O.get_at((OOO0O0O0O0OOO0O0[0] - 12, OOO0O0O0O0OOO0O0[1] + 17)) == (255, 255, 255, 255) and self.OOOO0O0OOO00OO0O.get_at((OOO0O0O0O0OOO0O0[0], OOO0O0O0O0OOO0O0[1] + 17)) == (255, 255, 255, 255) and self.OOOO0O0OOO00OO0O.get_at((OOO0O0O0O0OOO0O0[0] + 12, OOO0O0O0O0OOO0O0[1] + 17)) == (255, 255, 255, 255):
                        OOO0O0O0O0OOO0O0[1] += 5
                        self.OO0000O00OOOOOO0 -= self.OO0000O00OOOOOO0 / 4000
                    if O00O0O00O0O00OO0[2] and self.OOOO0O0OOO00OO0O.get_at((OOO0O0O0O0OOO0O0[0] - 17, OOO0O0O0O0OOO0O0[1] - 12)) == (255, 255, 255, 255) and self.OOOO0O0OOO00OO0O.get_at((OOO0O0O0O0OOO0O0[0] - 17, OOO0O0O0O0OOO0O0[1])) == (255, 255, 255, 255) and self.OOOO0O0OOO00OO0O.get_at((OOO0O0O0O0OOO0O0[0] - 17, OOO0O0O0O0OOO0O0[1] + 12)) == (255, 255, 255, 255):
                        OOO0O0O0O0OOO0O0[0] -= 5
                        self.OO0000O00OOOOOO0 -= self.OO0000O00OOOOOO0 / 4000
                    elif O00O0O00O0O00OO0[3] and self.OOOO0O0OOO00OO0O.get_at((OOO0O0O0O0OOO0O0[0] + 17, OOO0O0O0O0OOO0O0[1] - 12)) == (255, 255, 255, 255) and self.OOOO0O0OOO00OO0O.get_at((OOO0O0O0O0OOO0O0[0] + 17, OOO0O0O0O0OOO0O0[1])) == (255, 255, 255, 255) and self.OOOO0O0OOO00OO0O.get_at((OOO0O0O0O0OOO0O0[0] + 17, OOO0O0O0O0OOO0O0[1] + 12)) == (255, 255, 255, 255):
                        OOO0O0O0O0OOO0O0[0] += 5
                        self.OO0000O00OOOOOO0 -= self.OO0000O00OOOOOO0 / 4000
                self.O0OOO00OO0OOO000()
                self.OOOO0O0OOO00OO0O.blit(self.O000OO0O0O000OO0, [
                    OOO0O0O0O0OOO0O0[0] - 12,
                    OOO0O0O0O0OOO0O0[1] - 12])
                text = self.OO0OO00O0OO00O0O(str(OOO0O0O0O0OOO0O0), self.OOOOO00OOO00OO00, 14, (0, 0, 0))
                self.OOOO0O0OOO00OO0O.blit(text, (725, 584))
                text = self.OO0OO00O0OO00O0O(str(int(self.OO0000O00OOOOOO0)), self.OOOOO00OOO00OO00, 14, (0, 0, 0))
                self.OOOO0O0OOO00OO0O.blit(text, (700, 584))
                pygame.display.flip()
                O000OO0O0O0O0OOO = self.O00OOO0OO000O00O(OOO0O0O0O0OOO0O0)
                if O000OO0O0O0O0OOO != OOO000OOO0O00O0O and O000OO0O0O0O0OOO != []:
                    print(O000OO0O0O0O0OOO)
                OOO000OOO0O00O0O = O000OO0O0O0O0OOO
                agente.work(OOO0O0O0O0OOO0O0, self.OO0000O00OOOOOO0, O000OO0O0O0O0OOO)
                O0OOOOO00OO00OOO.tick(50)
                continue

h = Fabrica()
h.OO0000O000O00000()
