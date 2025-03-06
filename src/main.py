import os
import shutil
from web_generation import static_to_public, generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
tempalte_path = "./template.html"

def main():
    print("Deleting...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    
    print("Copying...")
    static_to_public(dir_path_static, dir_path_public)

    generate_pages_recursive(dir_path_content, tempalte_path, dir_path_public)

    
    



main()