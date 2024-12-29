from generate_video import start_generate_video
from playwright.sync_api import Page, expect, sync_playwright
import json

def post_tiktok(last_win_message: str):
    video_generated = start_generate_video(last_win_message)

    if not video_generated:
        return

    with sync_playwright() as p:

        with open('cookies.json') as file:
            cookies = json.load(file)

        browser = p.firefox.launch(headless=False)
        context = browser.new_context(
            accept_downloads=True)
        context.add_cookies(cookies)

        page = context.new_page()
        page.goto("https://tiktok.com/")

        page.locator('span', has_text='Upload ' ).click()

        page.wait_for_selector('button[aria-label="Select video"]')
        page.set_input_files('input', './output/video.mp4')

        is_video_uploaded = page.locator('span', has_text='Uploaded')
        is_video_uploaded.wait_for()

        page.locator('div[contenteditable="true"]').clear()
        page.locator('div[contenteditable="true"]').fill(last_win_message + '   #Losc #Lille #Lens')

        page.locator('button[data-e2e="post_video_button"]').click()

        page.wait_for_url("https://www.tiktok.com/tiktokstudio/content", timeout=10000000)
        browser.close()