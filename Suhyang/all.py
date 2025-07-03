import shutil

import pytest
import os

if __name__ == '__main__':
    reports_dir = 'reports'
    if os.path.exists(reports_dir):
        shutil.rmtree(reports_dir)
    pytest.main()
    os.system("allure generate reports -o allure-report --clean")