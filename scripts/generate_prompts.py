import json
import yaml
import re
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

# Project structure paths
ROOT_DIR = Path(__file__).parent.parent
DIST_DIR = ROOT_DIR / "dist"
TEMPLATES_DIR = ROOT_DIR / "templates"
PROMPTS_DIR = ROOT_DIR / "prompts"
CONFIG_FILE = ROOT_DIR / "config/libraries.yml"

def main():
    """
    Generates final prompt Markdown files from Jinja2 templates and libdoc data.
    """
    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR), trim_blocks=True, lstrip_blocks=True)
    
    with open(CONFIG_FILE, 'r') as f:
        config = yaml.safe_load(f)

    for lib_config in config.get("libraries", []):
        lib_name_lower = lib_config["name"].lower()
        
        lib_data_file = DIST_DIR / f"{lib_name_lower}.json"
        if not lib_data_file.exists():
            print(f"Warning: Data file not found for {lib_config['name']}. Skipping.")
            continue

        with open(lib_data_file, 'r') as f:
            lib_data = json.load(f)

        for kw in lib_data["keywords"]:
            # Remove the verbose forum link, which is just noise for the LLM
            kw["doc"] = re.sub(r'\n\n\[https://forum\.robotframework\.org/t//\d+\|Comment >>\]', '', kw["doc"]).strip()

        print(f"Rendering prompt for '02-test-creation' using {lib_config['name']} library...")
        template = env.get_template("02-test-creation.md.j2")
        
        output = template.render(
            library_name=lib_config["name"],
            library=lib_data
        )

        output_dir = PROMPTS_DIR / "02-test-creation"
        output_dir.mkdir(exist_ok=True)
        output_path = output_dir / f"01-{lib_name_lower}-test.md"
        
        with open(output_path, 'w') as f:
            f.write(output)

        print(f"Successfully generated prompt at: {output_path}")
        
    print("\nPrompt generation complete.")

if __name__ == "__main__":
    main()
