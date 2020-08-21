from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import contacts
from .models import slack
from .models import tweet
from .models import dropbox
import json
from django.apps import apps
import requests

# loads contacts.json file to the contacts table
def load_files_contact(request):
    file_contact = open('acme_search\static\contacts.json')
    data = json.load(file_contact)
    for i in data['contacts']:
        id = i["id"]
        name = i["name"]
        company = i["company"]
        emails = i["emails"]
        phones = i["phones"]
        matching_terms = i["matching_terms"]
        last_contact = i["last_contact"]
        contact = contacts(id = id, name = name, company = company, emails = emails, phones = phones, matching_terms= matching_terms,last_contact= last_contact)
        contact.save()
    res = {
        "0": "success"
    }
    return JsonResponse(res)

# loads slack.json files to slack table
def load_files_slack(request):
    file_slack = open('acme_search\static\slack.json')
    data = json.load(file_slack)
    for i in data['slack']:
        id = i["id"]
        channel = i["channel"]
        author = i["author"]
        message = i["message"]
        timestamp = i["timestamp"]
        matching_terms = i["matching_terms"]
        slack_obj = slack(id=id, channel = channel, author = author, message= message, time_stamp=timestamp,
                           matching_terms=matching_terms)
        slack_obj.save()
    res = {
        "0": "success"
    }
    return JsonResponse(res)

# loads tweet file to tweet table
def load_files_tweet(request):
    file_tweet = open('acme_search/static/tweet.json')
    data = json.load(file_tweet)
    for i in data['tweet']:
        user = i["user"]
        message = i["message"]
        timestamp = i["timestamp"]
        matching_terms = i["matching_terms"]
        tweet_obj = tweet(user = user, message= message, time_stamp=timestamp,
                           matching_terms=matching_terms)
        tweet_obj.save()
    res = {
        "0": "success"
    }
    return JsonResponse(res)

# loads dropbox files to dropbox table
def load_files_dropbox(request):
    file_dropbox = open('acme_search\static\dropbox.json')
    data = json.load(file_dropbox)
    print(data)
    for i in data['dropbox']:
        print(i["id"])
        id = i["id"]
        path = i["path"]
        title = i["title"]
        shared_with = i["shared_with"]
        matching_terms = i["matching_terms"]
        created = i["created"]
        dropbox_obj = dropbox(id = id, path=path, title=title,shared_with=shared_with,
                          matching_terms=matching_terms,created=created)
        dropbox_obj.save()
    res = {
        "0": "success"
    }
    return JsonResponse(res)

# function to handle the search request
@csrf_exempt
def search(request):
    param = json.loads(request.body)
    query = param["data"]["name"]
    contact = contacts.objects.filter(matching_terms__contains=query)
    slacks =  slack.objects.filter(matching_terms__contains=query)
    dropboxs= dropbox.objects.filter(matching_terms__contains=query)
    tweets = tweet.objects.filter(matching_terms__contains=query)
    res = []
    temp = list(contact.values())
    for obj in range(len(temp)):
        temp[obj]['filename'] = "contacts"
    res += temp
    temp = list(tweets.values())
    for obj in range(len(temp)):
        temp[obj]['filename'] = "tweet"
    res += temp
    temp = list(slacks.values())
    for obj in range(len(temp)):
        temp[obj]['filename'] = "slack"
    res += temp
    temp = list(dropboxs.values())
    for obj in range(len(temp)):
        temp[obj]['filename'] = "dropbox"
    res += temp
    return JsonResponse(res, safe=False)

# function to handle the addition of matching_term to the existing matching_terms list
@csrf_exempt
def addTag(request):
    param = json.loads(request.body)
    filename = param["data"]["filename"]
    id = param["data"]["id"]
    tag = param["data"]["matching_name"]
    print(tag)
    filename = apps.get_model('acme_search', model_name= filename)
    c = filename.objects.get(id = id)
    c.matching_terms = tag
    c.save()
    return JsonResponse({})

# deletes a record from the table
@csrf_exempt
def delete(request):
    param = json.loads(request.body)
    filename = param["data"]["filename"]
    id = param["data"]["id"]
    name = param["data"]["name"]
    filename = apps.get_model('acme_search', model_name=filename)
    c = filename.objects.get(id=id)
    c.delete()
    return JsonResponse({})