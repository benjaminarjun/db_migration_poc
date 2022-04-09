"""Form models for the sample application: a gym that offers online registrations and feedback"""


class RegistrationForm:
    """Registration information for a given gym member"""

    def __init__(self, form_id, member_name, phone_number, membership_level):
        self.form_id = form_id
        self.member_name = member_name
        self.phone_number = phone_number
        self.membership_level = membership_level

class FeedbackForm:
    """Feedback provided by a gym member via the website"""

    def __init__(self, feedback_id, member_name, feedback):
        self.feedback_id = feedback_id
        self.member_name = member_name
        self.feedback = feedback
