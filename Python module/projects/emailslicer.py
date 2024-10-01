#collect email from user.
#split the email using @, the  first part as username, the second part as domain.
#split the second name using .,

def get_email():
    print("Welcome Here!\n")
    print("")

    email_input = input("Enter your email address")
    (username, domain) = email_input.split("@")
    (domain,extension) = domain.split(".")

    print("Username: " ,username)
    print("Domain: " ,domain)
    print("Extension: " ,extension)
while True:
 get_email()