file_name = input(f"[>>>] Enter the file name: ");file_name = "".join([file_name + ".py" if not file_name.endswith(".py") else file_name])
with open(file_name, "r") as f:
    lines = f.read();code = str(lines.encode("utf8"))[:-1][2:]
    with open(file_name[:-3]+"_oneline.py", "w") as f:
        f.write(f"exec(\"\"\"{code}\"\"\")");print(f"[>>>] File saved as {file_name[:-3]+'_oneline.py'}")
