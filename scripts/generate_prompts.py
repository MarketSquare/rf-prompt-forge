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

def load_and_clean_libdoc(lib_name: str) -> dict:
    """Loads a libdoc JSON file and cleans its content for the LLM."""
    lib_data_file = DIST_DIR / f"{lib_name.lower()}.json"
    if not lib_data_file.exists():
        print(f"ERROR: Data file not found for {lib_name}. Run generate_libdoc.py first.")
        return None

    with open(lib_data_file, 'r') as f:
        lib_data = json.load(f)

    # Clean up keyword documentation for better LLM consumption
    for kw in lib_data.get("keywords", []):
        kw["doc"] = re.sub(r'\n\n\[https://forum\.robotframework\.org/t//\d+\|Comment >>\]', '', kw["doc"]).strip()
    
    return lib_data

def main():
    """
    Generates final prompt Markdown files from Jinja2 templates and libdoc data.
    """
    env = Environment(loader=FileSystemLoader(TEMPLATES_DIR), trim_blocks=True, lstrip_blocks=True)
    
    with open(CONFIG_FILE, 'r') as f:
        config = yaml.safe_load(f)

    libraries = config.get("libraries", [])
    
    # --- 1. Find and load the universal 'BuiltIn' library data ---
    builtin_library_data = None
    for lib_config in libraries:
        if lib_config.get("include_in_all"):
            print(f"Found universal library: {lib_config['name']}. Loading its data...")
            builtin_library_data = load_and_clean_libdoc(lib_config['name'])
            if not builtin_library_data:
                exit(1) # Exit if BuiltIn data is missing
            break
    
    if not builtin_library_data:
        print("Warning: No library marked with 'include_in_all: true' found in config.")

    # --- 2. Loop through libraries again to generate specific prompts ---
    for lib_config in libraries:
        # Skip disabled libraries and the universal library itself
        if not lib_config.get("enabled") or lib_config.get("include_in_all"):
            continue

        print(f"\n--- Processing: {lib_config['name']} ---")
        
        # Load the specific library's data
        library_data = load_and_clean_libdoc(lib_config['name'])
        if not library_data:
            continue

        # Get rendering details from config
        template_name = lib_config.get("template")
        output_file = lib_config.get("output_file")
        category = lib_config.get("category")

        if not all([template_name, output_file, category]):
            print(f"Warning: Skipping {lib_config['name']} due to missing config (template, output_file, or category).")
            continue
        
        template = env.get_template(template_name)
        
        # Render the template with both the specific library and BuiltIn data
        output = template.render(
            library_name=lib_config["name"],
            library=library_data,
            builtin_library=builtin_library_data
        )

        # Create the output directory and save the file
        output_dir = PROMPTS_DIR / category
        output_dir.mkdir(parents=True, exist_ok=True)
        # Add a .gitkeep file to new directories
        if not any(output_dir.iterdir()):
             (output_dir / ".gitkeep").touch()

        output_path = output_dir / output_file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(output)

        print(f"Successfully generated prompt at: {output_path}")
        
    print("\nPrompt generation complete.")

if __name__ == "__main__":
    main()