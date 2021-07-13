#user interface runner

import pygame, pickle
from os import listdir 

from file_path_converter import convert_path

pi = True

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Currier', 25)

display = pygame.display.set_mode((792, 612))

pygame.display.set_caption('Project')

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
key_color = (58, 166, 221)

#Load Database and stuff

print('Loading')

if pi :
    arsenal = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Arsenal.dat'), 'rb'))
    aston_villa = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Aston Villa.dat'), 'rb'))
    brighton_and_hove_albion = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Brighton & Hove Albion.dat'), 'rb'))
    burnley = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Burnley.dat'), 'rb'))
    chelsea = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Chelsea.dat'), 'rb'))
    crystal_palace = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Crystal Palace.dat'), 'rb'))
    everton = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Everton.dat'), 'rb'))
    fulham = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Fulham.dat'), 'rb'))
    leeds_united = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Leeds United.dat'), 'rb'))
    leicester_city = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Leicester City.dat'), 'rb'))
    liverpool = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Liverpool.dat'), 'rb'))
    manchester_city = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Manchester City.dat'), 'rb'))
    manchester_united = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Manchester United.dat'), 'rb'))
    newcastle_united = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Newcastle United.dat'), 'rb'))
    sheffield_united = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Sheffield United.dat'), 'rb'))
    southampton = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Southampton.dat'), 'rb'))
    tottenham_hotspur = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Tottenham Hotspur.dat'), 'rb'))
    west_bromwich_albion = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\West Bromwich Albion.dat'), 'rb'))
    west_ham_united = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\West Ham United.dat'), 'rb'))
    wolverhampton_wanderers = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Wolverhampton Wanderers.dat'), 'rb'))
else :
    arsenal = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Arsenal.dat', 'rb'))
    aston_villa = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Aston Villa.dat', 'rb'))
    brighton_and_hove_albion = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Brighton & Hove Albion.dat', 'rb'))
    burnley = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Burnley.dat', 'rb'))
    chelsea = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Chelsea.dat', 'rb'))
    crystal_palace = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Crystal Palace.dat', 'rb'))
    everton = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Everton.dat', 'rb'))
    fulham = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Fulham.dat', 'rb'))
    leeds_united = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Leeds United.dat', 'rb'))
    leicester_city = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Leicester City.dat', 'rb'))
    liverpool = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Liverpool.dat', 'rb'))
    manchester_city = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Manchester City.dat', 'rb'))
    manchester_united = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Manchester United.dat', 'rb'))
    newcastle_united = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Newcastle United.dat', 'rb'))
    sheffield_united = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Sheffield United.dat', 'rb'))
    southampton = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Southampton.dat', 'rb'))
    tottenham_hotspur = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Tottenham Hotspur.dat', 'rb'))
    west_bromwich_albion = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\West Bromwich Albion.dat', 'rb'))
    west_ham_united = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\West Ham United.dat', 'rb'))
    wolverhampton_wanderers = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Wolverhampton Wanderers.dat', 'rb'))

print('done')

print(aston_villa)
quit()

#Saves Screen Stuff

save_number = 0

def get_save_image(save_number) :
    path = ''.join(['C:\\Users\\rhyde23\\Desktop\\Project\\Images\\', 'Save', str(save_number), '.png'])
    if pi :
        path = convert_path(path)
    return pygame.image.load(path).convert()

save_background_images = []
for i in range(10) :
    current_save_image = get_save_image(i+1)
    save_background_images.append(current_save_image)

current_save_image = save_background_images[save_number]

save_names = []
for i in range(10) :
    path = ''.join(['C:\\Users\\rhyde23\\Desktop\\Project\\Saves\\', 'File', str(i+1), 'BasicInfo.dat'])
    if pi :
        path = convert_path(path)
    basic_info = pickle.load(open(path, 'rb'))
    save_names.append(basic_info['SaveName'])

save_names_texts = []
for save_name in save_names :
    save_names_texts.append(myfont.render(save_name, True, (0, 0, 0)))
    
clicker_mode = False
current_clicked = (0, 0)


y_difference = 37
x_start, x_end = 43, 761
buttons = []
for i in range(10) :
    first_y = 154+(i*y_difference)
    second_y = first_y+y_difference
    buttons.append([first_y, second_y])

print(buttons)

offset = [12, 13, 14, 16, 17, 19, 20, 22, 23, 25]


save_selected = None
#####

#Name Save Stuff

if not pi :
    keyboard_order = {
        pygame.K_m:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-002.png').convert(),
        pygame.K_n:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-003.png').convert(),
        pygame.K_b:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-004.png').convert(),
        pygame.K_v:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-005.png').convert(),
        pygame.K_c:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-006.png').convert(),
        pygame.K_x:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-007.png').convert(),
        pygame.K_z:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-008.png').convert(),
        pygame.K_l:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-009.png').convert(),
        pygame.K_k:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-010.png').convert(),
        pygame.K_j:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-011.png').convert(),
        pygame.K_h:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-012.png').convert(),
        pygame.K_g:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-013.png').convert(),
        pygame.K_f:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-014.png').convert(),
        pygame.K_d:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-015.png').convert(),
        pygame.K_s:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-016.png').convert(),
        pygame.K_a:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-017.png').convert(),
        pygame.K_p:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-018.png').convert(),
        pygame.K_o:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-019.png').convert(),
        pygame.K_i:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-020.png').convert(),
        pygame.K_u:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-021.png').convert(),
        pygame.K_y:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-022.png').convert(),
        pygame.K_t:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-023.png').convert(),
        pygame.K_r:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-024.png').convert(),
        pygame.K_e:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-025.png').convert(),
        pygame.K_w:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-026.png').convert(),
        pygame.K_q:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-027.png').convert(),
        pygame.K_DELETE:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-028.png').convert(),
        pygame.K_0:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-029.png').convert(),
        pygame.K_9:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-030.png').convert(),
        pygame.K_8:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-031.png').convert(),
        pygame.K_7:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-032.png').convert(),
        pygame.K_6:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-033.png').convert(),
        pygame.K_5:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-034.png').convert(),
        pygame.K_4:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-035.png').convert(),
        pygame.K_3:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-036.png').convert(),
        pygame.K_2:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-037.png').convert(),
        pygame.K_1:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-038.png').convert(),
    }
    
if pi :
    keyboard_order = {
        pygame.K_m:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-002.png')).convert(),
        pygame.K_n:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-003.png')).convert(),
        pygame.K_b:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-004.png')).convert(),
        pygame.K_v:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-005.png')).convert(),
        pygame.K_c:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-006.png')).convert(),
        pygame.K_x:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-007.png')).convert(),
        pygame.K_z:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-008.png')).convert(),
        pygame.K_l:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-009.png')).convert(),
        pygame.K_k:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-010.png')).convert(),
        pygame.K_j:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-011.png')).convert(),
        pygame.K_h:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-012.png')).convert(),
        pygame.K_g:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-013.png')).convert(),
        pygame.K_f:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-014.png')).convert(),
        pygame.K_d:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-015.png')).convert(),
        pygame.K_s:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-016.png')).convert(),
        pygame.K_a:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-017.png')).convert(),
        pygame.K_p:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-018.png')).convert(),
        pygame.K_o:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-019.png')).convert(),
        pygame.K_i:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-020.png')).convert(),
        pygame.K_u:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-021.png')).convert(),
        pygame.K_y:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-022.png')).convert(),
        pygame.K_t:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-023.png')).convert(),
        pygame.K_r:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-024.png')).convert(),
        pygame.K_e:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-025.png')).convert(),
        pygame.K_w:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-026.png')).convert(),
        pygame.K_q:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-027.png')).convert(),
        pygame.K_DELETE:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-028.png')).convert(),
        pygame.K_0:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-029.png')).convert(),
        pygame.K_9:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-030.png')).convert(),
        pygame.K_8:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-031.png')).convert(),
        pygame.K_7:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-032.png')).convert(),
        pygame.K_6:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-033.png')).convert(),
        pygame.K_5:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-034.png')).convert(),
        pygame.K_4:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-035.png')).convert(),
        pygame.K_3:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-036.png')).convert(),
        pygame.K_2:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-037.png')).convert(),
        pygame.K_1:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-038.png')).convert(),
    }

keyboard_letters = {
    pygame.K_m:'M',
    pygame.K_n:'N',
    pygame.K_b:'B',
    pygame.K_v:'V',
    pygame.K_c:'C',
    pygame.K_x:'X',
    pygame.K_z:'Z',
    pygame.K_l:'L',
    pygame.K_k:'K',
    pygame.K_j:'J',
    pygame.K_h:'H',
    pygame.K_g:'G',
    pygame.K_f:'F',
    pygame.K_d:'D',
    pygame.K_s:'S',
    pygame.K_a:'A',
    pygame.K_p:'P',
    pygame.K_o:'O',
    pygame.K_i:'I',
    pygame.K_u:'U',
    pygame.K_y:'Y',
    pygame.K_t:'T',
    pygame.K_r:'R',
    pygame.K_e:'E',
    pygame.K_w:'W',
    pygame.K_q:'Q',
    pygame.K_0:'0',
    pygame.K_9:'9',
    pygame.K_8:'8',
    pygame.K_7:'7',
    pygame.K_6:'6',
    pygame.K_5:'5',
    pygame.K_4:'4',
    pygame.K_3:'3',
    pygame.K_2:'1',
    pygame.K_1:'1',
}

current_typed = ''

if pi :
    default_typed_screen = pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-001.png')).convert()

if not pi :
    default_typed_screen = pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-001.png').convert()

current_typed_screen = default_typed_screen

space_bar_down = False

#####
    
manager_loop = True
saves_menu = True
name_save = False




while manager_loop :
    while saves_menu :
        display.fill(white)
        display.blit(current_save_image, (0, 0))
        display.set_at(current_clicked, red)
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get() :
            if event.type == pygame.MOUSEBUTTONDOWN :
                coords = pygame.mouse.get_pos()
                if clicker_mode :
                    current_clicked = coords
                save_selected = save_number
                print(save_selected)
                saves_menu = False
                name_save = True
                
        
        for i, save_name_text in enumerate(save_names_texts) :
            text_y = buttons[i][0]+offset[i]
            display.blit(save_name_text, (100, text_y))
            
        if x >= x_start and x <= x_end :
            for i, button in enumerate(buttons) :
                if y >= button[0] and y <= button[1] :
                    save_number = i
                    current_save_image = save_background_images[save_number]
        pygame.display.update()
    while name_save :
        display.fill(white)
        display.blit(current_typed_screen, (0, 0))
        for event in pygame.event.get() :
            if event.type == pygame.MOUSEBUTTONDOWN :
                coords = pygame.mouse.get_pos()
            if event.type == pygame.KEYDOWN :
                key = event.key
                if key == pygame.K_SPACE :
                    space_bar_down = True
                else :
                    current_typed_screen = keyboard_order[key]
            if event.type == pygame.KEYUP :
                if key == pygame.K_SPACE :
                    space_bar_down = False
                current_typed_screen = default_typed_screen
        
        if space_bar_down :
            pygame.draw.rect(display, key_color, pygame.Rect(240, 505, 315, 50))
        else :
            pygame.draw.rect(display, white, pygame.Rect(240, 505, 315, 50))
        pygame.display.update()
        
        

