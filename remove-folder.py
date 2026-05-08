import shutil

print("Paste ur path folder for delete")
remove = input("paste path: ").strip().strip('"')

delete = input("are u sure? (y/n): ").lower()

if delete == 'y' :
    print("clear remove..>")
    shutil.rmtree(remove)
elif delete == 'n' :
    print("cansle remove")
else :
    print("what ar u doing? input y or n dude")