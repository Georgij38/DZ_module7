from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.0.5',
    description='Program for sorting files by extension',
    url='https://github.com/Georgij38/DZ_moduie6.git',
    author='Jegor Zaharov',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['cleanfolder = clean_folder.sort_file_ext:main']}
)
