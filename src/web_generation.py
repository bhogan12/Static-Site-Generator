import os
import shutil
from pathlib import Path
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
    

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")

    with open(from_path) as file:
        from_md = file.read()

    with open(template_path) as file:
        template = file.read()

    md_html = markdown_to_html_node(from_md).to_html()
    title = extract_title(from_md)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", md_html)
    template = template.replace('href="/', 'href="' + basepath)
    template = template.replace('src="/', 'src="' + basepath)

    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, 'w') as file:
        file.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path, basepath)
        else:
            generate_pages_recursive(from_path, template_path, dest_path, basepath)