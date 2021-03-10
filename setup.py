import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README_EN.md')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'setuptools>=40.3.0',
    'easydict==1.9',
    'numpy',
    'tqdm==4.31.1',
    'torchvision',
    'torch',
    'opencv_python',
    'Pillow==7.1.2',
    'tensorboardX==2.0',
]

tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest >= 3.7.4',
    'pytest-cov',
]

setup(
    name='anti_spoofing',
    version='0.1',
    description='Face Spoof',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='',
    author_email='',
    url='',
    keywords='spoof',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': tests_require,
    },
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = face_verify:main',
        ],
        'console_scripts': [
            'start_face_processing=face_verify.app:main'
        ]
    },
)

