from setuptools import setup


setup(
    name="baselinewalk",
    version="0.1.0",
    py_modules=["baselinewalk"],
    author="Your Name",
    description="Ambient audio segment harmonizer and baseline comparison CLI tool",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    entry_points={
        "console_scripts": [
            "baselinewalk=baselinewalk:main",
        ],
    },
    python_requires=">=3.8",
)
