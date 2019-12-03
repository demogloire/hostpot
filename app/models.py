from app import db, login_manager
from datetime import datetime
from flask_login import UserMixin, current_user

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(128))
    postNom = db.Column(db.String(128))
    prenom= db.Column(db.String(128))
    age = db.Column(db.Integer)
    telephone = db.Column(db.String(60))
    email = db.Column(db.String(128),nullable=False)
    password = db.Column(db.String(120), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.png')
    validite = db.Column(db.Boolean, default=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
    macabes = db.relationship('Macabe', backref='user_macabe', lazy='dynamic')
    files = db.relationship('File', backref='user_file', lazy='dynamic')
    commentaires = db.relationship('Commentaire', backref='user_commentaire', lazy='dynamic')
    dates=db.Column(db.DateTime, nullable=False, default=datetime.utcnow )
    publications = db.relationship('Publication', backref='user_publication', lazy='dynamic')
    date_create=db.Column(db.DateTime, nullable=False, default=datetime.utcnow )
    date_update=db.Column(db.DateTime, nullable=False, default=datetime.utcnow )


    def __repr__(self):
        return ' {} '.format(self.nom)
    
class Macabe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cours = db.Column(db.String(128))
    journee = db.Column(db.String(128))
    section=db.Column(db.String(128))
    annee = db.Column(db.Integer)
    session = db.Column(db.String(60))
    description = db.Column(db.Text)
    enseignant = db.Column(db.String(128))
    promotion = db.Column(db.String(128))
    titulaire = db.Column(db.Boolean, default=False)
    corrige= db.Column(db.Boolean, default=False)
    macabe= db.Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    etablissement_id = db.Column(db.Integer, db.ForeignKey('etablissement.id'), nullable=False)
    files = db.relationship('File', backref='macabe_file', lazy='dynamic')
    commentaires = db.relationship('Commentaire', backref='macabe_commentaire', lazy='dynamic')
    date_create=db.Column(db.DateTime, nullable=False, default=datetime.utcnow )
    date_update=db.Column(db.DateTime, nullable=False, default=datetime.utcnow )


    def __repr__(self):
        return ' {} '.format(self.cours)

class Role(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    designation = db.Column(db.String(60))
    users = db.relationship('User', backref='role_user', lazy='dynamic')
    date_create=db.Column(db.DateTime, nullable=False, default=datetime.utcnow )
    date_update=db.Column(db.DateTime, nullable=False, default=datetime.utcnow )


    def __repr__(self):
        return ' {} '.format(self.designation)

class Config(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    enseignant = db.Column(db.String(128))
    cours = db.Column(db.String(128))
    ville = db.Column(db.String(128))
    annee = db.Column(db.Integer)
    journee= db.Column(db.String(128))
    section= db.Column(db.String(128))

    def __repr__(self):
        return ' {} '.format(self.nom)

class Commentaire(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text)
    response_user=db.Column(db.Boolean, default=False)
    macabe_id = db.Column(db.Integer, db.ForeignKey('macabe.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date_create=db.Column(db.DateTime, nullable=False, default=datetime.utcnow )
    date_update=db.Column(db.DateTime, nullable=False, default=datetime.utcnow )

    def __repr__(self):
        return " {} "  .format(self.message)

class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    macabe_id = db.Column(db.Integer, db.ForeignKey('macabe.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    publication_id = db.Column(db.Integer, db.ForeignKey('publication.id'))
    upload_user=db.Column(db.Boolean, default=False)
    download_user=db.Column(db.Boolean, default=False)
    date_create=db.Column(db.DateTime, nullable=False, default=datetime.utcnow )
    date_update=db.Column(db.DateTime, nullable=False, default=datetime.utcnow )


class Etablissement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    designation = db.Column(db.String(128))
    province = db.Column(db.String(128))
    ville = db.Column(db.String(128))
    macabes = db.relationship('Macabe', backref='etablissement_macabe', lazy='dynamic')
    date_create=db.Column(db.DateTime, nullable=False, default=datetime.utcnow )
    date_update=db.Column(db.DateTime, nullable=False, default=datetime.utcnow )

    def __repr__(self):
        return "{}".format(self.designation)

class Categorie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(128))
    publications = db.relationship('Publication', backref='categorie_publication', lazy='dynamic')
    date_create=db.Column(db.DateTime, nullable=False, default=datetime.utcnow )
    date_update=db.Column(db.DateTime, nullable=False, default=datetime.utcnow )

    def __repr__(self):
        return "{}".format(self.nom)

class Publication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom_auteur= db.Column(db.String(128))
    titre = db.Column(db.String(128))
    maison_edition = db.Column(db.String(128))
    Lieu = db.Column(db.String(128))
    annee=db.Column(db.Integer)
    resume=db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    categorie_id = db.Column(db.Integer, db.ForeignKey('categorie.id'))
    date_create=db.Column(db.DateTime, nullable=False, default=datetime.utcnow )
    date_update=db.Column(db.DateTime, nullable=False, default=datetime.utcnow )
    files = db.relationship('File', backref='publication_file', lazy='dynamic')

    def __repr__(self):
        return "{}".format(self.titre)

