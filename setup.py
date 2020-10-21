import setuptools

# reading long description from file
with open('DESCRIPTION.txt') as file:
    long_description = file.read()


# external packages requirements
REQUIREMENTS = ['PyJWT', 'requests']

CLASSIFIERS = [
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
]

# calling the setup function
setuptools.setup(name='zi_api_auth_client',
      version='1.0.1',
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