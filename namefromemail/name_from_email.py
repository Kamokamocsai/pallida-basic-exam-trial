def name_from_email(email_adress):
    snail_mail = email_adress.split("@")
    splitted_names = snail_mail[0]
    full_name = splitted_names.split(".")
    last_name = full_name[1]
    first_name = full_name[0]
    print(last_name.title(), first_name.title())

print(name_from_email("elek.viz@exam.com"))
