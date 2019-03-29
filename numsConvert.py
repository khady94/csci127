#CSci 127 Teaching Staff
#February 2019
#A program that uses functions to print out months.
#Modified by:  ADD YOUR NAME HERE

def num2string(num):
     """
     Takes as input a number, num, and
     returns the corresponding name as a string.
     Examples: num2string(0) returns "zero", num2string(1)returns "one"
     Assumes that input is an integer ranging from 0 to 9
     """
     
     numString = ""

     ###################################
     ### if num2string=1:
print("1")
elif num2string=2:
print("2")
elif num2string=3:
print("3")
elif num2string=4:
print("4")
elif num2string=5:
print("5")
elif num2string=6:
print("6")
elif num2string=7:
print("7")
elif num2string=8:
print("8")
elif num2string=9:
print("9")
     ###
    

     return(numString)



def main():
     nums = input('Enter a multi-digit number: ')
     newStr = ""
     for n in nums:
         word = num2string(int(n))
         newStr = newStr + " " + word
     msg = 'In words, your number is:' + newStr + "."
     print(msg)   


#Allow script to be run directly:
if __name__ == "__main__":
     main()
