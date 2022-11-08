from operator import ge
import requests
import json
import time

###### FobeAPI ######
# made by coke on fobe




# I don't suggest using register. may be considered API abuse. I also haven't tested this.
def register(key, username, password, email):
    headers = {
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    payload = {
        'username': username,
        'email': email,
        'password': password,
        'cpassword': password,
        'signup_key': key,
        'rb': ''
    }
    r = requests.post('https://www.idk16.xyz/register', data=json.dumps(payload), headers=headers)



def shout(message,cookie):
    headers = {
        'content-type': 'application/json',
        'cookie': cookie,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    payload = {'shout': message}
    r = requests.post('https://api.idk16.xyz/user/feed/post', data=json.dumps(payload), headers=headers)
    return r

def is_online(id, cookie):
    headers = {
        'content-type': 'application/json',
        'cookie': cookie,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    r = requests.get(f'https://api.idk16.xyz/users/profile/info?userId={id}', headers=headers)
    data = r.json()
    siteStatus = data[0]['siteStatus']
    return siteStatus

def get_username(id, cookie):
    headers = {
        'content-type': 'application/json',
        'cookie': cookie,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    r = requests.get(f'https://api.idk16.xyz/users/profile/info?userId={id}', headers=headers)
    data = r.json()
    siteUsername = data[0]['username']
    return siteUsername 

def get_shout(id, cookie):
    headers = {
        'content-type': 'application/json',
        'cookie': cookie,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    r = requests.get(f'https://api.idk16.xyz/users/profile/info?userId={id}', headers=headers)
    data = r.json()
    siteShout = data[0]['shout']
    return siteShout

def get_blurb(id, cookie):
    headers = {
        'content-type': 'application/json',
        'cookie': cookie,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    r = requests.get(f'https://api.idk16.xyz/users/profile/info?userId={id}', headers=headers)
    data = r.json()
    siteBlurb = data[0]['blurb']
    return siteBlurb    

def get_visits(id, cookie):
    headers = {
        'content-type': 'application/json',
        'cookie': cookie,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    r = requests.get(f'https://api.idk16.xyz/users/profile/info?userId={id}', headers=headers)
    data = r.json()
    gameVisits = data[0]['placevisits']
    return gameVisits   


def get_friends(id, page, limit, cookie):
    headers = {
        'content-type': 'application/json',
        'cookie': cookie,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    r = requests.get(f'https://api.idk16.xyz/users/profile/friends?userId={id}&page={page}&limit={limit}', headers=headers)
    data = r.json()
    friendCount = data['friendsCount']
    return friendCount

def get_gameName(id, cookie):
    headers = {
        'content-type': 'application/json',
        'cookie': cookie,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    r = requests.get(f'https://api.idk16.xyz/game/info?id={id}', headers=headers)
    data = r.json()
    gameName = data['Name']
    return gameName

def get_gameDescription(id, cookie):
    headers = {
        'content-type': 'application/json',
        'cookie': cookie,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    r = requests.get(f'https://api.idk16.xyz/game/info?id={id}', headers=headers)
    data = r.json()
    gameDescription = data['Description']
    return gameDescription

def get_gameVisits(id, cookie):
    headers = {
        'content-type': 'application/json',
        'cookie': cookie,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    r = requests.get(f'https://api.idk16.xyz/game/info?id={id}', headers=headers)
    data = r.json()
    gameVisits = data['Visits']
    return gameVisits

def get_alphabux(id, cookie):
    headers = {
        'content-type': 'application/json',
        'cookie': cookie,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    r = requests.get(f'https://api.idk16.xyz/users/profile/info?userId={id}', headers=headers)
    data = r.json()
    gameVisits = data[0]['placevisits']
    return gameVisits + " AlphaBux"
