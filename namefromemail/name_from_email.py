def name_from_email(email_adress):
    snail_mail = email_adress.split("@")
    splitted_names = snail_mail[0]
    full_name = splitted_names.split(".")
    print(full_name[1], full_name[0])

print(name_from_email("elek.viz@exam.com"))
