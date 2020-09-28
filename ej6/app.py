#!/usr/bin/env python3 
from flask import ( Flask, render_template, request, abort, redirect, make_response, g, jsonify, ) 
import binascii 
import hashlib 
import json 
app = Flask(__name__) 
app.secret_key = open("secret_key", "r").read().strip() 
FLAG = open("flag.txt", "r").read().strip() 

def do_login(user, password, admin): 
    cookie = {"user": user, "password": password, "admin": admin} 
    cookie["digest"] = hashlib.sha512( secret_key + bytes(json.dumps(cookie, sort_keys=True), "ascii") ).hexdigest() 
    cookie_value = binascii.hexlify(json.dumps(cookie).encode("utf8")) 
    return cookie_value

@app.route("/login", methods=["POST"]) 
def login(): 
    user = request.form.get("user", "") 
    password = request.form.get("password", "") 
    if ( user != "hacker" or hashlib.sha512(bytes(password, "ascii")).digest() != b"hackshackshackshackshackshackshackshackshackshackshackshackshack" ): 
        return abort(403) 
    return do_login(user, password, True) 

def load_cookie(): 
    cookie = {} 
    auth = request.cookies.get("auth") 
    if auth: 
        try: 
            cookie = json.loads(binascii.unhexlify(auth).decode("utf8")) 
            digest = cookie.pop("digest") 
            if ( digest != hashlib.sha512( app.secret_key + bytes(json.dumps(cookie, sort_keys=True), "ascii") ).hexdigest() ): 
                return False, {} 
        except: 
            pass 
    return True, cookie 

@app.route("/logout", methods=["GET"]) 
def logout(): 
    response = make_response(redirect("/")) 
    response.set_cookie("auth", "", expires=0) 
    return response 
    
@app.route("/") 
def index(): 
    ok, cookie = load_cookie() 
    if not ok: 
        return abort(403) 
    return render_template( "index.html", user=cookie.get("user", None), admin=cookie.get("admin", None), flag=FLAG, )

@app.route("/robots.txt") 
def source(): 
    return "" + open(__file__).read() + "" 

if __name__ == "__main__":
     app.run(debug=True, host="0.0.0.0", port=1337)