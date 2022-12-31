def print_hi(name):
    # assert name == "bad_name", f"name should be More!!"  # PASS
    # x = 10
    # print(eval("x * 10"))  # PASS
    username = "user"
    password = "admin123456"
    url = "https://example.com/accounts/details?id=123&access_key=abcdefg&access_secret=opensecret"
    print(username, password)
    print(url)
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi('More!!')
