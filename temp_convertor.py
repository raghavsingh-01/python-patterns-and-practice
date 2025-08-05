#This program of temperature convertor convert the °C to Kelvin or Fahreinheit

def temp_conv(temp) :
    unW = input("Enter the first letter of desired uint i.e, 'f' or 'k' :")
    if unW == 'f' :
        cal=((temp/5)*9)+32
        un = "Fahrenheit"
    elif unW == 'k' :
        cal=temp+273.15
        un = "Kelvin"
    else :
        print("Your entered unit is not in system !")
    print(temp,"Celsius","=", cal, un)
    
i=int(input("Enter the temperature in °Celsius :"))
temp_conv(i)