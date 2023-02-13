from pymongo import MongoClient

client = MongoClient('mongodb+srv://sparta:test@cluster0.1spozhb.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

'''movie = db.movies.find_one({'title':'가버나움'})
target_star = movie['star']
movies = list(db.movies.find({},{'_id':False}))

for i in movies:
    print(i['tilte'])'''
    
db.movies.update_one({'title':'가버나움'},{'$set':{'star':0}})