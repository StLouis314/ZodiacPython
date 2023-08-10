#This is a simple program that ask the user to input their Birth Month & Date
#then returning the users zodiac sign with some basic info.

zodiac = ["Aries","Taurus","Gemini","Cancer","Leo",
          "Virgo","Libra","Scorpio","Sagittarius",  #I created a list of signs
          "Capricorn","Aquarius","Pisces"]

months = ["January","February","March","April","May","June",
          "July","August","September","October","November", #A list of months
          "December"]

element_is = {
    "Aries":"Fire","Taurus":"Earth","Gemini":"Air","Cancer":"Water","Leo":"Fire",
    "Virgo":"Earth","Libra":"Air","Scorpio":"Water","Sagittarius":"Fire",  
    "Capricorn":"Earth","Aquarius":"Air","Pisces":"Water",           
}           #I created a dict of the signs elemental affiliation and attributes                                     
characteristics = {
    "Aries":"loves to be number one!",
    "Taurus":"enjoys relaxing and is good with their finances.",
    "Gemini":"is spontaneous, playful and curious by nature.",
    "Cancer":" is highly intuitive and emotionally driven",
    "Leo":"is passionate, loyal, and highly dramatic,",
    "Virgo":"is logical, practical, and systematic.",
    "Libra":"is balanced, justice defines Libra's energy.",
    "Scorpio":"is courageous and crazy, considered emotionally fueled.",
    "Sagittarius":"loves academia, travel, and being alone",  
    "Capricorn":"is patient and dedicated.",
    "Aquarius":"is considered innovative, progressive, and revolutionary",
    "Pisces":"is the most intuitive, sensitive, and empathetic sign",
}         
          
          #Then continue to the opening "string"

print("------------------------------------")

print("""Hello! Welcome to the Zodiac!\nI need to ask you a 
few questions, then I'll \ntell you the sign you were\nborn in.\n
So Let's Begin!""")

print("------------------------------------")

def get_name():
    """Get users name"""
    name = input("Enter your name:\n>>>")#Prompts the user for three inputs
    return name.title()
name = get_name()

def get_month():
    """Get users month ensuring accurate input."""
    while True:
        print("------------------------------------")
        usr_month = input(f"Hello {name}!\nPlease enter your birth month:\n>>>")
        if usr_month.title() not in months: 
            print("Please enter an actual month (Check your spelling).")
            usr_month = input("Enter your birth month:\n")
        return usr_month.title()

usr_month = get_month()

def get_date():
    """Get day of month user was born, ensuring proper input."""
    while True:
        date = None
        try:
            date = int(input(f"Please enter the day of the month" 
                    " you were born on:\n>>>"))
        except ValueError:
            print("Only enter integers, try again.")
        else:
            return date
your_date = get_date()
print("------------------------------------")

def eval_zod(name,usr_month,your_date): 
    """evaluate the Months/dates to get sign/info"""
    if (usr_month == months[3] and your_date <= 20 
    or usr_month == months[2] and your_date >= 21):
        your_sign = zodiac[0] 
        your_element = element_is['Aries']
        char = characteristics['Aries']
    
    elif (usr_month == months[4] and your_date <= 20
     or usr_month == months[3] and your_date >= 20):
        your_sign = zodiac[1]
        your_element = element_is['Taurus']
        char = characteristics['Taurus']

    elif (usr_month == months[5] and your_date <= 20 
    or usr_month == months[4] and your_date >= 21):
        your_sign = zodiac[2]
        your_element = element_is['Gemini']
        char = characteristics['Gemini']

    elif (usr_month == months[6] and your_date <= 22 
    or usr_month == months[5] and your_date >= 21):
        your_sign = zodiac[3]
        your_element = element_is['Cancer']
        char = characteristics['Cancer']

    elif (usr_month == months[7] and your_date <= 22 
    or usr_month == months[6] and your_date >= 23):
        your_sign = zodiac[4]
        your_element = element_is['Leo']
        char = characteristics['Leo']

    elif (usr_month == months[8] and your_date <= 22 
    or usr_month == months[7] and your_date >= 23):
        your_sign = zodiac[5]
        your_element = element_is['Virgo']
        char = characteristics['Virgo']

    elif (usr_month == months[9] and your_date <= 22 
    or usr_month == months[8] and your_date >= 23):
        your_sign = zodiac[6]
        your_element = element_is['Libra']
        char = characteristics['Libra']

    elif (usr_month == months[10] and your_date <= 21 
    or usr_month == months[9] and your_date >= 23):
        your_sign = zodiac[7]
        your_element = element_is['Scorpio']
        char = characteristics['Scorpio']

    elif (usr_month == months[11] and your_date <= 21 
    or usr_month == months[10] and your_date >= 22):
        your_sign = zodiac[8]
        your_element = element_is['Sagittarius']
        char = characteristics['Sagittarius']

    elif (usr_month == months[0] and your_date <= 19 
    or usr_month == months[11] and your_date >= 22):
        your_sign = zodiac[9]
        your_element = element_is['Capricorn']
        char = characteristics['Capricorn']

    elif (usr_month == months[1] and your_date <= 18 
    or usr_month == months[0] and your_date >= 20):
        your_sign = zodiac[10]
        your_element = element_is['Aquarius']
        char = characteristics['Aquarius']

    elif (usr_month == months[2] and your_date <= 21
    or usr_month == months[1] and your_date >= 19):
        your_sign = zodiac[11]
        your_element = element_is['Pisces']
        char = characteristics['Pisces']
    
    else:
        None
    
    print("------------------------------------")
    print(f"Guess what {name}, your zodiac sign is {your_sign}!")
    print(f"{your_sign} is associated with the element of {your_element}.")
    print(f"Your sign {char} ")
    print("------------------------------------")
    

eval_zod(name,usr_month,your_date)







