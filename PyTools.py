import random

# Function to generate a random password with at least one character from each class with the number of digits specified

def random_password_gen( password_length=25):
    #define the 4 character classes - uppercase, lowercase, digits, special characters in lists
    character_classes = ['uppercase', 'lowercase', 'digits', 'special_characters']
    alphabet_lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    special_characters = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=','{','}','[',']','|',';',':','<','>','?','/','~','`','.',','] 
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    #create the password string
    password = ''

    #track used character classes in a list
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

# Function to check if any string from a list is found in a file (case insensitive)

def is_string_found_in_file(file_path, search_string_list=[]):
    
    if type(search_string_list) is str: 
        search_string_list = [search_string_list]

    try:
        with open(file_path, 'r') as file:
            content = file.read()
            content = content.lower()
            print(f"Searching for strings: {search_string_list} in file: {file_path}")
            print(f"File length: {len(content)} characters")
            for search_string in search_string_list:
                search_string = search_string.lower()
                if search_string in content:
                    print(f"Found string: {search_string}")
                    return True
            return False
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False 

