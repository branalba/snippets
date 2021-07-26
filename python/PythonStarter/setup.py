import setuptools
APP_VERSION = '0.1'

setuptools.setup(
    name='Python Starter',
    version='0.1',
    packages=['pythonstarter'],
    install_requires=[
        'Click',
        'pyinstaller'
    ],
    entry_points={
        'console_scripts': [
            'pythonstarter = pythonstarter.main:main',
        ],
    },
    author="Brandon Alba",
    author_email="branalba42@gmail.com"
)
