import setuptools

setuptools.setup(
    name='orderdict',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
