# print(bin(5)) #0b101 (or) 0B101. binary with is divisible with only the 2 table only.
# print(bin(10)) #0B1010
# print(bin(8)) #0b1000
# print(bin(7)) #0b111
# print(bin(1)) #0b1
# print(bin(0)) #0b0
# print(0b101) #5. to check weather the answer 5 is correct or not.


# print(oct(36)) #0o44 (or) 0O44. octal which is divisible with only the 8 table only.
# print(oct(40)) #0o50 (or) 0O50
# print(0o50) #40. to check weather the 40 answer is correct or not


# print(hex(50)) #0x32 (or) 0X32. hexa decimal is divisible with only the 16 table only.
# print(0x32) #50. to check weather the answer 50 is correct or not and its correct.
# print(0xA) #10
# print(0Xb) #11
# print(0Xc) #12
# print(0Xd) #13
# print(0XE) #14
# print(0XF) #15. in hexa decimal till A to F it may be upper case letter or lower case letter it contain some values . and this are taht values.
#this hexa deciamal values contain till A to F. and only in hex method only.

# a="r\tr\tk"
# print(a.expandtabs(0))
# print(a.expandtabs(1))
# print(a.expandtabs(2))
# print(a.expandtabs(3))
# print(a.expandtabs(4))
# print(a.expandtabs(5))
# print(a.expandtabs(6))
# print(a.expandtabs(7))
# print(a.expandtabs(8))
# print(a.expandtabs())
# print(a.expandtabs(9))
# print(a.expandtabs(-1))

""""join"""
# a="hello","python","programming"
# b="rohan"
# print("-".join(a)) #hello-python-programming
# print("*".join(b)) #r*o*h*a*n
# print("$".join("hey")) #h$e$y
 
# "maketrans and translate"
# a="hello helly"
# c=a.maketrans("l",'r')
# print(a.translate(a))
'this above one is not getting perfectly.'

# print("Hello\nRohan") #Hello
#                       #Rohan. \n which means new line or next line

a="hello\npyhton\nprogramming\ncoding"
g=a.splitlines()
# print(g) #["hello",["python"],["programming"],["code"]] split lines which we can divide all the words. and the asnwer will be shown in form of list.
print(g[2]) #programming
print(g[3]) #coding
print(g[4]) #indexerror:list index out of range

