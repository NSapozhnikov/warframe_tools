from PIL import ImageGrab
import pyautogui
import time

### function to check if RGB is white (r,g,b > 220)
### compare each element of a RBG tuple with 220
### arguments are:
### RGB - (r,g,b) - color code
def is_white(RGB):
    if RGB[0] > 220 and RGB[1] > 220 and RGB[2] > 220:
        return True
    else:
        return False          
        
### fonction to check how many white sticks there is
### arguments are:
### hexagone - [(x1,y1),(x2,y2),...,(x6,y6)] - coords of white sticks to check
def check_figure(hexagone):
    counter = 0
    idx = []
    for stick_idx, stick in enumerate(hexagone):
        if is_white(stick):
            idx.append(stick_idx)
            counter += 1
    return counter, idx             
        
### function to click mouse on coords of a hexa center
### arguments are:
### coords - (x,y) to click on
### l_r - 'left'/'right' for LMB/RMB
### x - times to click
def mouse_click(coords,l_r,x):
#     x = coords[0]
#     y = coords[1]      
#     for i in range(x):
#         pyautogui.click(x=x, y=y,button=l_r)
#         time.sleep(15)
    print(f"click on {coords} with {l_r} MB {x} times")

### dictionary contains list of tuples (x,y) for correct positions anti-clockwise 
### (first 3 tuples are coordinats of correct positions)
### center coords start with top_left
dict_positions = {'top_left':[(2351,727),(2501,732),(2584,585),(2509,443),(2361,448),(2281,590)],
                  'left':[(2288,1098),(2361,973),(2292,836),(2154,829),(2089,955),(2152,1088)],
                  'bottom_left':[(2558,1374),(2487,1231),(2342,1213),(2270,1335),(2340,1473),(2478,1496)],
                  'bottom_right':[(2945,1280),(2770,1262),(2683,1392),(2755,1543),(2930,1570),(3025,1435)],
                  'right':[(3035,860),(2935,1008),(3021,1170),(3211,1190),(3322,1036),(3230,868)],
                  'top_right':[(2712,586),(2788,738),(2970,740),(3070,580),(2985,423),(2804,430)],
                  'center':[(2560,844),(2480,985),(2548,1128),(2710,1140),(2800,1000),(2722,855)]}
# dictionary contains list of tuples (x,y) for hexagon centers to click on
dict_cents = {'top_left':(2430,590),
              'left':(2220,965),
              'bottom_left':(2410,1360),
              'bottom_right':(2850,1415),
              'right':(3125,1025),
              'top_right':(2885,583),
              'center':(2633,991)}
              
### function to grab a screenshot
### *not implemented* arguments:
### faction - 'corpus'/'greneer'/'orokin'/'narmer'
### returns screen_dict - dictionary with RGB tuples for pre-specified faction unique pixels
# def grab_screenshot():
    ### Corpus
    ###########
    ### Greneer
    ###########
    ### Orokin
    ###########
    ### Narmer
    ###########
time.sleep(5)
## Capture the screen or a specific region
## and conform 2 dicts with RGBs
screenshot = ImageGrab.grab()
screen_dict = {'top_left':[],
               'left':[],
               'bottom_left':[],
               'bottom_right':[],
               'right':[],
               'top_right':[],
               'center':[]}
screen_dict_cents = {'top_left':[],
                     'left':[],
                     'bottom_left':[],
                     'bottom_right':[],
                     'right':[],
                     'top_right':[],
                     'center':[]}
for i in dict_positions:
    for j in dict_positions[i]:
        # Define the coordinates of the pixel you want to retrieve
        x = j[0]
        y = j[1]
        pixel_color = screenshot.getpixel((x, y))
        screen_dict[i].append(pixel_color)
    # Define the coordinates of the pixel you want to retrieve
    x = dict_cents[i][0]
    y = dict_cents[i][1]
    pixel_color = screenshot.getpixel((x, y))
    screen_dict_cents[i].append(pixel_color)
print(screen_dict)
print(screen_dict_cents)
# return screen_dict, screen_dict_cents 

### LMB - clockwise; RMB - anti-clockwise 
### indeces of 'whites' are starting with 0 and continuing anti-clockwise. And 1 is always the stick to the center
##################################################################################################################
### make a screenshot
# screen_dict, screen_dict_cents = grab_screenshot()
### list of wide-angled hexa's
wide_angles = []
### list of sharp-angled hexa's
sharp_angles = []
### list of 1-stick hexa's
_1_stick = []
# hexa_s = 0
# ### count hexa's to solve unique 2-hexa and 3-hexa
# for hexa_id, hexa in enumerate(dict_cents):
#     ### if center is white then there is a moveable hexa    
#     if is_white(screen_dict_cents[hexa][0]):
#         hexa_s += 1
    
for hexa_id, hexa in enumerate(dict_cents):
    ### if center is white then there is a moveable hexa    
    if is_white(screen_dict_cents[hexa][0]):
        ### get number and indeces of "whites"
        counter, idx = check_figure(screen_dict[hexa])
        ### firstly, we rotate all wide-angles, as they can be adjusted only for one possible position
        ### for a 3-sticks or a wide-angle
        ### if difference between indeces > 1 or == 5, then it's a wide-angle 
        print(idx)
        if counter == 3 or (counter == 2 and (idx[1]-idx[0] > 1 or idx[1]-idx[0] == 5)):
            print(f"{hexa} is a 3-sticks or a wide-angle") 
            ### add a hexa id to the list, so sharp-angles and 1-sticks could be adjusted
            wide_angles.append(hexa_id)
            ### if 'white' are 0,1,2 - it is the right position
            if idx == [0,1,2] or idx == [0,2]:
                print('right position')
            ### if 'white' are 1 RMB away
            elif idx == [1,2,3] or idx == [1,3]:
                mouse_click(dict_cents[hexa],'left', 1)
            ### if 'white' are 1 LMB away:
            elif idx == [0,1,5] or idx == [1,5]:
                mouse_click(dict_cents[hexa],'right', 1)
            ### if 'white' are 2 RMB away:
            elif idx == [2,3,4] or idx == [2,4]:
                mouse_click(dict_cents[hexa],'left', 2)
            ### if 'white' are 2 LMB away:
            elif idx == [0,4,5] or idx == [0,4]:
                mouse_click(dict_cents[hexa],'right', 2) 
            ### if 'white' are 3 LMB away:
            elif idx == [3,4,5] or idx == [3,5]:
                mouse_click(dict_cents[hexa],'left', 3)
        ### then we rotate sharp-angles so 1 stick is always positioned on index 1 (facing center hexa)
        ### and the other stick facing the closest wide-angle or the opposite
        ### for a sharp-angle
        elif counter == 2 and (idx[1]-idx[0] == 1 or idx[1]-idx[0] == 5):
            print(f"{hexa} is a sharp-angle")
            ### add a hexa id to the list, so sharp-angles and 1-sticks could be adjusted
            sharp_angles.append(hexa_id)
            ### if the previous hexa is not a wide-angle, the then next must be
            if (not wide_angles) or (hexa_id - wide_angles[-1] != 1):
                ### if 'white' are 0,1 - it is the right position
                if idx == [0,1]:
                    print('right position')
                ### if 'white' are 1 RMB away
                elif idx == [0,5]:
                    mouse_click(dict_cents[hexa],'right', 1)
                ### if 'white' are 1 LMB away
                elif idx == [1,2]:
                    mouse_click(dict_cents[hexa],'left', 1)
                ### if 'white' are 2 RMB away
                elif idx == [4,5]:
                    mouse_click(dict_cents[hexa],'right', 2)
                ### if 'white' are 2 LMB away
                elif idx == [2,3]:
                    mouse_click(dict_cents[hexa],'left', 2)
                ### if 'white' are 3 LMB away
                elif idx == [3,4]:
                    mouse_click(dict_cents[hexa],'left', 3)
            else:
                ### if the previous hexa is a wide-angle
                if hexa_id - wide_angles[-1] == 1:
                ### if 'white' are 1,2 - it is the right position
                    if idx == [1,2]:
                        print('right position')
                    ### if 'white' are 1 RMB away
                    elif idx == [0,1]:
                        mouse_click(dict_cents[hexa],'right', 1)
                    ### if 'white' are 1 LMB away
                    elif idx == [2,3]:
                        mouse_click(dict_cents[hexa],'left', 1)
                    ### if 'white' are 2 RMB away
                    elif idx == [0,5]:
                        mouse_click(dict_cents[hexa],'right', 2)
                    ### if 'white' are 2 LMB away
                    elif idx == [3,4]:
                        mouse_click(dict_cents[hexa],'left', 2)
                    ### if 'white' are 3 LMB away
                    elif idx == [4,5]:
                        mouse_click(dict_cents[hexa],'left', 3)                  
                
        ### then we rotate 1-sticks so it is positioned to the nearest wide- or sharp-angle if any
        ### else it is rotated to the 1st index (to the center)
        
        ### finally we rotate the center hexa
              
                    
                
                
                
            
            
            
            

            
            


            
        
        
