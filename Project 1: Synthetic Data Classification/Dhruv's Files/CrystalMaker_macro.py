#Macro script which automatically generates diffraction profiles in a given range using CrystalMaker 
import mouse
import keyboard
import time
import pyautogui


#sets up adjustment values for custom screen sizes
screen_size_x = pyautogui.size()[0]
screen_size_y = pyautogui.size()[1]

x_adjust = screen_size_x/1366
y_adjust = screen_size_y/768


#list of coordinates to move to/actions to take
coords_to_move = [(248, 41),(272, 294),(935, 472),(891, 318),(935, 472),(887, 342),(943, 532),(470, 41),(546, 307),(270, 164),(501, 353),(605, 394),(579, 529),(752, 600),(1107, 136)]
action_on_click = ["C","C",'C','T','C','T',"C","C","C_wait","C","C","CC",'S',"C","C",]


start_val = float(input("what uiso val to start from? (e.g. 0.0, 1.0) "))
end_val = float(input("what uiso val to go up to? (e.g. 0.1 or 2.5) "))
increment = float(input("What increments? (e.g. 0.05)"))

#counts down from 5 before starting program
print("please open up crystal maker and crystal diffract in advance, with the crystal file loaded. Also, electron diffraction must already be set as default for this script to work properly.")

#adds relevant uiso values to a list
for i in range(5,0,-1):
    print("starting in: " + str(i))
    time.sleep(1)

uiso_to_scan = [round(i*increment,4) for i in range(int(start_val/increment),int(end_val/increment)+1,1)]

#converts each uiso value into a file name as well
uiso_to_scan_str = ["Bi_mp-23152_computed Profile_"+str(i) for i in uiso_to_scan]


#iterates through each uiso value
for index in range(0,len(uiso_to_scan)):
    uiso = uiso_to_scan[index]
    uiso_str = uiso_to_scan_str[index]

    #goes through each action
    for coord_index in range(0,len(coords_to_move)):
        coord = coords_to_move[coord_index]
        action = action_on_click[coord_index]
        mouse.move(int(x_adjust*coord[0]),int(y_adjust*coord[1]))
        time.sleep(2)
        
        #acts different based on the 'action' label for the coordinate
        if action == "C_wait":
            #click + wait
            mouse.click()
            if index < 3:
                #crystal diffract takes longer to load on the first few calls
                time.sleep(15)
            else:
                time.sleep(8)
        if action == "C":
            #click
            mouse.click()
        elif action == "T":
            #type number
            mouse.click()
            time.sleep(1)
            mouse.click()
            time.sleep(1)
            keyboard.write(str(uiso))         
        elif action == "CC":
            #click, wait, click
            mouse.click()
            time.sleep(1)
            keyboard.press_and_release("delete")
            #mouse.click()
        elif action == "S":
            #type string
            mouse.click()
            keyboard.write(uiso_str)
