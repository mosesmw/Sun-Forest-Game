print('''
                              *
                   *          *       **                 *
                    *        **       **               **
                     **      *       ***              **
                      ***    *       **             ***
                       ***    *     ****           ***
                        ****                     ****
     **                  *    ********* *        ***
       *****              **********************
         ********        ***************      ****
             ******    *****************         **                 **
                **    *******************         ***       ********
                     ********************           ***  *******
                    *********************            ***  **         ****
  ********* *      ***********************            ***         ****
     **********   ************************        **** **       ***
          ****    ***********************       *     ****
                  **************  ******       *  *** * **
                   ***********  **   ****       * *** *  **   ********** *
                *************  *****  *****     **   *   **   ****** *
            *   *************  ****  *******      ***    **
************** ****************    ***********           **
       ******   *******************************           **
                *********************************         **
                ********************************          **   **
                *******************************           **  *********
          ****  ***************************              ***         *****
     ***** *     ***  ********************                **
 *****         *       *****************                 **    ******
             ****      *********************             *         *****
          *****          ******************             **
        ****               ****************             *    *****
       *                   *****************           **      ******
                           **  **************         **             **
                           **    *************        *
                          ***     *************      **
                       * ***        *********************
                      ******           ******* * ***   ***
                      *******                      **   ***
                      ************                  ********
                     ********************** *     **********
                      *************************   ***********
                     **************************   ***********
                      *************************   ***********
                       ************************   **********
                         *********************    *********
                              ****************      ***
                                      * ******
''')
print("Welcome to the Sun's Forest.")
print("Your mission is to find the treasure.")

answer = input("You are in a dark forest. Go 'left' or 'right'?:\n").lower()
if answer == "left":
    print("You find a clearing. You are safe... for now.")

    action = input("You see a bear sleeping. Type 'sneak' or 'run':\n").lower()
    if action == "sneak":
        print("You successfully snuck past the bear")
    else:
        print("You woke up the bear and it diminished your life force instantly."
              " Game Over.")
else:
    print("You fell into a pit of snakes. Game Over.")

print("You reach the temple in the middle of the forest.")
choice = input("The temple itself is wide with three doors and three symbols above."
           " Type 'lion' 'seal' or 'hawk' to choose your door:\n").lower()
if choice == "lion":
    print("The ground around you begins to crumble as you fall into a lion pit."
          " Game Over.")
elif choice == "seal":
    print("The door bursts open as water seeps you away and you fade into obscurity."
          " Game Over.")
else:
    print("You chose the door with a Hawk."
          " You notice a shadow fly over as the door opens. Inside lays the treasure.\nYou win!")
