def three_args(*, var1=None, var2=None, var3=None):
    args_str = "Переданы аргументы:"
    if var1 is not None:
        args_str += f" var1 = {var1},"
    if var2 is not None:
        args_str += f" var2 = {var2},"
    if var3 is not None:
        args_str += f" var3 = {var3},"

    args_str = args_str.rstrip(',')

    print(args_str)


three_args(var1=2, var3=10)
three_args(var2=5)
three_args(var1=1, var2=3, var3=7)