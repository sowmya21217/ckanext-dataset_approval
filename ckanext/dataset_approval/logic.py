# ckanext/dataset_approval/logic.py
from ckan import model
from ckan.logic import get_action
from ckanext.dataset_approval.plugin import DatasetApprovalPlugin

def set_status_pending(dataset_id):
    """Set a dataset's status to 'pending'."""
    dataset = model.Package.get(dataset_id)
    dataset['status'] = 'pending'
    dataset.save()

def approve_dataset(dataset_id):
    """Set dataset status to 'approved' and trigger publishing."""
    dataset = model.Package.get(dataset_id)
    dataset['status'] = 'approved'
    dataset.save()

    # Now publish the dataset on CKAN
    get_action('package_patch')(context={'user': 'admin'}, data_dict={'id': dataset.id, 'status': 'active'})

def reject_dataset(dataset_id):
    """Set dataset status to 'rejected'."""
    dataset = model.Package.get(dataset_id)
    dataset['status'] = 'rejected'
    dataset.save()
