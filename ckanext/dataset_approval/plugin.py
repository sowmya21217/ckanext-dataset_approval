# ckanext/dataset_approval/plugin.py
from ckan.plugins import SingletonPlugin, implements, IConfigurer
from ckan import model
from ckan.lib.mailer import send_mail
from ckan.logic import get_action
from ckan.lib.base import c

class DatasetApprovalPlugin(SingletonPlugin):
    implements(IConfigurer)

    def update_config(self, config):
        """This method is used to configure CKAN settings if necessary."""
        pass

    def create(self, context, data_dict):
        """Set the dataset's status to 'pending' when created."""
        data_dict['status'] = 'pending'
        dataset = model.Package.get(data_dict['id'])
        self.send_submission_email(dataset)

    def send_submission_email(self, dataset):
        """Send an email when a dataset is submitted."""
        send_mail(
            subject="Dataset Submission Received",
            message=f"Your dataset {dataset['name']} has been submitted and is pending approval.",
            recipients=[dataset['author_email']]
        )

    def approve_or_reject(self, context, data_dict):
        """Approve or reject the dataset."""
        dataset = model.Package.get(data_dict['id'])
        action = data_dict.get('action')

        if action == 'approve':
            self.approve_dataset(dataset)
        elif action == 'reject':
            self.reject_dataset(dataset)

    def approve_dataset(self, dataset):
        """Set the dataset status to 'approved' and publish it."""
        dataset['status'] = 'approved'
        dataset.save()

        # Publish the dataset using CKAN's API
        get_action('package_patch')(context={'user': 'admin'}, data_dict={'id': dataset.id, 'status': 'active'})
        
        self.send_approval_email(dataset)

    def reject_dataset(self, dataset):
        """Set the dataset status to 'rejected'."""
        dataset['status'] = 'rejected'
        dataset.save()

        self.send_rejection_email(dataset)

    def send_approval_email(self, dataset):
        """Send an email when the dataset is approved."""
        send_mail(
            subject="Your Dataset Has Been Approved",
            message=f"Your dataset {dataset['name']} has been approved and is now visible.",
            recipients=[dataset['author_email']]
        )

    def send_rejection_email(self, dataset):
        """Send an email when the dataset is rejected."""
        send_mail(
            subject="Your Dataset Has Been Rejected",
            message=f"Unfortunately, your dataset {dataset['name']} has been rejected.",
            recipients=[dataset['author_email']]
        )

    def before_view(self, context, data_dict):
        """Add dataset information and status to the admin page."""
        dataset = model.Package.get(data_dict['id'])
        return {
            'dataset_name': dataset['name'],
            'dataset_status': dataset['status'],
            'user': dataset['author']
        }
