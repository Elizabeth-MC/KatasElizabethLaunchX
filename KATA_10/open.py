"""def main():
    open("/path/to/mars.jpg")

if __name__ == '__main__':
    main()"""

#Salida

"""
Traceback (most recent call last):
  File "c:/Users/Elizabeth/Documents/LAUNCH X/ProgramasPython/EJERCICIOS/open.py", line 5, in <module>
    main()
  File "c:/Users/Elizabeth/Documents/LAUNCH X/ProgramasPython/EJERCICIOS/open.py", line 2, in main
    open("/path/to/mars.jpg")
FileNotFoundError: [Errno 2] No such file or directory: '/path/to/mars.jpg'

"""

try:
     open("mars.jpg")
except FileNotFoundError as err:
    print("got a problem trying to read the file:", err)
