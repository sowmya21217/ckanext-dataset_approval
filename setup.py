from setuptools import setup

setup(
    name='ckanext-dataset_approval',
    version='0.1',
    description='A CKAN extension for dataset approval and rejection.',
    long_description='This CKAN extension adds dataset approval, rejection, and email notification features.',
    author='Sowmya',
    author_email='k.l.sowmya219@gmail.com',
    license='AGPL',
    packages=['ckanext.dataset_approval'],
    entry_points={
        'ckan.plugins': [
            'dataset_approval = ckanext.dataset_approval.plugin:DatasetApprovalPlugin'
        ],
    },
    install_requires=[
        'ckan>=2.11'
    ]
)
