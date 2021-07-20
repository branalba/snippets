from setuptools import setup, find_packages

APP_VERSION = '0.1'

setup(
        name = 'Python Starter',
        version = '0.1',
        packages = find_packages(),
        include_package_data = True,
        py_modules=['pythonstarter'],
        install_requires=[
            'Click',
            ],
        entry_points={
            'console_scripts': [
                'pythonstarter = pythonstarter.main:main',
                ],
            },
        author = "Brandon Alba",
	    author_email = "branalba42@gmail.com"
        )
