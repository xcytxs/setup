from setuptools import setup, find_packages

setup(
    name="xcytxs-setup",  # Your package name
    version="0.1",        # Version of your package
    author="Your Name",
    author_email="your.email@example.com",
    description="An automated installation tool for Python apps.",
    long_description=open('README.md').read(),  # README file as long description
    long_description_content_type='text/markdown',
    url="https://github.com/xcytxs/setup",  # URL for the project repository
    packages=find_packages(),  # Automatically find packages
    install_requires=[
        'pip',   # Include pip if you need it for installation
        'requests',  # Include any external dependencies here
        # add other dependencies like `portchecker`, etc., if required
    ],
    entry_points={
        'console_scripts': [
            'xcytxs-setup = setup.main:main_function',  # Main entry point for your app
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
