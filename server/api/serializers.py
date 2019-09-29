from rest_meets_djongo.serializers import *
from api.models import *

class FolderSerializer(DjongoModelSerializer):
    class Meta:
        model = Folder
        fields = "__all__"

class AnalysisResultsSerializer(DjongoModelSerializer):
    class Meta:
        model = AnalysisResults
        fields = "__all__"

class PhotoSerializer(DjongoModelSerializer):
    class Meta:
        model = Photo
        fields = "__all__"

class SubmittedPhotoSerializer(DjongoModelSerializer):
    class Meta:
        model = SubmittedPhoto
        fields = "__all__"

class UserTrialSerializer(DjongoModelSerializer):
    class Meta:
        model = UserTrial
        fields = "__all__"

class UserSerializer(DjongoModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


# TRIAL COLLECTION

class DueDateSerializer(DjongoModelSerializer):
    class Meta:
        model = DueDate
        fields = "__all__"
    
class EnrolledUserSerializer(DjongoModelSerializer):
    class Meta:
        model = EnrolledUser
        fields = "__all__"

class TrialSerializer(DjongoModelSerializer):
    class Meta:
        model = Trial
        fields = "__all__"