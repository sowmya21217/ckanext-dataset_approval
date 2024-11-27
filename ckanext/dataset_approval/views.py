# ckanext/dataset_approval/views.py
import ckan.logic as logic
from ckan.lib.base import c, render
from ckanext.dataset_approval.logic import approve_dataset, reject_dataset

def dataset_approval_view(dataset_id):
    """Display the dataset details along with approval/rejection options."""
    dataset = logic.get_action('package_show')(context={'user': 'admin'}, data_dict={'id': dataset_id})
    
    return render('dataset_approval/dataset_approval.html', {
        'dataset_name': dataset['name'],
        'dataset_status': dataset['status'],
        'user': dataset['author']
    })

def dataset_approve_or_reject(dataset_id, action):
    """Approve or reject the dataset based on the admin action."""
    if action == 'approve':
        approve_dataset(dataset_id)
    elif action == 'reject':
        reject_dataset(dataset_id)

    return render('dataset_approval/dataset_approval.html', {'status': 'success'})
