def input_options(text, limit):
    options = [str(i+1) for i in range(limit)]

    while True:
        output = input(text)

        if output in options:
            return output
