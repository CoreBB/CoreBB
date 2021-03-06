import pymongo
import config
import random
import time
import string
from bson import ObjectId


db = pymongo.MongoClient(config.dbhost, config.port).corebb

def getUsers():
    members = []
    for x in db.members.find():
        members.append(x)
    return members

def getUser(user):
    return db.members.find_one({"username":user})

def getOnlineUsers():
    online = []
    members = db.members.find()
    for member in members:
        if time.time() - member['lastonline'] <= 60 * 5:
            online.append(member)
    return online

def getPosts(threadId):
    return [post for post in db.posts.find({"threadId":threadId})]

def getPost(_id):
    return db.posts.find_one({"_id":ObjectId(_id)})    

def getThreads(section):
    return [thread for thread in db.threads.find({"section":section})]

def getThread(section, _id):
    return db.threads.find_one({"_id":ObjectId(_id), "section":section})

def getUserField(username, field):
    check = getUser(username)
    if field not in check:
        updateUser(username, {field:[]}) # Default as array which is also None

def makeThread(username, content, section, title):
    db.threads.insert({"username":username, "title":title, "body":content, "section":section, "lastpost":time.time()})

def makePost(username, content, threadId):
    db.posts.insert({"username":username, "body":content, "threadId":threadId, "timestamp":time.time()})

def insert(into, data):
    db[into].insert(data)

def updateUser(username, data):
    db.members.update({"username":username}, {"$set":data})

def register(username, password, email, dob, referrer):
    check_user = db.members.find_one({"username":username})
    check_email = db.members.find_one({"email":email})

    if check_user:
        return {"success":False, "message":"Username already exists."}
    
    elif check_email:
        return {"success":False, "message":"Email already taken."}

    if referrer:
        data = getUser(referrer)
        referrals = data['referrals']
        referrals.append(username)
        updateUser(referrer, {"referrals":referrals})
    
    insert("members", {"username":username, "password":password, "email":email, "timestamp":time.time(), "lastonline":time.time(), "referrals":[], "group":"Users"})

    return {"success":True, "message":"Registeration successful!"}

def getSeed(): # When hashing
    seed = db.seed.find_one()
    if not seed:
        db.seed.insert({"seed":''.join([random.choice(string.uppercase+string.lowercase+string.digits) for x in range(100)])})
        return db.seed.find_one()['seed']
    else:
        return seed['seed']

