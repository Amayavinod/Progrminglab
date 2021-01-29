str=input("enter a string")
print("entered string is=",str)
char=str[0]
replace_str=str.replace(char,'$')
str1=char+replace_str[1:]
print("modifyed string=",str1)
