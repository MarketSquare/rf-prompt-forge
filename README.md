# Robot Framework Prompt Forge (RF-Prompt-Forge)

![License](https://img.shields.io/badge/license-Apache_2.0-blue.svg)

A dynamic generator for creating expert-crafted, up-to-date prompt templates to make Large Language Models (LLMs) super performant with Robot Framework.

---

### The Problem: Generic LLMs are Not Robot Framework Experts

When a newcomer asks a generic LLM for help, the answer is often outdated, incomplete, or missing best practices. This leads to a frustrating start for new users.

### The Solution: A Self-Updating Prompt Generation Engine

**RF-Prompt-Forge** is not a system that **generates** and maintains those expert prompts. It uses a Python-based toolkit to:
1.  Programmatically install popular Robot Framework libraries like `robotframework-browser`.
2.  Extract official keyword documentation directly from the source using `libdoc`.
3.  Inject this up-to-date information into expert-crafted Jinja2 templates.
4.  Produce highly optimized, copy-paste-ready prompt files.

This ensures our prompts always reflect the latest library versions and modern best practices, turning any LLM into a specialized Robot Framework mentor.

### How to Use

#### For Prompt Users

1.  Navigate to the `prompts` directory.
2.  Find the template that matches your task (e.g., `02-test-creation/01-browser-test.md`).
3.  Copy the entire content of the file and paste it into your favorite LLM.
4.  Follow the instructions in the prompt to get an expert-guided result!

#### For Developers

To regenerate the prompts (e.g., after updating a library version):
1.  Install the required Python packages: `pip install requests pyyaml jinja2`
2.  Run the generation script: `python scripts/generate_prompts.py`

### Project Roadmap

We have a detailed plan for expanding our library coverage and adding new prompt categories. For a full overview of our current status, next steps, and future goals, please see our **[Project Roadmap](ROADMAP.md)**.

### How to Contribute

We welcome contributions! If you have an idea for a new prompt template or an improvement to the generation system, please see our [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines.

### License

This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for details.
