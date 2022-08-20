from setuptools import find_packages, setup

with open('README.md','r') as f:
    long_description = f.read()

    setup(
            name = 'pgbackup',
            version = '0.1.0',
            author = 'Tanmesh Bhokare',
            author_email = 'tanmesh@devops.com'
            description = 'Backup  CLI',
            long_description = long_description,
            long_description_content_typr = 'text/markdown',
            url = 'https://github.com/tanmeshbhokare/build_cli.git',
            packages = find_packages('src')
            )
