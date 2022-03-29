from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='package_template',
    packages=['package_template'],
    version='CURRENT_VERSION',
    license='MIT',
    description='Python package project template',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Roger Vilà',
    author_email='rogervila@me.com',
    url='https://github.com/rogervila/package_template',
    download_url='https://github.com/rogervila/package_template/archive/CURRENT_VERSION.tar.gz',
    keywords=['package template', 'project template', 'pypi template'],
    install_requires=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],
)
