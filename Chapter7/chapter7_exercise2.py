def eval_loop():
    while True:
        inp=input("Enter any express or type done to exit")
        if inp=="done":
            break
        else:
            print(eval(inp))
eval_loop()