from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('requirements.txt') as f:
    requirements = f.read()

setup(
    name='python_example_app',
    version='0.1',
    author='An7ar35',
    author_email='',
    description='Python skeleton app example',
    long_description=readme,
    url='https://github.com/an7ar35/mediascrub',
    license="MIT",
    install_requires=requirements,
    packages=find_packages(exclude=('tests', 'docs')),
    entry_points=dict(
        console_scripts=[
            'python_example_app=app.__main__:main'
        ]
    ),
    classifiers=["Environment :: Console",
                 "Operating System :: POSIX :: Linux"],
)
