import yaml
import subprocess
import sys
import venv
import shutil
from pathlib import Path

# Project structure paths
ROOT_DIR = Path(__file__).parent.parent
CONFIG_FILE = ROOT_DIR / "config/libraries.yml"
DIST_DIR = ROOT_DIR / "dist"
VENV_DIR = ROOT_DIR / ".venv-libdoc"

def run_command(command, cwd=None):
    """Executes a command and raises an error if it fails."""
    print(f"Executing: {' '.join(command)}")
    result = subprocess.run(command, capture_output=True, text=True, cwd=cwd, check=False)
    if result.returncode != 0:
        print(f"Error executing command: {' '.join(command)}")
        print(f"STDOUT: {result.stdout}")
        print(f"STDERR: {result.stderr}")
        raise subprocess.CalledError(result.returncode, command, result.stdout, result.stderr)
    return result

def main():
    """
    Generates libdoc JSON files for libraries defined in config/libraries.yml.
    """
    if not CONFIG_FILE.exists():
        print(f"Error: Configuration file not found at {CONFIG_FILE}")
        sys.exit(1)

    with open(CONFIG_FILE, 'r') as f:
        config = yaml.safe_load(f)

    libraries = config.get("libraries", [])
    if not libraries:
        print("No libraries found in the configuration file. Exiting.")
        return

    DIST_DIR.mkdir(exist_ok=True)

    print(f"\n--- Creating temporary venv at {VENV_DIR} ---")
    if VENV_DIR.exists():
        shutil.rmtree(VENV_DIR)
    venv.create(VENV_DIR, with_pip=True)

    python_executable = VENV_DIR / "bin" / "python"
    if sys.platform == "win32":
        python_executable = VENV_DIR / "Scripts" / "python.exe"

    try:
        # Collect packages that need installation
        pypi_packages_to_install = [lib["package"] for lib in libraries if lib.get("type") == "pypi" and lib.get("enabled", False)]

        if pypi_packages_to_install:
            print("\n--- Installing dependencies into venv ---")
            base_packages = ["robotframework", "PyYAML"]
            run_command([str(python_executable), "-m", "pip", "install"] + base_packages + pypi_packages_to_install)
        else:
            print("\n--- No PyPI dependencies to install in venv (only BuiltIn or disabled libraries) ---")

        if "robotframework-browser" in pypi_packages_to_install:
            print("\n--- Initializing Browser library (rfbrowser init) ---")
            run_command([str(python_executable), "-m", "Browser.entry", "init"])

        print("\n--- Generating Libdoc JSON for each library ---")
        for lib in libraries:
            if lib.get("enabled", False): # Only process enabled libraries
                lib_name = lib["name"]
                output_file = DIST_DIR / f"{lib_name.lower()}.json"
                
                print(f"Processing '{lib_name}'...")
                command = [
                    str(python_executable),
                    "-m",
                    "robot.libdoc",
                    "--format", "JSON",
                    # CRITICAL: Use RAW specdoc format to avoid unwanted HTML in docs
                    "--specdocformat", "RAW",
                    lib_name,
                    str(output_file)
                ]
                run_command(command)
                print(f"Successfully generated libdoc at {output_file}")
            else:
                print(f"Skipping disabled library: {lib['name']}")

    finally:
        print("\n--- Cleaning up temporary venv ---")
        if VENV_DIR.exists():
            shutil.rmtree(VENV_DIR)

    print("\nLibdoc JSON generation complete.")

if __name__ == "__main__":
    main()