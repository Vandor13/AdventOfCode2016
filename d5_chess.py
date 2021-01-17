import hashlib

secret_key = "ojvtpuvg"
number = 0
password = [None] * 8

while True:
    string_value = secret_key + str(number)
    # byte_value = bytes(int(secret_key + str(number)), 16)
    m = hashlib.md5()
    # byte_value = string_value.encode()
    m.update(string_value.encode())
    hexdigest = m.hexdigest()
    # print(hexdigest)
    if hexdigest[:5] == "00000":
        print("Found char:", string_value)
        position = hexdigest[5]
        if "0" <= position <= "7" and password[int(position)] is None:
            password[int(position)] = hexdigest[6]
            print(password)
        if None not in password:
            print("Password:", "".join(password))
            exit()
    number += 1
