from flask import Flask,request,render_template
import requests
from bs4 import BeautifulSoup

application=Flask(__name__)

@application.route('/',methods=['GET','POST'])
def images():
    if  request.method == 'POST':
        query=request.form['image_name']
        req=requests.get(f"https://www.google.com/search?q={query}&client=firefox-b-d&sca_esv=573710622&tbm=isch&sxsrf=AM9HkKlUsSoFH6CLB8yfAmfwimLxfUQV_A:1697440002098&source=lnms&sa=X&ved=2ahUKEwi9zOjigPqBAxXOk1YBHXIJB3MQ_AUoAnoECAIQBA&biw=1536&bih=778&dpr=1.25")
        soup=req.content
        url=BeautifulSoup(soup,'html.parser')
        links=url.find_all('img')
        links.remove(links[0])
        return render_template('index1.html',links=links)
    return render_template('index.html')

if __name__=="__main__":
    application.run(debug=True)