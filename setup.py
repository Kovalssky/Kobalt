from setuptools import setup, find_packages

setup(
    name='kobalt',
        version='0.1.0',
            packages=find_packages(),
                install_requires=[
                        "requests"
                            ],
                                description='Работа с Cobalt API',
                                    long_description=open('README.md').read(),
                                        long_description_content_type='text/markdown',
                                            url='https://github.com/Kovalssky/Kobalt',
                                                author='devKovalsky',
                                                    author_email='xxboxf@gmail.com',
                                                        license='MIT',
                                                        )

