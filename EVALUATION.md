# Prompt Evaluation Framework

## 1. Introduction

To ensure our prompts are effective, reliable, and produce high-quality results, we must test them rigorously. This document outlines the manual evaluation process that every contributor should follow when creating or modifying a prompt.

The goal is to provide a structured, repeatable method for verifying that prompt changes are beneficial and do not cause regressions. The process is designed to be manual for now, but its structure is intended to support future automation.

## 2. The Evaluation Process

Any Pull Request that modifies a prompt (`.md` file in `/prompts/` or a `.j2` template) **must** include an "Evaluation Results" section in its description, containing a completed checklist for each relevant test scenario.

The process is as follows:

1.  **Choose Your LLM Testbeds**: Perform each test scenario on at least **two** of the following Large Language Models to ensure cross-compatibility.
    *   Claude (e.g., Sonnet 3.5)
    *   OpenAI GPT (e.g., GPT-4o)
    *   Google Gemini (e.g., Gemini 1.5 Pro)

2.  **Select Test Scenarios**: Identify the relevant test scenarios from the list below that cover the changes you made.

3.  **Start a Fresh Conversation**: For each test run, you **must** start a new, clean conversation with the LLM. This prevents context from previous interactions from influencing the result.

4.  **Execute the Scenario**:
    *   Copy the entire content of the modified prompt file.
    *   Paste it into the fresh LLM chat.
    *   Role-play the "User Persona" defined in the scenario.
    *   Follow the conversation to its conclusion.

5.  **Document the Results**: Copy the evaluation checklist template below into your Pull Request description for each scenario you tested. Fill it out honestly, noting both successes and failures.

## 3. Standard Test Scenarios

### Scenario: Setup-01 (Happy Path Beginner)
-   **Prompt File**: `prompts/01-setup/01-environment-setup.md`
-   **User Persona**:
    1.  When asked for OS: "Windows"
    2.  When asked for goal: "I want to automate logging into a website."
    3.  When asked for background: "I have no coding experience at all."
-   **Success Criteria**:
    -   The LLM follows the multi-step conversation correctly.
    -   The LLM correctly recommends creating and activating a Python virtual environment (`venv`) before installing anything.
    -   The LLM provides **only** Windows-specific commands.
    -   The LLM correctly recommends installing `robotframework-browser` and running `rfbrowser init`.
    -   The LLM **does not** mention `robotframework-seleniumlibrary`.

### Scenario: Setup-02 (Ambiguous OS Input)
-   **Prompt File**: `prompts/01-setup/01-environment-setup.md`
-   **User Persona**:
    1.  When asked for OS: "I use Windows at work and a Mac at home."
-   **Success Criteria**:
    -   The LLM does not get confused or enter a loop.
    -   The LLM asks the user to clarify which operating system they want to set up *for this session*.
    -   Once an OS is chosen, the rest of the conversation proceeds correctly for that single OS.

### Scenario: TestCreation-01 (Simple Web Task)
-   **Prompt File**: `prompts/02-test-creation/01-browser-test.md`
-   **User Persona**: "I want to go to robotframework.org, click the 'Docs' link in the main navigation, and verify that the page URL contains the word 'docs'."
-   **Success Criteria**:
    -   The LLM generates a complete, syntactically correct `.robot` file.
    -   The generated code uses `Browser` library keywords.
    -   The selectors used are reasonable and likely to work (e.g., `text=Docs`).
    -   The generated code includes a `*** Settings ***` and `*** Test Cases ***` section.
    -   The response includes the "How it Works" and "Keyword Reference" sections.
    -   The LLM **does not** use or mention `robotframework-seleniumlibrary`.

## 4. Evaluation Checklist Template

Copy and paste this template into your Pull Request description for each scenario you test.

```
### Evaluation: [Scenario Name] on [LLM Name]

- [ ] **Persona Adopted**: The LLM maintained the persona of a friendly Automation Consultant.
- [ ] **Rules Followed**: All critical rules in the prompt were followed.
- [ ] **Logical Flow**: The conversation was logical and did not loop or ask redundant questions.
- [ ] **Output Correctness**: The final output (code, commands) was correct and followed best practices.
- [ ] **No Hallucinations**: The LLM did not invent keywords or provide irrelevant information.

**Result**: PASS / FAIL

**LLM Transcript**:
<details>
<summary>Click to expand</summary>

(Paste the full conversation here)

</details>
```

## 5. Future Automation

The structured nature of these scenarios (defined user inputs and success criteria) is intentional. In the future, this framework can be adapted for automated evaluation using LLM APIs. An automated test could:
-   Send the prompt and user inputs to an LLM API.
-   Programmatically check the LLM's response against the success criteria (e.g., assert that the response string contains `python -m venv` and does not contain `seleniumlibrary`).
-   Flag regressions automatically in CI/CD.
```