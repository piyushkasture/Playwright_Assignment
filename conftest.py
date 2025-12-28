from pathlib import Path
import pytest
from slugify import slugify
import allure


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    screen_file = ''
    report = outcome.get_result()
    extra = getattr(report, "extra", [])

    if report.when == "call":
        # Check if page fixture is available
        if hasattr(item, "funcargs") and "page" in item.funcargs:
            try:
                page = item.funcargs["page"]
                screenshot_dir = Path("reports/screenshots")
                screenshot_dir.mkdir(exist_ok=True)
                screen_file = str(screenshot_dir / f"{slugify(item.nodeid)}.png")
                page.screenshot(path=screen_file)

                # Determine the status for naming the attachment
                if report.passed:
                    status = "Pass"
                elif report.failed:
                    status = "Failure"
                elif report.skipped:
                    status = "Skipped"
                else:
                    status = "Screenshot"

                # Add the screenshots to the html report for all outcomes
                extra.append(pytest_html.extras.png(screen_file))

                # Attach to Allure report for all outcomes
                allure.attach.file(
                    screen_file,
                    name=f"{status} Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception as e:
                print(f"Error capturing screenshot: {e}")

        report.extra = extra

