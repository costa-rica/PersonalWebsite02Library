from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup (
    name="pw-library",
    version="0.1",
    author="NickRodriguez",
    author_email="nick@dashanddata.com",
    description="pw stands for Personal Website.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/costa-rica/PersonalWebsite02Library",
    packages=['pw_config', 'pw_models','pw_tools'],
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
