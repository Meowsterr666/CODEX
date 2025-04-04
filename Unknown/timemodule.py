import time

def custom_keyboard_interrupt_handler():
    print(r"""
   ('-.  ) (`-.              .-') _               .-') _                  
 _(  OO)  ( OO ).           (  OO) )             ( OO ) )                 
(,------.(_/.  \_)-. ,-.-') /     '._ ,-.-') ,--./ ,--,'  ,----.          
 |  .---' \  `.'  /  |  |OO)|'--...__)|  |OO)|   \ |  |\ '  .-./-')       
 |  |      \     /\  |  |  \'--.  .--'|  |  \|    \|  | )|  |_( O- )      
(|  '--.    \   \ |  |  |(_/   |  |   |  |(_/|  .     |/ |  | .--, \      
 |  .--'   .'    \_),|  |_.'   |  |  ,|  |_.'|  |\    | (|  | '. (_/      
 |  `---. /  .'.  \(_|  |      |  | (_|  |   |  | \   |  |  '--'  |.-..-. 
 `------''--'   '--' `--'      `--'   `--'   `--'  `--'   `------' `-'`-' 

          """)

try:
    print("Press Ctrl+C:")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    custom_keyboard_interrupt_handler()
print("That's all folks,")

"""
Time seems to give the program time, essentially,
to wait for any exceptions; hence: except KeyboardInterrupt
"""