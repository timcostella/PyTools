import random, wget, magic, hashlib, os, pefile, datetime

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
    

# Function to download a specificied file from the internet
# Requires wget module, pip install wget / sudo apt install python3-wget

def GetURL(url, protocol, filename):
    address = protocol + "://" + url
    print(f"Downloading address: {address}")
    file = wget.download(address, filename)
    print(f"\n File downloaded as {file}")

def Get_FileHash(filepath):
    file=open(filepath,"rb").read()
    md5hash = hashlib.md5(file).hexdigest()
    sha256hash = hashlib.sha256(file).hexdigest()
    return [f"MD5 Hash: {md5hash}", f"SHA256 Hash: {sha256hash}"]

def Get_FileType(filepath):
    return magic.from_file(filepath)

def Get_StringsInFile(filepath):
    command = f"strings {filepath}"
    output = os.popen(command)
    return output.read()

def Get_DLLImports(filepath):
    pe = pefile.PE(filepath)
    if hasattr(pe, 'DIRECTORY_ENTRY_IMPORT'):
        for entry in pe.DIRECTORY_ENTRY_IMPORT:
            print(entry)
            for DLLimport in entry.imports:
                if DLLimport.name != None:
                    print (DLLimport.name)
                else:
                    print(str(DLLimport.ordinal))


def Set_LogFileDateFormat(log_file_name, log_file_ext):
    log_file_date_format = datetime.datetime.now().strftime("%a_%m_%d_%Y_%I_%M_%S_%p_%Z")
    return log_file_name + "_" + log_file_date_format + "." + log_file_ext
    


# Function requires https://pypi.org/project/python-magic/ 
# pip install python-magic / sudo apt-get install libmagic1, sudo apt install python3-magic

# Function requires https://github.com/erocarrera/pefile
# pip install pefile / sudo apt install python3-pefile

# Function requires os module
# Function requires hashlib module

def Do_StaticAnalysis(filepath):
    logfilepath = "/tmp/" + Set_LogFileDateFormat("Do_StaticAnalysis","txt")
    logfile = open(logfilepath, "a")

    try:
        seperator = "*********************************"
        
        print(seperator)
        logfile.write(seperator)
        logfile.write("\n")

        print(f"File Being Analyzed: {filepath}")
        logfile.write(f"File Being Analyzed: {filepath}")
        logfile.write("\n")
        
        print(seperator)
        logfile.write(seperator)
        logfile.write("\n")
        
        print(seperator)
        logfile.write(seperator)
        logfile.write("\n")

        print("File Hash")
        logfile.write("File Hash")

        print(seperator)
        logfile.write(seperator)
        logfile.write("\n")

        hash_values = Get_FileHash(filepath)
        for hash_val in hash_values:
            print(hash_val)
            logfile.write(hash_val)
            logfile.write("\n")

        
        print(seperator)
        print("Magic Analysis")
        logfile.write(seperator)
        logfile.write("\n")

        print(seperator)
        logfile.write(seperator)
        logfile.write("\n")

        results = Get_FileType(filepath)
        print(results)
        logfile.write(results)
        logfile.write("\n")


        print(seperator)
        logfile.write(seperator)
        logfile.write("\n")

        print("Strings")
        logfile.write("Strings")

        print(seperator)
        logfile.write(seperator)
        logfile.write("\n")

        results = Get_StringsInFile(filepath)
        print(results)
        logfile.write(results)
        logfile.write("\n")


        print(seperator)
        logfile.write(seperator)
        logfile.write("\n")

        print("DLL Imports")
        logfile.write("DLL Imports")

        print(seperator)
        logfile.write(seperator)
        logfile.write("\n")

        Get_DLLImports(filepath)

       

    except FileNotFoundError:
        print(f"File {filepath} not found")



