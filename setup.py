from setuptools import setup, find_packages

setup(
    name="xcytxs-setup",  # Package name
    version="0.1",        # Version
    author="Your Name",   # Your name
    author_email="your.email@example.com",  # Your email
    description="An automated setup tool for configuring services and installing dependencies.",
    long_description=open('README.md').read(),  # Read from the README.md file
    long_description_content_type='text/markdown',
    url="https://github.com/xcytxs/setup",  # The project repository URL
    packages=find_packages(),  # Automatically find your package
    install_requires=[
        'pip',   # Ensure pip is available
    ],
    entry_points={
        'console_scripts': [
            'xcytxs-setup = xcytxs_setup.main:main',  # The entry point for the CLI command
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
