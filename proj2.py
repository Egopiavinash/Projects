import random
import string
def g_password():
    length=int(input("enter the desired paasword length:").strip())
    include_uppercase=int(input("include uppercase leeter?(yes/no):")).strip().lower()
    include_special=int(input("include special characters?(yes/no):")).strip().lower()
    include_digits=int(input("include digits ?(yes/no):")).strip().lower()

    if length<4:
        print("password length must be at least 4 chars:")
        return
    
    lower=string.ascii_lowercase
    upper_case=string.ascii_uppercase if include_uppercase=="yes" else""
    special=string.punctuation if include_special=="yes" else""
    digits=string.digits if include_digits=="yes" else""
    all_characters=lower+upper_case+special+digits
    required_characters=[]
    if include_uppercase=="yes":
        required_characters.append(random.choice(upper_case))
        if include_special=="yes":
            required_characters.append(random.choice(special))
            if include_digits=="yes":
                required_characters.append(random.choice(digits))
                remain_length=length-len(required_characters)
                for _ in range(remain_length):
                    character=random.choice(all_characters)
                    password.append(character)
                    random.shuffle(password)
                    str_password="".join(password)
                    return str_password
                password=g_password()
                print(password)


        