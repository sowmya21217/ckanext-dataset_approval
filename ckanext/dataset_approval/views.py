from ckan.lib.base import BaseController, c, render
from ckan.model import Dataset

class DatasetApprovalController(BaseController):
    def approval_status(self, dataset_id):
        dataset = Dataset.get(dataset_id)
        c.dataset = dataset
        return render('dataset_approval/approval_status.html')

    def approve(self, dataset_id):
        # Update dataset status to 'approved'
        approve_dataset(dataset_id)
        return redirect_to_action('view', dataset_id=dataset_id)

    def reject(self, dataset_id):
        # Update dataset status to 'rejected'
        dataset = Dataset.get(dataset_id)
        dataset.status = 'rejected'
        Session.commit()
        return redirect_to_action('view', dataset_id=dataset_id)
