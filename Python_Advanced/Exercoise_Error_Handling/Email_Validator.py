class NameTooShortError(Exception):
    pass

class MustContainAtSymbolError(Exception):
    pass

class InvalidDomainError(Exception):
    pass

valid_domains = (".com", ".org", ".net", ".bg")


def is_valid_domain(email):
    domain = '.' + email.split(".")[-1]
    if domain not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

def is_valid_email_name(email):
    if '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")

    name = email.split("@")[0]
    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")


while (email := input()) != 'End':
    try:
        is_valid_email_name(email)
        is_valid_domain(email)
        print('Email is valid')
    except Exception as e:
        print(e)
