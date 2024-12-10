from setuptools import setup, find_packages

setup(
    name="link_extractor",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'requests>=2.31.0',
        'beautifulsoup4>=4.12.2',
        'aiohttp>=3.9.1',
    ],
    author="Samuel Levi Araújo Alves",
    author_email="samuel.levi.alves@gmail.com",
    description="Um extrator de links profissional com recursos avançados",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/samuelevi87/link-extractor-sl3v1",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
    entry_points={
        'console_scripts': [
            'link-extractor=link_extractor.cli:main',
        ],
    },
)