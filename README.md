# Robot Framework Prompt Forge (RF-Prompt-Forge)

![License](https://img.shields.io/badge/license-Apache_2.0-blue.svg)

An open-source collection of expert-crafted prompt templates to make Large Language Models (LLMs) super performant with Robot Framework.

---

### The Problem: Generic LLMs are Not Robot Framework Experts

When a newcomer asks a generic LLM for help with Robot Framework, they get an answer that is often:
-   Outdated (e.g., recommending `SeleniumLibrary` over the modern `Browser` library).
-   Missing best practices (e.g., forgetting to recommend `venv` virtual environments).
-   Incomplete (e.g., not mentioning the essential VS Code extension).

This leads to a frustrating experience and a poor start for new users.

### The Solution: Expert Knowledge as a Template

**RF-Prompt-Forge** provides structured, copy-paste-ready prompt templates that embed expert knowledge and best practices. These templates guide any LLM to produce a perfect, high-quality, and modern response every time.

Think of it as turning your LLM from a generic assistant into a specialized Robot Framework mentor.

### How to Use

1.  Navigate to the `prompts` directory.
2.  Find the template that matches your task (e.g., `01-setup/01-environment-setup.md`).
3.  Copy the entire content of the template file.
4.  Paste it into your favorite LLM (ChatGPT, Gemini, Claude, etc.).
5.  Modify any placeholders like `[USER INPUTS OS HERE]` to match your needs.
6.  Get a perfect, expert-guided result!

### Project Roadmap

This project aims to cover the entire Robot Framework lifecycle with templates for:

-   **[X] 01-Setup:** Environment and project initialization.
-   **[ ] 02-Test-Creation:** Generating boilerplate for Web (Browser), API, and Mobile tests.
-   **[ ] 03-Keyword-Creation:** Refactoring test steps into reusable custom keywords.
-   **[ ] 04-Library-Usage:** Getting specific, correct examples for keywords from popular libraries.
-   **[ ] 05-CI-CD:** Generating basic CI pipelines (e.g., GitHub Actions) to run your tests.

### How to Contribute

We welcome contributions! If you have an idea for a new prompt or an improvement to an existing one, please see our [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines.

### License

This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for details.
