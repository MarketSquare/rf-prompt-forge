# Project Roadmap for RF-Prompt-Forge

This document outlines the strategic vision, current status, and future goals for the Robot Framework Prompt Forge.

## Project Vision

Our vision is to create a living, self-updating repository of expert-crafted LLM prompts that cover the entire lifecycle of Robot Framework development. By using a dynamic generation system powered by official library documentation, we ensure that our prompts are always modern, accurate, and aligned with best practices, making Robot Framework more accessible to everyone.

## Current Status (November 2025)

The project has a robust, data-driven prompt generation engine and has expanded its library coverage based on community feedback and usage statistics.

-   **[✓] Dynamic Prompt Generation**: We have a Python-based system using Jinja2 templates to build prompts.
-   **[✓] Automated Data Extraction**: The system uses Robot Framework's `libdoc` tool to extract keyword information directly from installed libraries, ensuring data is always accurate.
-   **[✓] Expanded Library Coverage**: We have prompts for key testing domains:
    -   Web UI: `Browser` & `SeleniumLibrary`
    -   API: `RequestsLibrary`
    -   Mobile: `AppiumLibrary`
    -   SSH: `SSHLibrary`
-   **[✓] Foundational Prompts**: We have highly-optimized, interactive prompts for **New User Setup** and **Test Case Creation**. The `BuiltIn` library keywords are now included in all relevant prompts.
-   **[✓] Foundational Scripts**: The core scripts (`get_library_stats.py`, `generate_libdoc.py`, `generate_prompts.py`) are in place.

## Next Steps: Immediate Goals

These are the items we are actively working on or planning to start soon.

-   **[ ] Automate with GitHub Actions**: Create a scheduled GitHub workflow that automatically runs the generation scripts and creates a Pull Request if the prompts have changed due to a library update. This will keep our prompts perpetually up-to-date.
-   **[ ] Enhance Tooling Prompts**: Create prompts for ecosystem tools like `Pabot` (for parallel execution) and `Robocop` (for linting and quality checks).
-   **[ ] Further Library Expansion**: Add support for other popular libraries based on our PyPI stats analysis, such as `robotframework-databaselibrary`.

## Future Ideas

These are longer-term goals to consider once the immediate priorities are complete.

-   **[ ] Advanced Architecture Prompts**: Develop prompts that teach best practices for scalable test automation, such as the Page Object Model, creating reusable resource files, and data-driven testing strategies.
-   **[ ] CI/CD Pipeline Prompts**: Create prompts for generating basic CI pipelines (e.g., GitHub Actions) to run Robot Framework tests.
-   **[ ] Custom Keyword Prompts**: Develop a prompt that helps users refactor repetitive steps into their own reusable keywords.
-   **[ ] Desktop Testing Prompts**: Add support for libraries like `robotframework-flaui` (Windows) or `robotframework-zoomba` (cross-platform).
-   **[ ] `robotframework.org` Integration**: Explore the feasibility of hosting the "copy prompt" functionality directly on the official Robot Framework website.
-   **[ ] Tool-Specific Integrations**: Investigate creating specialized prompt files for specific tools, such as a `GEMINI.md` for the Gemini CLI.