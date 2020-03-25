import sys
import mdpagedl

if __name__ == "__main__":
    # help menu
    if len(sys.argv) == 2 and sys.argv[1] == '-h':
        print('Input $ main.py URL path')
        exit()

    # Arguments check
    if len(sys.argv) != 3:
        print('Argument error')
        exit()

    
    #--------------------------
    # main
    #--------------------------
    
    # read arguments
    url = sys.argv[1]
    path = sys.argv[2]

    mdpagedl.download(url, path)