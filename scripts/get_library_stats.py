import requests
import re
import time
import json
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor, as_completed

# --- Cache Configuration ---
CACHE_FILE = "pypi_stats_cache.json"
CACHE_DURATION_HOURS = 24

# --- API URLs ---
PYPI_SIMPLE_URL = "https://pypi.org/simple/"
PYPISTATS_API_URL = "https://pypistats.org/api/packages/{package_name}/recent"


def load_cache():
    """Loads the cache from a JSON file if it exists."""
    try:
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_cache(cache):
    """Saves the cache to a JSON file."""
    with open(CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=2)


def is_cache_valid(cache_entry):
    """Checks if a cache entry is still within the valid duration."""
    timestamp = datetime.fromisoformat(cache_entry["timestamp"])
    return datetime.now() - timestamp < timedelta(hours=CACHE_DURATION_HOURS)


def get_rf_package_names():
    """Fetches the list of all packages from PyPI's simple index."""
    print(f"Fetching package list from {PYPI_SIMPLE_URL}...")
    try:
        response = requests.get(PYPI_SIMPLE_URL, timeout=30)
        response.raise_for_status()
        package_names = re.findall(
            r">robotframework-([^<]+)<", response.text, re.IGNORECASE
        )
        full_names = sorted(
            list(set([f"robotframework-{name.lower()}" for name in package_names]))
        )
        print(f"Found {len(full_names)} unique packages matching 'robotframework-*'.")
        return full_names
    except requests.RequestException as e:
        print(f"Error: Could not fetch package list from PyPI. {e}")
        return []


def get_package_downloads(package_name):
    """Fetches download count for a single package."""
    try:
        url = PYPISTATS_API_URL.format(package_name=package_name.lower())
        response = requests.get(url, timeout=15)
        if response.status_code == 404:
            return (package_name, 0)
        response.raise_for_status()
        data = response.json()
        last_month_downloads = data.get("data", {}).get("last_month", 0)
        return (package_name, last_month_downloads)
    except requests.RequestException:
        return (package_name, -1)
    except Exception:
        return (package_name, -1)


def main():
    """Main function to orchestrate fetching, caching, and reporting."""
    cache = load_cache()
    all_package_names = get_rf_package_names()
    if not all_package_names:
        return

    final_stats = []
    packages_to_fetch = []

    # Partition packages: use cache if valid, otherwise mark for fetching
    for name in all_package_names:
        if name in cache and is_cache_valid(cache[name]):
            final_stats.append({"name": name, "downloads": cache[name]["downloads"]})
        else:
            packages_to_fetch.append(name)

    print(f"\n{len(final_stats)} packages loaded from cache.")
    print(f"{len(packages_to_fetch)} packages need to be fetched from API.")

    if packages_to_fetch:
        failed_packages = []
        with ThreadPoolExecutor(
            max_workers=5
        ) as executor:  # Reduced workers to be gentler on the API
            print(f"Fetching stats for {len(packages_to_fetch)} packages...")
            future_to_package = {
                executor.submit(get_package_downloads, name): name
                for name in packages_to_fetch
            }

            for i, future in enumerate(as_completed(future_to_package)):
                name = future_to_package[future]
                try:
                    _, downloads = future.result()
                    if downloads != -1:
                        final_stats.append({"name": name, "downloads": downloads})
                        # Update cache with new data
                        cache[name] = {
                            "downloads": downloads,
                            "timestamp": datetime.now().isoformat(),
                        }
                    else:
                        failed_packages.append(name)
                    print(f"\rProgress: {i + 1}/{len(packages_to_fetch)}", end="")
                except Exception as exc:
                    failed_packages.append(f"{name} (Exception: {exc})")

        print("\n")
        if failed_packages:
            print("--- Warnings ---")
            print(f"Could not retrieve stats for {len(failed_packages)} package(s):")
            for pkg in sorted(failed_packages):
                print(f" - {pkg}")

    # Save the updated cache to disk
    save_cache(cache)
    print("\nCache file updated.")

    print("\n--- Robot Framework Library Monthly Downloads ---")
    sorted_stats = sorted(final_stats, key=lambda x: x["downloads"], reverse=True)

    for i, stats in enumerate(sorted_stats):
        if i < 30:
            print(f"{i+1:<4} {stats['name']:<45} {stats['downloads']:>15,}")

    if len(sorted_stats) > 30:
        print("...")


if __name__ == "__main__":
    main()
