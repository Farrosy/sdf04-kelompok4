def validate_name(name):
    return bool(name and name.strip())
print(validate_name("Budi"))
print(validate_name(""))