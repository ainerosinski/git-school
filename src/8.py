def generate_random_code(length):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    code = ""
    for i in range(length):
        index = random.randint(0, len(chars) - 1)
        code += chars[index]
    return code
