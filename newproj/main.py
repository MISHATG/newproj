from pickle import TRUE
from mysite import main_app
app = main_app()
if __name__=="__main__":
    app.run(debug=TRUE)