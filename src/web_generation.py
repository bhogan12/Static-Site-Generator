import os
import shutil
from block_markdown import markdown_to_html_node, extract_title

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
    

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")

    with open(from_path) as file:
        from_md = file.read()

    with open(template_path) as file:
        template = file.read()

    md_html = markdown_to_html_node(from_md).to_html()
    title = extract_title(from_md)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", md_html)

    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(dest_path, exist_ok=True)

    with open(dest_path, 'w') as file:
        file.write(template)