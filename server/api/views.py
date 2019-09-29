from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from api.models import *
from api.serializers import *
import random, string
from pymongo import MongoClient
import logging
from django.utils import timezone
from api.imageanalysis import *

logger = logging.getLogger("mylogger")

def genKey():
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(24))

uid = "5d8fda000863c10647cf30bb"

@csrf_exempt
def index(request):
    return HttpResponse("This is an api u fool lmao")

@csrf_exempt
# POST: Get list of folders given a uid
def folders(request):
    if request.method == 'GET':
        return JsonResponse(None, status=400)
    elif request.method == 'POST':
        user = User.objects.get(_id=uid)
        folders = user.folders
        return_data = []
        for folder in folders:
            return_data.append(FolderSerializer(folder).data)
        return JsonResponse(return_data, status=200, safe=False)

@csrf_exempt
# POST: Add folder given a uid
def addFolder(request):
    if request.method == 'GET':
        return JsonResponse(None, status=400)
    elif request.method == 'POST':
        body = json.loads(request.body)
        folder = Folder(name=body["name"])
        user = User.objects.get(_id=uid)
        user.folders.append(folder)
        user.save()
        return JsonResponse({}, status=200, safe=False)
    
@csrf_exempt
# POST: Delete folder given a uid
def deleteFolder(request):
    if request.method == 'GET':
        return JsonResponse(None, status=400)
    elif request.method == 'POST':
        user = User.objects.get(_id=uid)
        body = json.loads(request.body)
        for folder in user.folders:
            if folder.name == body["name"]:
                user.folders.remove(folder)
        user.save()
        return JsonResponse({}, status=200, safe=False)

@csrf_exempt
# POST: Get list of photos given a folder and uid
def photosFromFolder(request):
    if request.method == 'GET':
        return JsonResponse(None, status=400)
    elif request.method == 'POST':
        user = User.objects.get(_id=uid)
        body = json.loads(request.body)
        folder_name = body["name"]
        return_data = []
        for photo in user.photos:
            if photo.folder == folder_name:
                return_data.append(PhotoSerializer(photo).data)
        return JsonResponse(return_data, status=200, safe=False)

@csrf_exempt
# POST: Send photo for analysis
def analyzePhoto(request):
    if request.method == 'GET':
        return JsonResponse(None, status=400)
    elif request.method == 'POST':
        user = User.objects.get(_id=uid)
        body = json.loads(request.body)
        
        img = readb64(body["photo"])
        img = square_crop(img)
        
        # might not work
        if (blur_metric(img) < 100):
            return JsonRespons({"valid": "false", "reason": "Image quality is too low."}, status=200, safe=False)
        
        img = cv_crop(img)
        #predictions = get_preds(img)
        predictions = [0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6]
        
        if max(predictions) < 0.5:
            return JsonRespons({"valid": "false", "reason": "ATTENTION JUDGES: WIL, THE RETARD WITH THE GLASSES, HAS AUTISM. PLEASE BE NICE"}, status=200, safe=False)
        
        return_data = {"valid": "true", "photo": {
            "photo": body["photo"],
            "date": "",
            "folder": "",
            "analysisResults": {
                "actinic_keratoses": predictions[0],
                "basal_cell_carcinoma": predictions[1],
                "benign_keratosis": predictions[2],
                "dermatofibroma": predictions[3],
                "malignant_melanoma": predictions[4],
                "melanocytic_nevi": predictions[5],
                "vascular_lesions": predictions[6]
            }
        }}
        
        return JsonResponse(return_data, status=200, safe=False)

@csrf_exempt
# POST: Add photo
def submitPhoto(request):
    if request.method == 'GET':
        return JsonResponse(None, status=400)
    elif request.method == 'POST':
        user = User.objects.get(_id=uid)
        body = json.loads(request.body)
        photo = Photo(**body["photo"])
        photo._id = genKey()
        photo.date = timezone.now()
        user.photos.append(photo)
        logger.info(PhotoSerializer(photo).data)
        logger.info(UserSerializer(user).data)
        # Ideally do checks to make sure photo is due
        for trial in user.trials:
            if trial.trialId == body["trialId"]:
                trial.submittedPhotos.append(SubmittedPhoto(date=photo.date,photoId=photo._id))
        user.save()
        return JsonResponse({}, status=200, safe=False)

@csrf_exempt
# POST: Delete photo given photo id and uid
def deletePhoto(request):
    print("deletePhoto")

@csrf_exempt
# POST: Get all enrolled trials
def getTrials(request):
    if request.method == 'GET':
        return JsonResponse(None, status=400)
    elif request.method == 'POST':
        user = User.objects.get(_id=uid)
        return_data = [];
        for t in user.trials:
            return_data.append(TrialSerializer(Trial.objects.get(_id=t.trialId)).data)
        return JsonResponse(return_data, status=200, safe=False)