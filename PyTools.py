import random

# Function to generate a random password with at least one character from each class

def random_password_gen( password_length=25):
    character_classes = ['uppercase', 'lowercase', 'digits', 'special_characters']
    alphabet_lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    special_characters = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=','{','}','[',']','|',';',':','<','>','?','/','~','`','.',','] 
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    password_length = 25
    password = ''
    used_classes = []
    for i in range(password_length):
        character_class = random.choice(character_classes)

        if character_class not in used_classes:
                used_classes.append(character_class)

        if character_class == 'uppercase':
            password += random.choice(alphabet_lowercase).upper()
                     
        elif character_class == 'lowercase':
            password += random.choice(alphabet_lowercase)
            
        elif character_class == 'digits':
            password += random.choice(digits)

        elif character_class == 'special_characters':
            password += random.choice(special_characters)

    if len(used_classes) < 4:
        print("Not enough character classes used. Regenerating password...")
        return random_password_gen(password_length)
    else:
        return password

