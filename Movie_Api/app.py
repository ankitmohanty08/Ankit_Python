
# from dotenv import load_dotenv
import os
from flask import Flask, request, Response, make_response
# from flask_httpauth import HTTPBasicAuth
from bson import json_util
import json
from pymongo import MongoClient


# myclient = MongoClient("mongodb://localhost:27017/")#--------> Connecting to local MongoDB
# load_dotenv() 
password=os.environ.get("password")

# password="Password123"
DATABASE_URL=f'mongodb+srv://admin:{password}'\
              '@movieapi.rleb4.mongodb.net/?'\
              'retryWrites=true&w=majority'
              
myclient=MongoClient(DATABASE_URL)


movieDB = myclient["movieDB"]
movies = movieDB["movies"]

USER_DATA={
    "username":"admin",
    "password":"Password123"
}


app=Flask(__name__)
# auth=HTTPBasicAuth()


# @auth.verify_password
# def verify(username,password):
#     if not (username and password):
#         return False
#     return (USER_DATA["username"]==username and USER_DATA["password"]==password)

@app.route('/movieratings',methods=['GET','POST'])
# @auth.login_required
def movieratings():
    # Handling GET request
    headers=request.headers
    if "Uname" and "Psword" in headers.keys():
        username=headers["uname"]
        password=headers["psword"]
        if not (username and password):
            return make_response({"Error":"Authorization Failed!!"},401)
        elif (USER_DATA["username"]==username and USER_DATA["password"]==password):
            if request.method == 'GET':
                movie_name=request.args.get('mname') #---------------> Getting Paramater 'mname'
                if movie_name is None:
                    '''
                    Return all movie data if no paramter passed
                    '''
                    movie_data=list(movies.find({},{"_id":0})) 
                else:
                    '''
                    Find and return the movie by movie_name
                    '''
                    movie_data=list(movies.find({"movie_name":{"$regex":movie_name.strip()}},{"_id":0}))    
                    
                '''ObjectID can't be serialized to json format using jsonify,
                So json_util helps to dump data to json which is wrapped inside Response class of flask
                '''    
                
                # print(len(list(movie_data)))
                if len(movie_data)==0:
                    
                    return make_response({"Error":"No Movie Found!!"},404)
                else:
                    return Response(json_util.dumps(movie_data),mimetype='application/json') 
            
            # Handling POST request
            elif request.method=='POST':
                movie_input_data=json.loads(request.data)
                # movie_input_data =request.get_json(force=True) #-----> Getting input data parsed in form of Pyhton dictionary
                movie_name=movie_input_data["movie_name"].strip()
                cur=movies.find({"movie_name":movie_name},{"_id":0})
                if len(list(cur))==0:
                    movies.insert_one(movie_input_data) #----------------> Writing the data to movies collection
                    return "Successfully Inserted."
                else:
                    return make_response({"Error":"Movie Already Exist!!"})

    return make_response({"Error":"Authorization Failed!!"},401)        


if __name__ == '__main__':
    app.run(debug=False)    