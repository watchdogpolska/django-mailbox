import sys
from setuptools import find_packages, setup
import os

from django_mailbox import __version__ as version_string

os.environ['DJANGO_SETTINGS_MODULE'] = 'django_mailbox.tests.settings'

from django.core import management

if len(sys.argv) > 1 and sys.argv[1] == 'test':
    management.execute_from_command_line()
    sys.exit()

tests_require = [
    'django',
    'mock',
    'unittest2',
]

gmail_oauth2_require = [
    'python-social-auth',
]

setup(
    name='django-mailbox',
    version=version_string,
    url='http://github.com/coddingtonbear/django-mailbox/',
    description=(
        'Import mail from POP3, IMAP, local mailboxes or directly from '
        'Postfix or Exim4 into your Django application automatically.'
    ),
    license='MIT',
    author='Adam Coddington',
    author_email='me@adamcoddington.net',
    extras_require={
        'gmail-oauth2': gmail_oauth2_require
    },
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Communications :: Email',
        'Topic :: Communications :: Email :: Post-Office',
        'Topic :: Communications :: Email :: Post-Office :: IMAP',
        'Topic :: Communications :: Email :: Post-Office :: POP3',
        'Topic :: Communications :: Email :: Email Clients (MUA)',
    ],
    packages=find_packages(),
    include_package_data = True,
    install_requires=[
        'six>=1.6.1'
    ]
)
