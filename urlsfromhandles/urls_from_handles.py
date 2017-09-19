names = ["teststudent", "ghhandle2"]

def urls_from_handles(names):
    output = []
    full_url1 = "https://github.com/greenfox-academy/" + names[0]
    full_url2 = "https://github.com/greenfox-academy/" + names[1]
    output.append(full_url1)
    output.append(full_url2)
    print(output)

print(urls_from_handles(names))