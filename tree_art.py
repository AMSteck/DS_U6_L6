##### Global color variables #####
from colorama import Fore
R = Fore.RED
G = Fore.GREEN
B = Fore.BLUE
W = Fore.RESET
P = Fore.CYAN

'''IF COLORAMA NOT FOUND - ENTER INTO TERMINAL:
pip install colorama'''
##################################

def VIEW_tree0():
    print("~" * 50)
    print(f"{P}This is what your tree looks like{W}\n")

    print("""
              (11)
            /     \\
          (1)      (16)
            \\     /  \\
            (7) (13)  (24)
                /     /
              (12)  (19)
    
    """)

def VIEW_tree1():
    print("~" * 50)
    print(f"{P}This is what your tree looks like{W}\n")

    print("""
              (11)
            /     \\
          (1)      (16)
            \\     /  \\
            (7) (13)  (24)
                      /
                    (19)
    
    """)


def VIEW_tree2():
    print("~" * 50)
    print(f"{P}This is what your tree looks like{W}\n")

    print("""
              (11)
             /    \\
           (7)     (16)
                   /  \\
                (13)  (19)
              
    
    """)