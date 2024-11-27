from setuptools import setup, find_packages

setup(
    name='ckanext-dataset_approval',
    version='0.1',
    description="CKAN Extension for dataset approval/rejection.",
    long_description="This extension allows for the approval/rejection of datasets before they are visible.",
    author="Sowmya",
    author_email="k.l.sowmya219@gmail.com",
    license="AGPL",
    packages=find_packages(),
    namespace_packages=['ckanext'],
    include_package_data=True,
    install_requires=[
        'CKAN>=2.9',  # CKAN version
    ],
    entry_points={
        'ckan.plugins': [
            'dataset_approval = ckanext.dataset_approval.plugin:DatasetApprovalPlugin',
        ]
    },
)
