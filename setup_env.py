import subprocess
import sys
import os

def run_command(command):
    subprocess.run(command, shell=True, check=True)

def main():
    # Update pip
    run_command("python -m pip install --upgrade pip")

    # Create a virtual environment
    venv_dir = "venv"
    run_command(f"python -m venv {venv_dir}")

    # Determine activation command based on OS
    if sys.platform == "win32":
        activate_cmd = os.path.join(venv_dir, "Scripts", "activate")
    else:
        activate_cmd = os.path.join(venv_dir, "bin", "activate")

    # Provide user with activation instructions
    print(f"Virtual environment created. To activate, run:\n{activate_cmd}")

if __name__ == "__main__":
    main()

# Locate the search bar, clear any previous text, and enter the company name
        search_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "search-global-typeahead__input"))
        )
        search_input.clear()  # Clear any previous text
        print(company_name)
        search_input.send_keys(company_name)
        search_input.send_keys(Keys.RETURN)

        # Use JavaScript to locate the buttons and print their text content
        # Find all buttons within the specified <ul> element
        # Find the "Companies" button element by its text content within the <ul> element
        companies_button = driver.find_element(By.XPATH,
                                               "//ul[contains(@class, 'search-reusables__filter-list')]//button[text()='Companies']")

        # Click on the "Companies" button
        companies_button.click()

        exit(1)

        time.sleep(5)

        element = driver.find_element_by_class_name("entity-result")

        # Get the first link within the element
        link = element.find_element_by_tag_name("a")

        # Get the href attribute of the link
        href = link.get_attribute("href")
        # Print or use the 'href' variable as needed
        print(href)
        # Navigate to the link
        driver.get(href)
        time.sleep(5)

        # Extract the specified element from the company's LinkedIn page
        org_top_card_summary = driver.find_element_by_css_selector(".org-top-card-summary-info-list")
        info_items = org_top_card_summary.find_elements_by_css_selector(".org-top-card-summary-info-list__info-item")

        # Extract individual pieces of information
        outsourcing_consulting = info_items[0].text.strip()
        location = info_items[1].text.strip()
        followers = info_items[2].text.strip()
        employees = info_items[3].text.strip()