# Contributing to RF-Prompt-Forge

First off, thank you for considering contributing! This project thrives on community involvement, and every contribution helps make Robot Framework more accessible for everyone.

Our project is a **prompt generator**, not just a collection of static files. Contributions typically involve improving the generation process or the templates themselves.

## How Can I Contribute?

### Suggesting an Improvement or New Prompt

Have an idea for a new prompt workflow (e.g., "A prompt for creating custom keywords") or a way to make an existing prompt better?
1.  **Open an Issue:** Go to the "Issues" tab and describe your suggestion in detail. This is the best way to start a discussion.

### Adding a New Library

Want to add prompt support for a new Robot Framework library?
1.  **Fork the Repository.**
2.  **Update `config/libraries.yml`**: Add the new library's name and PyPI package name to the list.
3.  **Create a Template (if needed)**: If the library introduces a new testing domain (e.g., Desktop), create a new Jinja2 template (e.g., `templates/06-desktop-test.md.j2`). For common types like web or API, you can often reuse an existing template.
4.  **Run the Generators**:
    *   First, run `python scripts/generate_libdoc.py` to fetch the new library's keyword data.
    *   Then, run `python scripts/generate_prompts.py` to create the final prompt file based on your new config entry.
5.  **Create a Pull Request**: Submit your changes for review.

### Improving Existing Templates or Scripts

See a way to make an existing template (`.j2` file) or a Python script better?
1.  **Fork the Repository.**
2.  **Make Your Changes**: Modify the relevant files in `/templates/` or `/scripts/`.
3.  **Run the Generator**: Ensure your changes work by running `python scripts/generate_prompts.py`.
4.  **Commit Your Changes**: Commit the changes to the source files AND the newly generated prompt files in the `prompts/` directory.
5.  **Create a Pull Request.**

Thank you again for your contribution!