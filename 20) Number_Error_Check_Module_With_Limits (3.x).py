
###### Example of Error checking Module ######

## Make a module called Chk_Number ##
def Chk_Number(item,limit):  ### Store the first thing passes to this module as the variable "Item" and the second thing as "Limit"
        while True:
                enter_number = input("Please enter the quantity of "+(item)+"(s) you would like to order: ") # ask the user to enter the Item Note that the name of the Item is already passed to it so you can use the same module.
                try: #trys the following code first.
                        number = int(enter_number)#Attempts to change what the user entered into a number, if it is successful it will run the code.

                        #### Now check to see if the Number is between the correct Limit ###
                        if number <= limit:
                                break
                        else:
                                print("Please enter a valid number between 0 and "+str(limit))
                except ValueError:
                        print("That is Invalid Please Try again")#if it could not change it into a number it will display this error.
                        
        return number  ## if the code executes correctly it will pass the value of number back.





## Save into the variable "Fish_Qty" the number passed back and SEND the word "Fish Bites" and SEND the Number you would like as the Limit.
fish_qty = Chk_Number("Fish Bites",7)
print (fish_qty) 

peanut_qty = Chk_Number("Peanut",5)
print (peanut_qty) 

butter_qty = Chk_Number("Butter",4)
print (butter_qty) 
