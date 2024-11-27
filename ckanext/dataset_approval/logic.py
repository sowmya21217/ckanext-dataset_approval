from ckan.model import Dataset
from ckan.logic import get_action
from ckan.lib.mailer import send_mail
from ckan.lib.base import c

def send_approval_notification(dataset_id):
    dataset = Dataset.get(dataset_id)
    # Here, you would send an email to admins or notify users about approval
    send_mail(
        'Dataset Approval Needed',
        'admin@example.com',  # Send to admin or relevant users
        'A new dataset requires approval: {}'.format(dataset.name)
    )

def approve_dataset(dataset_id):
    dataset = Dataset.get(dataset_id)
    dataset.status = 'approved'
    send_approval_notification(dataset_id)
    # Optionally, do other things after approval, like logging or notifications
