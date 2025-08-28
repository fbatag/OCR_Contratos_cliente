import os
from flask import Flask, request, render_template
from imageasylib.utils import getSaAcessToken, get_iap_user, getSignedUrlParam

print("(RE)LOADING APPLICATION")
TOKEN = os.environ.get("TOKEN", "TOKEN")
print(f"TOKEN: {TOKEN}")
VAL_DOCS_API = os.environ.get("VAL_DOCS_API", "http://127.0.0.1:8080/")
print(f"VAL_DOCS_API: {VAL_DOCS_API}")


app = Flask(__name__)
timezone = None

def get_user_version_info():
    return "User: " + get_iap_user() + " -  Version: 1.0.1"

@app.route("/getAuthToken", methods=["GET"])
def getSignedUrl():
    print("METHOD: getSignedUrl")
    return getSaAcessToken()

@app.route("/", methods=["GET"])
def index():
    print("METHOD: index -> " + request.method)
    return renderIndex()

def renderIndex(page="index.html"):
    print("METHOD: renderIndex -> ")
    return render_template(page,
                           user_version_info=get_user_version_info(),
                           token=TOKEN,
                           val_docs_api=VAL_DOCS_API)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
