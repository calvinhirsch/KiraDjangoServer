from djongo.models import *

# USER COLLECTION

class Folder(Model):
    _id = ObjectIdField(db_column='_id', primary_key=True)
    name = CharField(max_length=127)

class AnalysisResults(Model):
    _id = ObjectIdField()
    actinic_keratoses = FloatField()
    basal_cell_carcinoma = FloatField()
    benign_keratosis = FloatField()
    dermatofibroma = FloatField()
    malignant_melanoma = FloatField()
    melanocytic_nevi = FloatField()
    vascular_lesions = FloatField()

class Photo(Model):
    _id = ObjectIdField()
    photo = TextField()
    date = DateTimeField() # may have to change to fit mongoDB
    folder = CharField(max_length=127)
    analysisResults = EmbeddedModelField(
        model_container=AnalysisResults,
    )

class SubmittedPhoto(Model):
    date = DateTimeField()
    photoId = CharField(max_length=24)

class UserTrial(Model):
    _id = ObjectIdField()
    trialId = CharField(max_length=24)
    submittedPhotos = ArrayModelField(
        model_container=SubmittedPhoto,
    )

class User(Model):
    _id = ObjectIdField()
    name = CharField(max_length=127)
    email = CharField(max_length=127)
    photos = ArrayModelField(
        model_container=Photo,
    )
    trials = ArrayModelField(
        model_container=UserTrial,
    )
    folders = ArrayModelField(
        model_container=Folder,
    )


# TRIAL COLLECTION

class DueDate(Model):
    _id = ObjectIdField()
    date = DateTimeField()
    
class EnrolledUser(Model):
    _id = ObjectIdField()
    uid = CharField(max_length=24)
    required = IntegerField()

class Trial(Model):
    _id = ObjectIdField()
    name = CharField(max_length=127)
    owner = CharField(max_length=30)
    description = CharField(max_length=999)
    contact = CharField(max_length=127)
    savePreProcessedPhoto = BooleanField()
    dueDates = ArrayModelField(
        model_container=DueDate,
    )
    enrolled = ArrayModelField(
        model_container=EnrolledUser,
    )
    
    