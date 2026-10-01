import flask 

app = flask(__name__)

@app.route("/")
def home_page():
    return {"message":"Containeraized Application"}

@app.route("/health")
def health_check():
    return {"status":"health"}

if "__name__" == "__main__":
    app.run(host="0.0.0.0", port=5000)