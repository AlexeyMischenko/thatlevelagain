import pygame
import colorsys

pygame.font.init()
BGC = (255, 204, 255)


class Load():
    def __init__(self):
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.x = 0
        self.dot = 100
        self.r = 1
        self.g = 1
        self.b = 1
        self.zn = 1

    def draw(self):
        screen.fill(pygame.Color(255, 204, 255))
        textsurface = self.myfont.render('LOADING' + '.' * (self.dot // 100), True, (0, 0, 0))
        if self.dot < 500:
            self.dot += 5
        else:
            self.dot = 100
        screen.blit(textsurface, (width / 2 - 70, 300))

        h = (self.x / width)
        s = 1
        l = 0.5
        color = colorsys.hls_to_rgb(h, l, s)
        color = [int(x * 255) for x in color]
        screen.fill(pygame.Color(color[0], color[1], color[2]), pygame.Rect(0, 350, self.x, 20))
        self.x += 1

        if self.x == width:
            global loading
            global menu_on
            loading = False
            menu_on = True


class Options():
    def __init__(self):
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.back_shadow = True
        self.right_shadow = True
        self.left_shadow = True
        self.levels_unlocked = False
        self.open_levels_shadow = True

    def draw(self):
        screen.fill(pygame.Color(255, 204, 255))
        textsurface = self.myfont.render('OPTIONS', True, (0, 0, 0))
        screen.blit(textsurface, (width / 2 - 70, 150))

        back = self.myfont.render('<- BACK', True, (0, 0, 0))
        if self.back_shadow:
            screen.fill(pygame.Color(50, 50, 50), pygame.Rect(25, 25, 150, 50))
            screen.fill(pygame.Color(0, 204, 102), pygame.Rect(20, 20, 150, 50))
            screen.blit(back, (30, 20))
        else:
            screen.fill(pygame.Color(0, 204, 102), pygame.Rect(25, 25, 150, 50))
            screen.blit(back, (35, 25))
        # delay
        textsurface2 = self.myfont.render("DELAY " + str(delay), True, (0, 0, 0))
        screen.fill(pygame.Color(0, 204, 102), pygame.Rect(width / 2 - 85, 235, 180, 50))
        screen.blit(textsurface2, (width / 2 - 50, 235))
        # RIGHT BUTTON
        right = self.myfont.render("<", True, (0, 0, 0))
        if self.right_shadow:
            screen.fill(pygame.Color(50, 50, 50), pygame.Rect(width / 2 - 145, 235, 50, 50))
            screen.fill(pygame.Color(0, 204, 102), pygame.Rect(width / 2 - 150, 230, 50, 50))
            screen.blit(right, (width / 2 - 130, 230))
        else:
            screen.fill(pygame.Color(0, 204, 102), pygame.Rect(width / 2 - 145, 235, 50, 50))
            screen.blit(right, (width / 2 - 125, 235))
        # LEFT BUTTON
        left = self.myfont.render(">", True, (0, 0, 0))
        if self.left_shadow:
            screen.fill(pygame.Color(50, 50, 50), pygame.Rect(width / 2 + 105, 235, 50, 50))
            screen.fill(pygame.Color(0, 204, 102), pygame.Rect(width / 2 + 100, 230, 50, 50))
            screen.blit(left, (width / 2 + 120, 230))
        else:
            screen.fill(pygame.Color(0, 204, 102), pygame.Rect(width / 2 + 105, 235, 50, 50))
            screen.blit(left, (width / 2 + 125, 235))

        if not self.levels_unlocked:
            chits = self.myfont.render("OPEN ALL LEVELS", True, (0, 0, 0))
        else:
            chits = self.myfont.render("ALREADY OPENED", True, (0, 0, 0))
        if self.open_levels_shadow:
            if not self.levels_unlocked:
                screen.fill(pygame.Color(50, 50, 50), pygame.Rect(width / 2 - 145, 325, 300, 50))
            else:
                screen.fill(pygame.Color(0, 255, 0), pygame.Rect(width / 2 - 145, 325, 300, 50))
            screen.fill(pygame.Color(0, 204, 102), pygame.Rect(width / 2 - 150, 320, 300, 50))
            screen.blit(chits, (width / 2 - 140, 320))
        else:
            screen.fill(pygame.Color(0, 204, 102), pygame.Rect(width / 2 - 145, 325, 300, 50))
            screen.blit(chits, (width / 2 - 135, 325))


class Rules():
    def __init__(self):
        self.back_shadow = True
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.text = pygame.image.load('./data/rules.png').convert()

    def draw(self):
        screen.fill(pygame.Color(255, 204, 255))
        # self.text_rect = self.text.get_rect(center=(50, 50))
        screen.fill(pygame.Color(0, 0, 0), pygame.Rect(270, 220, 650, 240))
        screen.blit(self.text, (275, 225))
        textsurface = self.myfont.render('RULES', True, (0, 0, 0))
        screen.blit(textsurface, (width / 2 - 50, 150))

        back = self.myfont.render('<- BACK', True, (0, 0, 0))
        if self.back_shadow:
            screen.fill(pygame.Color(50, 50, 50), pygame.Rect(25, 25, 150, 50))
            screen.fill(pygame.Color(0, 204, 102), pygame.Rect(20, 20, 150, 50))
            screen.blit(back, (30, 20))
        else:
            screen.fill(pygame.Color(0, 204, 102), pygame.Rect(25, 25, 150, 50))
            screen.blit(back, (35, 25))


class Menu():
    def __init__(self):
        self.start_shadow = True
        self.right_shadow = True
        self.left_shadow = True
        self.rules_shadow = True
        self.options_shadow = True
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
        #self.menu = pygame.image.load('./brain1.jpg').convert()
        # self.menu.set_colorkey((255, 255, 255))

    def draw(self):
        #self.menu_rect = self.menu.get_rect((0, 0))
        #screen.blit(self.menu, (-20, 0))
        screen.fill(pygame.Color(255, 204, 255))
        # Start ->
        textsurface = self.myfont.render('START', True, (0, 0, 0))
        if self.start_shadow:
            screen.fill(pygame.Color(50, 50, 50), pygame.Rect(width / 2 - 145, 155, 300, 50))
            screen.fill(pygame.Color(0, 204, 102), pygame.Rect(width / 2 - 150, 150, 300, 50))
            screen.blit(textsurface, (width / 2 - 50, 150))
        else:
            screen.fill(pygame.Color(0, 204, 102), pygame.Rect(width / 2 - 145, 155, 300, 50))
            screen.blit(textsurface, (width / 2 - 45, 155))
        # LEVEL
        textsurface2 = self.myfont.render("LEVEL " + str(level), True, (0, 0, 0))
        screen.fill(pygame.Color(0, 204, 102), pygame.Rect(width / 2 - 85, 235, 180, 50))
        screen.blit(textsurface2, (width / 2 - 50, 235))
        # RIGHT BUTTON
        right = self.myfont.render("<", True, (0, 0, 0))
        if self.right_shadow:
            screen.fill(pygame.Color(50, 50, 50), pygame.Rect(width / 2 - 145, 235, 50, 50))
            screen.fill(pygame.Color(0, 204, 102), pygame.Rect(width / 2 - 150, 230, 50, 50))
            screen.blit(right, (width / 2 - 130, 230))
        else:
            screen.fill(pygame.Color(0, 204, 102), pygame.Rect(width / 2 - 145, 235, 50, 50))
            screen.blit(right, (width / 2 - 125, 235))
        # LEFT BUTTON
        left = self.myfont.render(">", True, (0, 0, 0))
        if self.left_shadow:
            screen.fill(pygame.Color(50, 50, 50), pygame.Rect(width / 2 + 105, 235, 50, 50))
            screen.fill(pygame.Color(0, 204, 102), pygame.Rect(width / 2 + 100, 230, 50, 50))
            screen.blit(left, (width / 2 + 120, 230))
        else:
            screen.fill(pygame.Color(0, 204, 102), pygame.Rect(width / 2 + 105, 235, 50, 50))
            screen.blit(left, (width / 2 + 125, 235))

        rules = self.myfont.render("RULES", True, (0, 0, 0))
        if self.rules_shadow:
            screen.fill(pygame.Color(50, 50, 50), pygame.Rect(width / 2 - 145, 325, 300, 50))
            screen.fill(pygame.Color(0, 204, 102), pygame.Rect(width / 2 - 150, 320, 300, 50))
            screen.blit(rules, (width / 2 - 50, 320))
        else:
            screen.fill(pygame.Color(0, 204, 102), pygame.Rect(width / 2 - 145, 325, 300, 50))
            screen.blit(rules, (width / 2 - 45, 325))

        options = self.myfont.render("OPTIONS", True, (0, 0, 0))
        if self.options_shadow:
            screen.fill(pygame.Color(50, 50, 50), pygame.Rect(width / 2 - 145, 415, 300, 50))
            screen.fill(pygame.Color(0, 204, 102), pygame.Rect(width / 2 - 150, 410, 300, 50))
            screen.blit(options, (width / 2 - 70, 410))
        else:
            screen.fill(pygame.Color(0, 204, 102), pygame.Rect(width / 2 - 145, 415, 300, 50))
            screen.blit(options, (width / 2 - 65, 415))


class Room():
    def __init__(self):
        self.hole_found = False
        self.back_shadow = True

    def draw_room(self, level):
        self.myfont = pygame.font.SysFont('Comic Sans MS', 25)
        screen.fill(pygame.Color(255, 204, 255))
        screen.fill(pygame.Color('black'), pygame.Rect(0, 160, 170, 20))  # верхн€€ лева€ платформа
        screen.fill(pygame.Color('black'), pygame.Rect(width - 170, 160, 170, 20))  # верхн€€ права€ платформа
        screen.fill(pygame.Color('black'), pygame.Rect(525, 150, 170, 20))  # верхн€€ центральна€ платформа
        screen.fill(pygame.Color('black'), pygame.Rect(525, 400, 170, 20))
        screen.fill(pygame.Color('black'), pygame.Rect(275, 275, 170, 20))  # средн€€ лева€ платформа
        screen.fill(pygame.Color('black'), pygame.Rect(775, 275, 170, 20))  # средн€€ права€ платформа
        screen.fill(pygame.Color('black'), pygame.Rect(0, 650, 1200, 20))  # нижн€€ платформа
        screen.fill(pygame.Color('black'), pygame.Rect(0, 400, 170, 20))  # стартова€ платформа

        screen.fill(pygame.Color('black'), pygame.Rect(width - 10, 400, 10, 20))
        screen.fill(pygame.Color('black'), pygame.Rect(width - 170, 400, 90, 20))  # финальна€ платформа
        if not self.hole_found or level != 3:
            screen.fill(pygame.Color('black'), pygame.Rect(width - 100, 400, 90, 20))  # секретный ход

        screen.fill(pygame.Color('black'), pygame.Rect(0, 0, width, 40))  # верхн€€ платформа
        screen.fill(pygame.Color('black'), pygame.Rect(250, 550, 100, 100))  # ступенька на старт
        screen.fill(pygame.Color('black'), pygame.Rect(250, 600, 180, 50))
        if level == 1:
            textsurface = self.myfont.render('Level 1: jump on buttons', True, (255, 255, 255))
            screen.blit(textsurface, (100, 3))
        if level == 2:
            textsurface = self.myfont.render('Level 2: push buttons', True, (255, 255, 255))
            screen.blit(textsurface, (100, 3))
        if level == 3:
            textsurface = self.myfont.render('Level 3: find a secret hole', True, (255, 255, 255))
            screen.blit(textsurface, (100, 3))
        if level == 4:
            textsurface = self.myfont.render('Level 4: give up and relax', True, (255, 255, 255))
            screen.blit(textsurface, (100, 3))
        if level == 5:
            textsurface = self.myfont.render('Level 5: one plus one', True, (255, 255, 255))
            screen.blit(textsurface, (100, 3))

        screen.fill(pygame.Color('black'), pygame.Rect(width - 80, 560, 90, 90))  # блок под финишем
        screen.fill(pygame.Color('black'), pygame.Rect(0, 180, 20, 220))  # входна€ дверь

        # боковые стенки ->
        screen.fill(pygame.Color('black'), pygame.Rect(0, 0, 10, 180))
        screen.fill(pygame.Color('black'), pygame.Rect(1190, 0, 10, 180))
        screen.fill(pygame.Color('black'), pygame.Rect(0, 420, 10, 250))
        screen.fill(pygame.Color('black'), pygame.Rect(1190, 420, 10, 250))

        # лава
        screen.fill(pygame.Color('red'), pygame.Rect(600, floor, 100, 20))
        screen.fill(pygame.Color('red'), pygame.Rect(80, floor, 80, 20))
        screen.fill(pygame.Color('red'), pygame.Rect(width - 200, floor, 120, 20))

        # огонь -> [лагает!!!]
        """
        self.fire = pygame.image.load('./fire1.jpg').convert_alpha()
        self.fire = pygame.transform.scale(self.fire, (140, 160))
        self.fire.set_colorkey((255, 255, 255))
        self.fire_rect = self.fire.get_rect(center=(600, floor - 20))
        screen.blit(self.fire, self.fire_rect)
        self.fire_rect = self.fire.get_rect(center=(630, floor - 20))
        screen.blit(self.fire, self.fire_rect)            
        self.fire_rect = self.fire.get_rect(center=(660, floor - 20))
        screen.blit(self.fire, self.fire_rect)
        self.fire_rect = self.fire.get_rect(center=(690, floor - 20))
        screen.blit(self.fire, self.fire_rect)            
        """
        self.myfont = pygame.font.SysFont('Comic Sans MS', 15)
        back = self.myfont.render('<- BACK', True, (0, 0, 0))
        if self.back_shadow:
            screen.fill(pygame.Color(50, 50, 50), pygame.Rect(15, 15, 75, 20))
            screen.fill(pygame.Color(0, 204, 102), pygame.Rect(10, 10, 75, 20))
            screen.blit(back, (20, 10))
        else:
            screen.fill(pygame.Color(0, 204, 102), pygame.Rect(15, 15, 75, 20))
            screen.blit(back, (25, 15))

    def get_pix_color(self, x, y):
        return screen.get_at((x, y))

    def generate_new_level(self):
        yellow_button.state = False
        blue_button.state = False
        spirit.coords = 80, 320
        self.hole_found = False
        door.state = False


class Button():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.state = False

    def draw_button(self):
        if not self.state:
            screen.fill(pygame.Color(self.color), pygame.Rect(self.x, self.y, 70, 15))
            screen.fill(pygame.Color('grey'), pygame.Rect(self.x - 5, self.y + 10, 80, 5))
        else:
            screen.fill(pygame.Color(self.color), pygame.Rect(self.x, self.y + 5, 70, 10))
            screen.fill(pygame.Color('green'), pygame.Rect(self.x - 5, self.y + 10, 80, 5))

    def change_state(self):
        if not self.state:
            self.state = True
        else:
            self.state = False


class Door():
    def __init__(self):
        self.state = False
        self.coords = width - 120, 180

    def draw_door(self):
        if not self.state:
            screen.fill(pygame.Color('black'), pygame.Rect(self.coords[0], self.coords[1], 20, 220))  # дверь
        screen.fill(pygame.Color(0, 255, 255), pygame.Rect(width - 10, 180, 10, 220))

    def change_state(self):
        self.state = True


class Fire_Spirit():
    def __init__(self):
        self.coords = 80, 320  # координаты центра персонажа
        self.pers = pygame.image.load('./data/pers2.png').convert()
        self.pers.set_colorkey((255, 255, 255))

    def draw_spirit(self):
        # персонаж ->
        self.pers_rect = self.pers.get_rect(center=(self.coords))
        screen.blit(self.pers, self.pers_rect)

    def go_right(self):
        self.coords = self.coords[0] + 3, self.coords[1]

    def go_left(self):
        self.coords = self.coords[0] - 3, self.coords[1]

    def jump(self):
        global height_jump
        if room.get_pix_color(self.coords[0], self.coords[1] - 15) == (255, 204, 255, 255) and\
           room.get_pix_color(self.coords[0] - 25, self.coords[1] - 15) == (255, 204, 255, 255) and\
           room.get_pix_color(self.coords[0] + 25, self.coords[1] - 15) == (255, 204, 255, 255):
            self.coords = self.coords[0], self.coords[1] - 10
        else:
            height_jump = 35

    def fall(self):
        self.coords = self.coords[0], self.coords[1] + 4


def check_if_win():
    global level
    global max_level
    if room.get_pix_color(spirit.coords[0] + 40, spirit.coords[1]) == (0, 255, 255, 255):
        level += 1
        if level > max_level and level != 6:
            max_level = level
        room.generate_new_level()


"""      
class Mouse():
    def __init__(self):
        self.mouse = pygame.image.load('./mouse.png').convert()
        self.mouse.set_colorkey((0, 0, 0))
        pygame.mouse.set_visible(False)
        
    def draw(self):
        self.Mouse_x, self.Mouse_y = pygame.mouse.get_pos()
        if self.Mouse_x > 0 and self.Mouse_x < width and self.Mouse_y > 0 and self.Mouse_y < height:
            screen.blit(self.mouse, (self.Mouse_x, self.Mouse_y)) 
 """


if __name__ == "__main__":
    pygame.init()
    size = width, height = 1200, 700
    screen = pygame.display.set_mode(size)
    level = 1
    loading = True
    max_level = 1
    delay = 5
    menu_on = False
    rules_on = False
    options_on = False
    rules = Rules()
    options = Options()
    floor = 650
    room = Room()
    yellow_button = Button(50, 145, 'yellow')
    blue_button = Button(1080, 145, 'blue')
    spirit = Fire_Spirit()
    running = True
    jump = False
    door = Door()
    load = Load()
    # mouse = Mouse()
    menu = Menu()
    height_jump = 0  # высота прыжка
    while running:
        if loading:
            load.draw()
            pygame.time.delay(5)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYUP or event.type == pygame.MOUSEBUTTONUP:
                    loading = False
                    menu_on = True

        elif menu_on:
            menu.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] >= width / 2 - 150 and\
                   pygame.mouse.get_pos()[0] <= width / 2 + 150 and pygame.mouse.get_pos()[1] >= 150 and\
                   pygame.mouse.get_pos()[1] <= 200:
                    menu.start_shadow = False
                if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pos()[0] >= width / 2 - 150 and\
                   pygame.mouse.get_pos()[0] <= width / 2 + 150 and pygame.mouse.get_pos()[1] >= 150 and\
                   pygame.mouse.get_pos()[1] <= 200:
                    menu_on = False
                    room.generate_new_level()

                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] >= width / 2 - 150 and\
                   pygame.mouse.get_pos()[0] <= width / 2 - 100 and pygame.mouse.get_pos()[1] >= 230 and\
                   pygame.mouse.get_pos()[1] <= 280:
                    menu.right_shadow = False
                if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pos()[0] >= width / 2 - 150 and\
                   pygame.mouse.get_pos()[0] <= width / 2 - 100 and pygame.mouse.get_pos()[1] >= 230 and\
                   pygame.mouse.get_pos()[1] <= 280:
                    if level != 1:
                        level -= 1

                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] >= width / 2 + 100 and\
                   pygame.mouse.get_pos()[0] <= width / 2 + 150 and pygame.mouse.get_pos()[1] >= 230 and\
                   pygame.mouse.get_pos()[1] <= 280:
                    menu.left_shadow = False
                if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pos()[0] >= width / 2 + 100 and\
                   pygame.mouse.get_pos()[0] <= width / 2 + 150 and pygame.mouse.get_pos()[1] >= 230 and\
                   pygame.mouse.get_pos()[1] <= 280:
                    if level != max_level:
                        level += 1

                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] >= width / 2 - 150 and\
                   pygame.mouse.get_pos()[0] <= width / 2 + 150 and pygame.mouse.get_pos()[1] >= 320 and\
                   pygame.mouse.get_pos()[1] <= 370:
                    menu.rules_shadow = False
                if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pos()[0] >= width / 2 - 150 and\
                   pygame.mouse.get_pos()[0] <= width / 2 + 150 and pygame.mouse.get_pos()[1] >= 320 and\
                   pygame.mouse.get_pos()[1] <= 370:
                    menu_on = False
                    rules_on = True

                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] >= width / 2 - 150 and\
                   pygame.mouse.get_pos()[0] <= width / 2 + 150 and pygame.mouse.get_pos()[1] >= 410 and\
                   pygame.mouse.get_pos()[1] <= 460:
                    menu.options_shadow = False
                if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pos()[0] >= width / 2 - 150 and\
                   pygame.mouse.get_pos()[0] <= width / 2 + 150 and pygame.mouse.get_pos()[1] >= 410 and\
                   pygame.mouse.get_pos()[1] <= 460:
                    menu_on = False
                    options_on = True

                if event.type == pygame.MOUSEBUTTONUP:
                    menu.rules_shadow = True
                    menu.options_shadow = True
                    menu.start_shadow = True
                    menu.right_shadow = True
                    menu.left_shadow = True

            # pygame.display.flip()
        elif options_on:

            options.draw()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] >= 20 and\
                   pygame.mouse.get_pos()[0] <= 170 and pygame.mouse.get_pos()[1] >= 20 and\
                   pygame.mouse.get_pos()[1] <= 70:
                    options.back_shadow = False

                if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pos()[0] >= 20 and\
                   pygame.mouse.get_pos()[0] <= 170 and pygame.mouse.get_pos()[1] >= 20 and\
                   pygame.mouse.get_pos()[1] <= 70:
                    options.back_shadow = True
                    options_on = False
                    menu_on = True

                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] >= width / 2 - 150 and\
                   pygame.mouse.get_pos()[0] <= width / 2 - 100 and pygame.mouse.get_pos()[1] >= 230 and\
                   pygame.mouse.get_pos()[1] <= 280:
                    options.right_shadow = False
                if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pos()[0] >= width / 2 - 150 and\
                   pygame.mouse.get_pos()[0] <= width / 2 - 100 and pygame.mouse.get_pos()[1] >= 230 and\
                   pygame.mouse.get_pos()[1] <= 280:
                    if delay != 0:
                        delay -= 1

                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] >= width / 2 + 100 and\
                   pygame.mouse.get_pos()[0] <= width / 2 + 150 and pygame.mouse.get_pos()[1] >= 230 and\
                   pygame.mouse.get_pos()[1] <= 280:
                    options.left_shadow = False

                if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pos()[0] >= width / 2 + 100 and\
                   pygame.mouse.get_pos()[0] <= width / 2 + 150 and pygame.mouse.get_pos()[1] >= 230 and\
                   pygame.mouse.get_pos()[1] <= 280:
                    if delay != 10:
                        delay += 1

                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] >= width / 2 - 150 and\
                   pygame.mouse.get_pos()[0] <= width / 2 + 150 and pygame.mouse.get_pos()[1] >= 320 and\
                   pygame.mouse.get_pos()[1] <= 370:
                    options.open_levels_shadow = False

                if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pos()[0] >= width / 2 - 150 and\
                   pygame.mouse.get_pos()[0] <= width / 2 + 150 and pygame.mouse.get_pos()[1] >= 320 and\
                   pygame.mouse.get_pos()[1] <= 370:
                    options.open_levels_shadow = True
                    options.levels_unlocked = True
                    max_level = 5

                if event.type == pygame.MOUSEBUTTONUP:
                    options.back_shadow = True
                    options.right_shadow = True
                    options.left_shadow = True
                    options.open_levels_shadow = True
            # pygame.display.flip()

        elif rules_on:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] >= 20 and\
                   pygame.mouse.get_pos()[0] <= 170 and pygame.mouse.get_pos()[1] >= 20 and\
                   pygame.mouse.get_pos()[1] <= 70:
                    rules.back_shadow = False

                if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pos()[0] >= 20 and\
                   pygame.mouse.get_pos()[0] <= 170 and pygame.mouse.get_pos()[1] >= 20 and\
                   pygame.mouse.get_pos()[1] <= 70:
                    rules.back_shadow = True
                    rules_on = False
                    menu_on = True

                if event.type == pygame.MOUSEBUTTONUP:
                    rules.back_shadow = True
            rules.draw()
            # pygame.display.flip()
        else:
            ground_color = room.get_pix_color(spirit.coords[0], spirit.coords[1] + 65)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    if (door.state and level == 4) or level != 4:
                        running = False
                    if level == 4:
                        door.change_state()

                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] >= 10 and\
                   pygame.mouse.get_pos()[0] <= 85 and pygame.mouse.get_pos()[1] >= 10 and\
                   pygame.mouse.get_pos()[1] <= 30:
                    room.back_shadow = False

                if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pos()[0] >= 10 and\
                   pygame.mouse.get_pos()[0] <= 85 and pygame.mouse.get_pos()[1] >= 10 and\
                   pygame.mouse.get_pos()[1] <= 30:
                    room.back_shadow = True
                    menu_on = True

                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP and (ground_color != (255, 204, 255, 255) or
                                                                                  room.get_pix_color(spirit.coords[0] - 30, spirit.coords[1] + 65) != (255, 204, 255, 255) or
                                                                                  room.get_pix_color(spirit.coords[0] + 30, spirit.coords[1] + 65) != (255, 204, 255, 255)):
                    jump = True
                    height_jump = 0

                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] >= 50 and\
                   pygame.mouse.get_pos()[0] <= 120 and not yellow_button.state and\
                   pygame.mouse.get_pos()[1] >= 145 and pygame.mouse.get_pos()[1] <= 160 and\
                   level == 2:
                    yellow_button.change_state()

                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pos()[0] >= 1080 and\
                   pygame.mouse.get_pos()[0] <= 1150 and not blue_button.state and\
                   pygame.mouse.get_pos()[1] >= 145 and pygame.mouse.get_pos()[1] <= 160 and\
                   level == 2:
                    blue_button.change_state()

                if event.type == pygame.MOUSEBUTTONUP:
                    room.back_shadow = True
            # дл€ плавного прыжка
            if jump:
                height_jump += 1
                spirit.jump()
                # print(height_jump)
            if height_jump == 35:
                jump = False

            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_LEFT]:
                if spirit.coords[0] - 35 > 0:
                    if room.get_pix_color(spirit.coords[0] - 35, spirit.coords[1] + 55) == (255, 204, 255, 255):
                        spirit.go_left()

            if keystate[pygame.K_RIGHT]:
                if spirit.coords[0] + 40 < width:  # чтоб не сломалось
                    if room.get_pix_color(spirit.coords[0] + 40, spirit.coords[1] + 55) == (255, 204, 255, 255):
                        spirit.go_right()

            if keystate[pygame.K_2] and level == 5:
                door.change_state()

            if ground_color == (255, 204, 255, 255) and\
               room.get_pix_color(spirit.coords[0] + 20, spirit.coords[1] + 65) == (255, 204, 255, 255) and\
               room.get_pix_color(spirit.coords[0] - 20, spirit.coords[1] + 65) == (255, 204, 255, 255):
                spirit.fall()

            if spirit.coords[0] >= 50 and spirit.coords[0] <= 120 and\
               ground_color == (255, 255, 0, 255) and not yellow_button.state and level != 2:
                yellow_button.change_state()

            if spirit.coords[0] >= 1080 and spirit.coords[0] <= 1150 and\
               ground_color == (0, 0, 255, 255) and not blue_button.state and level != 2:
                blue_button.change_state()

            if level == 3:
                if spirit.coords[0] >= width - 80 and spirit.coords[1] <= 480 and spirit.coords[1] >= 300:
                    room.hole_found = True
                else:
                    room.hole_found = False

            if room.get_pix_color(spirit.coords[0] + 15, spirit.coords[1] + 65) == (255, 0, 0, 255) or\
               room.get_pix_color(spirit.coords[0] - 15, spirit.coords[1] + 65) == (255, 0, 0, 255):
                room.generate_new_level()
                print('die')

            if blue_button.state and yellow_button.state and (level == 1 or level == 2):
                door.change_state()

            if level != 6:
                room.draw_room(level)
            else:
                menu_on = True
                level = 5
            yellow_button.draw_button()
            blue_button.draw_button()
            spirit.draw_spirit()
            door.draw_door()
            # screen.fill(pygame.Color('grey'), pygame.Rect(spirit.coords[0] + 35, spirit.coords[1] + 65, 80, 5))
            pygame.time.delay(delay)
            # pygame.display.flip()
            check_if_win()
        pygame.display.flip()
    pygame.quit()
