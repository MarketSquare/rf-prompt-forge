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
3.  **Create a Template**: Create a new Jinja2 template (e.g., `templates/04-api-test-creation.md.j2`) for the library's primary use case. You can often copy and adapt an existing template.
4.  **Update `scripts/generate_prompts.py`**: Modify the script to call your new template and generate the corresponding `.md` file in the `prompts/` directory.
5.  **Run the Generator**: Run `python scripts/generate_prompts.py` to create the final prompt file.
6.  **Create a Pull Request**: Submit your changes for review.

### Improving Existing Templates or Scripts

See a way to make an existing template (`.j2` file) or a Python script better?
1.  **Fork the Repository.**
2.  **Make Your Changes**: Modify the relevant files in `/templates/` or `/scripts/`.
3.  **Run the Generator**: Ensure your changes work by running `python scripts/generate_prompts.py`.
4.  **Commit Your Changes**: Commit the changes to the source files AND the newly generated prompt files in the `prompts/` directory.
5.  **Create a Pull Request.**

Thank you again for your contribution!