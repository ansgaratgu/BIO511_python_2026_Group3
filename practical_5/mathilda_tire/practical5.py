#prictical 5
#mathilda järketig 12-10-26

#imports:
import sys

#argumants:

add_text = sys.argv[1]

with open('test1.csv', 'w') as file:
    file.write(",,,,\n,,,,\n,,,,\n,,,,\n,,,,")
   

with open('test1.csv', 'a') as fiel:
    fiel.write("\n")
    fiel.write(add_text)
    fiel.write("\n")

with open('test1.csv', 'r') as fuck:
    fool = fuck.read()
    print(fool)