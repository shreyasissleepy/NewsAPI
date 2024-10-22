from setuptools import setup, find_packages

setup(
    name='wrapper_news_api',  
    version='0.6',  
    description='A Python package to fetch news from BBC, ABP News, and India Today',
    long_description=open('./README.md','r',encoding='utf-8').read(),
    long_description_content_type='text/markdown',  
    url='https://github.com/shreyasissleepy/NewsAPI',  
    author='Shreyas Naik',
    author_email='shreyasnaik179@gmail.com',
    license='MIT',  
    packages=find_packages(),
    install_requires=[
        'requests',  
        'beautifulsoup4'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',  
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.7',  
)
