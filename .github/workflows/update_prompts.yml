name: Update Prompts

on:
  schedule:
    # Run at 08:00 UTC every day
    - cron: '0 8 * * *'
  workflow_dispatch:

jobs:
  update-prompts:
    runs-on: ubuntu-latest
    permissions:
      contents: write
      pull-requests: write

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '24'

      - name: Install Script Dependencies
        # Installs the tools needed to RUN the generators.
        # (The generators themselves create a venv for the target libraries)
        run: |
          python -m pip install --upgrade pip
          pip install requests pyyaml jinja2 robotframework

      - name: Generate Libdoc JSON
        # This script:
        # 1. Creates a temp venv
        # 2. Installs latest versions of libraries from config/libraries.yml
        # 3. Runs 'rfbrowser init'
        # 4. Generates fresh JSON spec files
        run: python scripts/generate_libdoc.py

      - name: Generate Prompts
        # Consumes the JSON and Templates to write Markdown
        run: python scripts/generate_prompts.py

      - name: Create Pull Request
        uses: peter-evans/create-pull-request@v7
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: "chore: update prompts with latest library versions"
          title: "chore: Update Prompts"
          body: |
            This PR was automatically created by the `update_prompts.yml` workflow.
            
            It contains updates to the prompt files based on the latest releases of the Robot Framework libraries defined in `config/libraries.yml`.
          branch: auto/update-prompts
          delete-branch: true
          base: main