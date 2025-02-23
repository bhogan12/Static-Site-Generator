import os
import shutil

def static_to_public(source_dir, target_dir):
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    
    for file in os.listdir(source_dir):
        src = os.path.join(source_dir, file)
        tgt = os.path.join(target_dir, file)

        if os.path.isfile(src):
            shutil.copy(src, tgt)
        else:
            static_to_public(src, tgt)
    

def main():
    print("Deleting...")
    if os.path.exists("./public"):
        shutil.rmtree("./public")
    
    print("Copying...")
    static_to_public("./static", "./public")


main()