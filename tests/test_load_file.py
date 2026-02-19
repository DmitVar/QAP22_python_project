import os

from playwright.sync_api import Page, expect


def test_download_file(playwright_page: Page):
    url = "https://letcode.in/file"
    playwright_page.goto(url)
    download_text_file_button = playwright_page.locator("#txt")
    with playwright_page.expect_download() as download:
        download_text_file_button.click()
    file = download.value
    file.save_as("/home/d-varchak/qap22_python_project/data/" + file.suggested_filename)


def test_load_file(playwright_page: Page):
    url = "https://letcode.in/file"
    playwright_page.goto(url)
    file_input = playwright_page.locator("input[type='file']")
    current_dir = os.path.dirname(os.path.realpath(__file__))
    main_dir_path = current_dir.replace("/tests", "")
    file_path = os.path.join(main_dir_path, "data", "sample.txt")
    file_input.set_input_files(file_path)
    selected_file_message = playwright_page.locator("//p[normalize-space() = 'Selected File: sample.txt']")
    expect(selected_file_message).to_be_visible()
