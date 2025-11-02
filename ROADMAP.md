# Project Roadmap for RF-Prompt-Forge

This document outlines the strategic vision, current status, and future goals for the Robot Framework Prompt Forge.

## Project Vision

Our vision is to create a living, self-updating repository of expert-crafted LLM prompts that cover the entire lifecycle of Robot Framework development. By using a dynamic generation system powered by official library documentation, we ensure that our prompts are always modern, accurate, and aligned with best practices, making Robot Framework more accessible to everyone.

## Current Status (November 2025)

The project has successfully transitioned from a collection of static Markdown files to a dynamic prompt generation engine.

-   **[✓] Dynamic Prompt Generation**: We have a Python-based system using Jinja2 templates to build prompts.
-   **[✓] Automated Data Extraction**: The system uses Robot Framework's `libdoc` tool to extract keyword information directly from installed libraries, ensuring data is always accurate.
-   **[✓] Initial Prompt Implemented**: We have a complete, highly-optimized prompt for **Test Case Creation** using the `robotframework-browser` library.
-   **[✓] Foundational Scripts**: The core scripts (`get_library_stats.py`, `generate_libdoc.py`, `generate_prompts.py`) are in place.

## Next Steps: Immediate Goals

These are the items we are actively working on or planning to start soon.

-   **[ ] Automate with GitHub Actions**: Create a scheduled GitHub workflow that automatically runs the generation scripts and creates a Pull Request if the prompts have changed due to a library update.
-   **[ ] Expand Library Coverage**: Add support for other popular libraries based on our PyPI stats analysis, starting with:
    -   `robotframework-requests` (API Testing)
    -   `robotframework-pabot` (Tooling/Execution)
-   **[ ] Refine "New User Setup" Prompt**: Convert the static `01-environment-setup.md` prompt into a dynamic template that can be updated with the latest recommendations.

## Future Ideas

These are longer-term goals to consider once the immediate priorities are complete.

-   **[ ] CI/CD Pipeline Prompts**: Create prompts for generating basic CI pipelines (e.g., GitHub Actions) to run Robot Framework tests.
-   **[ ] Custom Keyword Prompts**: Develop a prompt that helps users refactor repetitive steps into their own reusable keywords.
-   **[ ] Mobile & Desktop Prompts**: Add support for libraries like `robotframework-appiumlibrary` and `robotframework-flaui`.
-   **[ ] `robotframework.org` Integration**: Explore the feasibility of hosting the "copy prompt" functionality directly on the official Robot Framework website.