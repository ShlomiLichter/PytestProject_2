import os
import pytest
from datetime import datetime

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        # Get the page fixture if available
        page = item.funcargs.get('page', None)
        if page:
            screenshots_dir = os.path.join(os.getcwd(), 'screenshots')
            os.makedirs(screenshots_dir, exist_ok=True)
            test_name = item.name.replace('/', '_').replace('\\', '_')
            timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            filename = f"{test_name}_{timestamp}.png"
            filepath = os.path.join(screenshots_dir, filename)
            page.screenshot(path=filepath)
            print(f"\nScreenshot saved to: {filepath}")
