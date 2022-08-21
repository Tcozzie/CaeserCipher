import string
abc=string.ascii_uppercase

def main():
    start=input("Would you like to encode or decode a message?\n")
    if (start=="encode") or (start=="Encode"):
        userM=input("Message to Encode: ")
        offset=int(input("How many letters do you want to offset your message by?  "))
        encode(userM, offset)
    else:
        userM=input("Message to Decode: ")
        offset=int(input("How much was the message offset by? "))
        decode(userM,offset)
   

def encode(message, offset):
    message=message.upper()
    new=""
    for x in message:
        position=abc.index(x)
        position+=offset
        if(position>25):
            position-=26
            letter_pos=abc[position]
            new+=letter_pos
        else:
            letter_pos=abc[position]
            new+=letter_pos
        
    print("Your encoded message: "+new)


def decode(message,offset):
    message=message.upper()
    new=""
    for x in message:
        position=abc.index(x)
        position -=offset
        if(position<0):
            position+=26
            letter_pos=abc[position]
            new+=letter_pos
        else:
            letter_pos=abc[position]
            new+=letter_pos
            
    print("Your decoded message: "+new)


main()
