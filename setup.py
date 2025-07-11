from setuptools import setup, find_packages

setup(
    name="caelum-sys",
    version="0.1.6",
    description="A human-friendly system automation layer for scripting and AI agents",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Joshua Wells",
    packages=find_packages(),
    install_requires=[
        "psutil",
        "pyautogui",
        "requests",  # For network tools and potential LLM integration
        "pillow",    # Required by pyautogui for screenshots
    ],
    entry_points={
        "console_scripts": [
            "caelum-sys=caelum_sys.cli:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: System :: Shells",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.7",
    include_package_data=True
)
