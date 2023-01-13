import setuptools

# reading long description from file
with open('DESCRIPTION.txt') as file:
    long_description = file.read()

# external packages requirements
REQUIREMENTS = ['PyJWT==2.6.0', 'requests==2.28.1', 'cryptography==38.0.4']

CLASSIFIERS = [
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
]

# calling the setup function
setuptools.setup(name='zi_api_auth_client',
                 version='2.0.0',
                 description='A library that supports username-password and PKI authentication methods for enterprise-api',
                 long_description=long_description,
                 url='https://github.com/Zoominfo/api-auth-python-client',
                 author='Krishna Teja Dinavahi',
                 author_email='krishnateja.dinavahi@zoominfo.com',
                 license='MIT',
                 classifiers=CLASSIFIERS,
                 install_requires=REQUIREMENTS,
                 keywords='ZoomInfo enterprise-api pki-auth',
                 packages=setuptools.find_packages()
                 )
