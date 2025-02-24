import os
import shutil
from web_generation import static_to_public, generate_page

def main():
    print("Deleting...")
    if os.path.exists("./public"):
        shutil.rmtree("./public")
    
    print("Copying...")
    static_to_public("./static", "./public")

    generate_page("./content/index.md", "./template.html", "./public/index.html")

    
    



main()