from phue import Bridge

# https://github.com/studioimaginaire/phue
# in and for meaning: https://www.quora.com/In-Python-what-does-for-return-and-in-mean
# https://stackoverflow.com/questions/19845924/python-how-to-generate-list-of-variables-with-new-number-at-end
# the hub 192.168.1.107

b = Bridge('192.168.1.107')

b.connect() 
b.get_api()

b.get_light(1, 'on')
b.get_light(1, 'name') 

lights = b.lights

print ("NOTICE: Only 1 light is supported in this script more will be allowed in the future.")
print ("This script is highly work in progress, contact Yusef (YUZi22) on Github if any errors occur")
print()
print ("Please make sure to input the local ip address of your hue hub, and press the button on it before you run this script")
print()

# Print names of all lights connected to hue hub.
for l in lights:
    print ("Lights:")
    print(l.name)
    print()

lselect = input("""Select Light (Top to bottom, has to be a number. Goes like this: light on top of list starts with 1 and as it goes down it will go 2,3,4,5 etc..)

Type here: """)


if lselect == ('1'):
    print ("Light 1 selected")
    print()
    print()
    operation = input("""Select Operation:
1 Brightness 
2 Colour select
3 Turn off
4 Turn on

(1 - 4)

Type here: """)
    
    if operation == ('1'):
        brightsel = input("Input a brightness value (0-255): ")
        brightop = l.brightness = int(brightsel)
        print ("Set brightness of", (l.name), "to", "Brightness:", (brightsel))

    if operation == ('2'):
        colhue = input("Set hue: ")
        colop = b.hue = int(colhue)
        colsat = input("Set saturation: ")
        colsaop = b.saturation = int(colsat)
        print ("Saturation set to", (colsat), "and hue set to", (colhue), "on", (l.name))

    if operation == ('3'):
        b.set_light([(l.name)], 'on', False)
        print ("Turned", (l.name), "off")

    if operation == ('4'):
        b.set_light([(l.name)], 'on', True)
        print ("Turned", (l.name), "on")
        


    



