import re

def valid_input(input, type):
    if type == "username":
        USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
        return USER_RE.match(input)
    elif type == "password":
        USER_RE = re.compile(r"^.{3,20}$")
        return USER_RE.match(input)
    elif type == "email":
        USER_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
        return USER_RE.match(input)

def error_gen(user_name, user_pass, user_veri, user_email):
    error_msg = ["","","","", True]
    if (valid_input(user_name, "username") == None):
        error_msg[0] = "That's not a valid username"

    if (valid_input(user_pass, "password") == None):
        error_msg[1] = "That wasn't a valid password"
    else:
        if user_pass != user_veri:
            error_msg[2] = "Your passwords didn't match"

    if (valid_input(user_email, "email") == None):
        error_msg[3] = "That's not a valid email"

    if (error_msg[0] == "" and error_msg[1] == "" and error_msg[2] == "" and error_msg[3] == ""):
        error_msg[4] = True
    else:
        error_msg[4] = False

    return error_msg

user_name = "terry"
user_pass = "123"
user_veri = "123"
user_email = "terry@hotmail.com"

error_msg = error_gen(user_name, user_pass, user_veri, user_email)
print(error_msg)