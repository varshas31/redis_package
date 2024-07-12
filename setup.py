# setup.py

from setuptools import setup, find_packages

setup(
    name='redis',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'uvicorn',
        'redis',
        'pydantic'
    ],
    entry_points={
        'console_scripts': [
            'my_redis_app = app.main:app',
        ],
    },
    python_requires='>=3.6',
)
