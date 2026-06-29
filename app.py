from flask import Flask, render_template, request, redirect, session, abort, send_from_directory, jsonify
from flask_sqlalchemy import SQLAlchemy
import markdown
from markupsafe import Markup
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'goal26-dev-secret')
MODEL_DIR = os.path.abspath(os.path.dirname(__file__))
# Database configuration
DATABASE_URL = os.getenv('DATABASE_URL')
if DATABASE_URL and DATABASE_URL.startswith('postgres://'):
    DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL or 'postgresql://postgres:postgres@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

COUNTRY_FLAGS = {
    "Mexico": "https://hatscripts.github.io/circle-flags/flags/mx.svg",
    "South Africa": "https://hatscripts.github.io/circle-flags/flags/za.svg",
    "Korea Republic": "https://hatscripts.github.io/circle-flags/flags/kr.svg",
    "Czechia": "https://hatscripts.github.io/circle-flags/flags/cz.svg",
    "Canada": "https://hatscripts.github.io/circle-flags/flags/ca.svg",
    "Bosnia and Herzegovina": "https://hatscripts.github.io/circle-flags/flags/ba.svg",
    "USA": "https://hatscripts.github.io/circle-flags/flags/us.svg",
    "Paraguay": "https://hatscripts.github.io/circle-flags/flags/py.svg",
    "Haiti": "https://hatscripts.github.io/circle-flags/flags/ht.svg",
    "Scotland": "https://hatscripts.github.io/circle-flags/flags/gb-sct.svg",
    "Australia": "https://hatscripts.github.io/circle-flags/flags/au.svg",
    "Türkiye": "https://hatscripts.github.io/circle-flags/flags/tr.svg",
    "Brazil": "https://hatscripts.github.io/circle-flags/flags/br.svg",
    "Morocco": "https://hatscripts.github.io/circle-flags/flags/ma.svg",
    "Qatar": "https://hatscripts.github.io/circle-flags/flags/qa.svg",
    "Switzerland": "https://hatscripts.github.io/circle-flags/flags/ch.svg",
    "Côte d'Ivoire": "https://hatscripts.github.io/circle-flags/flags/ci.svg",
    "Ecuador": "https://hatscripts.github.io/circle-flags/flags/ec.svg",
    "Germany": "https://hatscripts.github.io/circle-flags/flags/de.svg",
    "Curaçao": "https://hatscripts.github.io/circle-flags/flags/cw.svg",
    "Netherlands": "https://hatscripts.github.io/circle-flags/flags/nl.svg",
    "Japan": "https://hatscripts.github.io/circle-flags/flags/jp.svg",
    "Sweden": "https://hatscripts.github.io/circle-flags/flags/se.svg",
    "Tunisia": "https://hatscripts.github.io/circle-flags/flags/tn.svg",
    "Uruguay": "https://hatscripts.github.io/circle-flags/flags/uy.svg",
    "Spain": "https://hatscripts.github.io/circle-flags/flags/es.svg",
    "Cabo Verde": "https://hatscripts.github.io/circle-flags/flags/cv.svg",
    "Saudi Arabia": "https://hatscripts.github.io/circle-flags/flags/sa.svg",
    "IR Iran": "https://hatscripts.github.io/circle-flags/flags/ir.svg",
    "New Zealand": "https://hatscripts.github.io/circle-flags/flags/nz.svg",
    "Belgium": "https://hatscripts.github.io/circle-flags/flags/be.svg",
    "Egypt": "https://hatscripts.github.io/circle-flags/flags/eg.svg",
    "France": "https://hatscripts.github.io/circle-flags/flags/fr.svg",
    "Senegal": "https://hatscripts.github.io/circle-flags/flags/sn.svg",
    "Iraq": "https://hatscripts.github.io/circle-flags/flags/iq.svg",
    "Norway": "https://hatscripts.github.io/circle-flags/flags/no.svg",
    "Argentina": "https://hatscripts.github.io/circle-flags/flags/ar.svg",
    "Algeria": "https://hatscripts.github.io/circle-flags/flags/dz.svg",
    "Austria": "https://hatscripts.github.io/circle-flags/flags/at.svg",
    "Jordan": "https://hatscripts.github.io/circle-flags/flags/jo.svg",
    "Ghana": "https://hatscripts.github.io/circle-flags/flags/gh.svg",
    "Panama": "https://hatscripts.github.io/circle-flags/flags/pa.svg",
    "Croatia": "https://hatscripts.github.io/circle-flags/flags/hr.svg",
    "Portugal": "https://hatscripts.github.io/circle-flags/flags/pt.svg",
    "DR Congo": "https://hatscripts.github.io/circle-flags/flags/cd.svg",
    "Uzbekistan": "https://hatscripts.github.io/circle-flags/flags/uz.svg",
    "Colombia": "https://hatscripts.github.io/circle-flags/flags/co.svg",
    "England": "https://hatscripts.github.io/circle-flags/flags/gb-eng.svg",
}

# Define Player model
class Player(db.Model):
    __tablename__ = 'players'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(50))
    team = db.Column(db.String(100))
    jersey_number = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    
    def __repr__(self):
        return f'<Player {self.name}>'

# Define Match model
class Match(db.Model):
    __tablename__ = 'matches'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(255))
    match_number = db.Column(db.String(50), unique=True)
    team1 = db.Column(db.String(255))
    team2 = db.Column(db.String(255))
    group = db.Column(db.String(50))
    stadium = db.Column(db.String(255))
    date_dt = db.Column(db.Date)
    win = db.Column(db.Numeric(precision=5, scale=2))
    loss = db.Column(db.Numeric(precision=5, scale=2))
    draw = db.Column(db.Numeric(precision=5, scale=2))

    def __repr__(self):
        return f'<Match {self.match_number}>'


# Your existing Match model remains untouched here...

class Match2(db.Model):
    __tablename__ = 'matches2'
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(255))
    match_number = db.Column(db.String(50), unique=True)
    team1 = db.Column(db.String(255))
    team2 = db.Column(db.String(255))
    group = db.Column(db.String(50))
    stadium = db.Column(db.String(255))
    date_dt = db.Column(db.Date)
    win = db.Column(db.Numeric(precision=5, scale=2))
    loss = db.Column(db.Numeric(precision=5, scale=2))
    draw = db.Column(db.Numeric(precision=5, scale=2))

    def __repr__(self):
        return f'<Match2 {self.match_number}>'


class MatchFeedback(db.Model):
    __tablename__ = 'match_feedback'

    id = db.Column(db.Integer, primary_key=True)
    match_id = db.Column(db.Integer, db.ForeignKey('matches.id'), nullable=False)
    feedback = db.Column(db.String(20), nullable=False)
    ip_address = db.Column(db.String(45), nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    match = db.relationship('Match', backref=db.backref('feedbacks', lazy=True))

    def __repr__(self):
        return f'<MatchFeedback match_id={self.match_id} feedback={self.feedback}>'


# Define Article model for blog posts (kept simple)
class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255), unique=True, nullable=False)
    body = db.Column(db.Text)
    published = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f'<Article {self.slug}>'


@app.route('/')
def index():
    """Display the homepage with published articles plus match predictions."""
    try:
        articles = Article.query.filter_by(published=True).order_by(Article.created_at.desc()).limit(5).all()

        matches = Match.query.filter(Match.id < 208).order_by(Match.id).all()

        match_predictions = {
            "Match 1": True,
            "Match 2": True,
            "Match 3": True,
            "Match 4": True,
            "Match 5": False,
            "Match 6": False,
            "Match 7": False,
            "Match 8": False,
            "Match 9": False,
            "Match 10": True,
            "Match 11": False,
            "Match 12": False,
            "Match 13": False,
            "Match 14": False,
            "Match 15": False,
            "Match 16": False,
            "Match 17": True,
            "Match 18": False,
            "Match 19": True,
            "Match 20": False,
            "Match 21": False,
            "Match 22": True,
            "Match 23": True,
            "Match 24": True,
            "Match 25": False,
            "Match 26": True,
            "Match 27": True,
            "Match 28": True,
            "Match 29": False,
            "Match 30": True,
            "Match 31": False,
            "Match 32": True,
            "Match 33": True,
            "Match 34": False,
            "Match 35": True,
            "Match 36": True,
            "Match 37": False,
            "Match 38": True,
            "Match 39": False,
            "Match 40": True,
            "Match 41": False,
            "Match 42": True,
            "Match 43": True,
            "Match 44": True,
            "Match 45": False,
            "Match 46": True,
            "Match 47": True,
            "Match 48": False,
            "Match 49": True,
            "Match 50": True,
            "Match 51": True,
            "Match 52": True,
            "Match 53": True,
            "Match 54": False,
            "Match 55": True,
            "Match 56": False,
            "Match 57": False,
            "Match 58": True,
            "Match 59": False,
            "Match 60": False,
            "Match 61": True,
            "Match 62": False,
            "Match 63": False,
            "Match 64": True,
            "Match 65": False,
            "Match 66": True,
            "Match 67": True,
            "Match 68": True,
            "Match 69": False,
            "Match 70": True,
            "Match 71": False,
            "Match 72": True
        }

        for match in matches:
            match.debug1 = match.match_number
            match.prediction = match_predictions.get(match.match_number, None)

            match.team1_flag_url = COUNTRY_FLAGS.get(match.team1)
            match.team2_flag_url = COUNTRY_FLAGS.get(match.team2)
            match.group_is_group = bool(match.group and match.group.strip().startswith('Group'))

        feedback_map = {
            item.match_id: item.feedback
            for item in MatchFeedback.query.order_by(MatchFeedback.id).all()
        }
        voted_matches = set(session.get('voted_matches', []))
        return render_template('index.html', articles=articles, matches=matches, feedback_map=feedback_map, voted_matches=voted_matches)
    except Exception as e:
        return f"<h1>Error fetching data</h1><p>{str(e)}</p>", 500


@app.route('/download-model')
def download_model():
    return send_from_directory('static', 'goal26_trained_model.pkl', as_attachment=True)


@app.route('/article/<slug>')
def article_detail(slug):
    article = Article.query.filter_by(slug=slug, published=True).first()
    if not article:
        abort(404)

    article_body_html = Markup(markdown.markdown(
        article.body or '',
        extensions=['extra', 'sane_lists'],
        output_format='html5'
    ))

    return render_template('article_detail.html', article=article, article_body_html=article_body_html, hide_banner=True)

@app.route('/create', methods=['GET', 'POST'])
def create_player():
    """Create a new player"""
    if request.method == 'POST':
        try:
            name = request.form['name']
            position = request.form.get('position')
            team = request.form.get('team')
            jersey_number = request.form.get('jersey_number', type=int)
            
            player = Player(name=name, position=position, team=team, jersey_number=jersey_number)
            db.session.add(player)
            db.session.commit()
            
            return redirect('/')
        except Exception as e:
            db.session.rollback()
            return f"<h1>Error creating player</h1><p>{str(e)}</p>", 500
    
    return render_template('create.html')


@app.route('/admin/submit', methods=['GET', 'POST'])
def admin_submit():
    """Password-protected article submission form.

    Protect the form using the `ADMIN_PASSWORD` environment variable.
    """
    # NOTE: intentionally hardcoded per user request
    ADMIN_PASSWORD = 'goal26Article'

    if request.method == 'POST':
        # simple password check
        provided = request.form.get('password')
        if not ADMIN_PASSWORD or provided != ADMIN_PASSWORD:
            return "<h1>Forbidden</h1><p>Invalid password.</p>", 403

        # collect fields (kept minimal)
        title = request.form.get('title')
        slug = request.form.get('slug')
        body = request.form.get('body')
        published = bool(int(request.form.get('published', '0')))

        # ensure slug uniqueness
        existing = Article.query.filter_by(slug=slug).first()
        if existing:
            return f"<h1>Conflict</h1><p>Slug '{slug}' already exists.</p>", 409

        try:
            article = Article(
                title=title,
                slug=slug,
                body=body,
                published=published,
            )
            db.session.add(article)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            db.session.rollback()
            return f"<h1>Error</h1><p>{str(e)}</p>", 500

    # GET: render the admin submit form; password field will be entered by admin
    return render_template('admin_submit.html')

@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    match_id = request.form.get('match_id', type=int)
    feedback = request.form.get('feedback')

    if not match_id or feedback not in ('agree', 'disagree'):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify({'success': False, 'error': 'Invalid request'}), 400
        return redirect('/')

    forwarded_for = request.headers.get('X-Forwarded-For')
    ip_address = forwarded_for.split(',')[0].strip() if forwarded_for else request.remote_addr

    voted_matches = set(session.get('voted_matches', []))
    if match_id in voted_matches:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return jsonify({'success': False, 'error': 'Already voted'}), 400
        return redirect('/')

    existing = MatchFeedback.query.filter_by(match_id=match_id).first()
    if existing:
        existing.feedback = feedback
        existing.ip_address = ip_address
    else:
        db.session.add(MatchFeedback(match_id=match_id, feedback=feedback, ip_address=ip_address))

    db.session.commit()
    voted_matches.add(match_id)
    session['voted_matches'] = list(voted_matches)
    session.modified = True
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return jsonify({'success': True, 'message': 'Thanks for your input'})
    return redirect('/')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
