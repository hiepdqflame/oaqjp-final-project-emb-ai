"""Capture actual browser results; successful deployment requires live Watson."""

import argparse
from pathlib import Path

from playwright.sync_api import expect, sync_playwright


def main():
    """Check desktop/mobile input handling and capture submission screenshots."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", default="http://127.0.0.1:5000")
    parser.add_argument("--channel", default=None,
                        help="Use an installed browser, for example chrome")
    parser.add_argument("--live", action="store_true",
                        help="Also capture successful real Watson analysis")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    destination = root / "submission"
    destination.mkdir(exist_ok=True)
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(channel=args.channel)
        page = browser.new_page(viewport={"width": 1280, "height": 800})
        errors = []
        page.on("pageerror", lambda error: errors.append(str(error)))
        page.goto(args.url)
        page.get_by_role("button", name="Run Sentiment Analysis").click()
        expect(page.get_by_role("status")).to_have_text(
            "Invalid text! Please try again!")
        page.screenshot(path=str(destination / "7c_error_handling_interface.png"),
                        full_page=True)
        print("PASS: blank-input browser screenshot captured")

        page.set_viewport_size({"width": 390, "height": 844})
        expect(page.get_by_label("Please enter the text to be analyzed")).to_be_visible()
        page.get_by_label("Please enter the text to be analyzed").fill("   ")
        page.get_by_role("button", name="Run Sentiment Analysis").click()
        expect(page.get_by_role("status")).to_have_text(
            "Invalid text! Please try again!")
        assert page.evaluate(
            "document.documentElement.scrollWidth <= window.innerWidth"
        ), "Mobile page overflows horizontally"
        mobile_path = root / "tmp" / "mobile-error.png"
        mobile_path.parent.mkdir(exist_ok=True)
        page.screenshot(path=str(mobile_path), full_page=True)
        print("PASS: mobile blank-input flow, no horizontal overflow")

        if args.live:
            target = destination / "6b_deployment_test.png"
            target.unlink(missing_ok=True)
            page.set_viewport_size({"width": 1280, "height": 800})
            page.get_by_label("Please enter the text to be analyzed").fill(
                "I think I am having fun")
            page.get_by_role("button", name="Run Sentiment Analysis").click()
            expect(page.get_by_role("status")).to_contain_text(
                "The dominant emotion is joy.", timeout=90000)
            page.screenshot(path=str(target), full_page=True)
            print("PASS: live Watson deployment screenshot captured")

        assert not errors, errors
        browser.close()


if __name__ == "__main__":
    main()
