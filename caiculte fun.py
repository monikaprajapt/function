def calculator(number_x,number_y,operation):
    if operation=="+":
        return(number_x+number_y)
    elif operation=="-":
        return(number_x-number_y)
    elif operation=="*":
        return(number_x*number_y)
    elif operation=="/":
        return(number_x/number_y)
number2=(calculator(20,25,"+"))
print(number2)
number3=(calculator(90,23,"-"))
print(number3)
number4=(calculator(50,60,"*")) 
print(number4)
number5=(calculator(80,120,"/"))
print(number5)