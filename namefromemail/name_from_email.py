def name_from_email(email_adress):
    snail_mail = email_adress.split("@")
    splitted_names = snail_mail[0]
    full_name = splitted_names.split(".")
    last_name = full_name[1].title()
    first_name = full_name[0].title()
    print(last_name, first_name)

print(name_from_email("elek.viz@exam.com"))
