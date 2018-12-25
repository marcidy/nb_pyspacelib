from setuptools import setup, find_packages

setup(
    name='pyspacelib',
    version='0.1',
    description='Python lib for interacting with physical Noisebridge',
    packages=find_packages(),
    url='http://github.com/marcidy/nb_pyspacelib',
    author='Matthew Arcidy',
    author_email='marcidy@gmail.com',
    license='MIT',
    install_requires=[
        'requests',
        'pillow'],
    include_package_data=True,
    zip_safe=False)
