print("\n")
print("Recursive Desent Parsing For Following Grammar\n")
print("E->iE'\nE'->+iE'/e\n") 
print("For above grammar, small letter 'e' represents epsilon. Now,\n")
print("Enter the string want to be checked:\n")

global s
s=list(input())
global i
i=0
def match(a):
    global s
    global i
    if(i>=len(s)):
        return False
    elif(s[i]==a):
        i+=1
        return True
    else:
        return False

def Ex():
    if(match("+")):
        if(match("i")):
            if(Ex()):
                return True
            else:
                return False
        else:
            return False
    else:
        return True

def E():  
    if(match("i")):
        if(Ex()):
            return True
        else:
            return False
    else:
        return False
   
if(E()):
    if(i==len(s)):
        print("String is accepted")
    else:
        print("String is not accepted")
    
else:
    print("string is not accepted")