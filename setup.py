from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

classifiers = [
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'License :: OSI Approved :: MIT License',
]

setup(name='get_retries',
      version='0.1.0',
      description="Adding retries to Requests.get() with exponential backoff",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/jfilter/get_retries',
      author='Johannes Filter',
      author_email='hi@jfilter.de',
      license='MIT',
      packages=['get_retries'],
      install_requires=['requests'],
      classifiers=classifiers)
