from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from flask import Flask, render_template, request, jsonify
import mysql.connector
from passlib.hash import bcrypt_sha256
import subprocess

'''try:
    from flask import Flask, render_template, request, jsonify
    import mysql.connector
    from passlib.hash import bcrypt_sha256
except ImportError:
    subprocess.run(["pip", "install", "flask mysql-connector-python passlib"])'''

app = Flask('Cagnotte')

# Connexion à la base de données
db_config = {
    'host': 'IP for your mysql server',
    'user': 'Your_user_name',
    'password': 'Your_password',
    'database': 'name_bdd'
}

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor(dictionary=True)


@app.route('/')
def index():
    cursor.execute("SELECT * FROM participants")
    participants = cursor.fetchall()
    cursor.execute("SELECT * FROM mots_interdit")
    mots_interdit = cursor.fetchall()
    return render_template('index.html', title='Cagnotte', participants=participants, mots_interdit=mots_interdit)


def envoyer_email(participant):
    # Configurer les détails du serveur SMTP Gmail avec une connexion sécurisée (TLS)
    smtp_username = 'leolepinette24@gmail.com'
    smtp_password = 'wflvqzyxolytkjnq'

    # Destinataire de l'e-mail
    destinataire = participant["email"]  # Remplacez par le champ de l'e-mail du participant

    # Construire le message
    sujet = 'Bienvenue dans la cagnotte !'
    corps_message = f'Ceci est un message automatique - ne pas répondre\n\nBonjour {participant["prenom"]},\n\n'
    message = MIMEMultipart()
    message['From'] = smtp_username
    message['To'] = destinataire
    message['Subject'] = sujet
    message.attach(MIMEText(corps_message, 'plain'))

    # Établir une connexion avec le serveur SMTP avec une connexion sécurisée (TLS)
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, destinataire, message.as_string())
        server.quit()

        return 'Email Sent!'
    except Exception as e:
        return str(e)


@app.route('/ajouter_p', methods=['POST'])
def ajouter_participant():
    prenom = request.form.get('prenom')
    nom = request.form.get('nom')
    email = request.form.get('email')

    insert_query = "INSERT INTO participants (prenom, nom, email, argents) VALUES (%s, %s, %s, 0)"
    data = (prenom, nom, email)  # Ajoutez l'e-mail à la liste des données

    cursor.execute(insert_query, data)
    conn.commit()

    nouveau_participant = {'prenom': prenom, 'nom': nom, 'email': email}
    print(envoyer_email(nouveau_participant))
    return jsonify(message="Participant ajouté avec succès. Un e-mail de bienvenue a été envoyé.", type="success")


@app.route('/supprimer_p/<int:id_participant>', methods=['POST'])
def supprimer_participant(id_participant):
    delete_query = "DELETE FROM participants WHERE id = %s"
    data = (id_participant,)

    cursor.execute(delete_query, data)
    conn.commit()

    return jsonify(message="Participant supprimé avec succès.", type="success")


@app.route('/modifier/<int:id_participant>', methods=['POST'])
def modifier_valeur(id_participant):
    nouvelle_valeur = int(request.form.get('nouvelleValeur'))  # Convertis la valeur en entier

    update_query = "UPDATE participants SET argents = argents + %s WHERE id = %s"
    data = (nouvelle_valeur, id_participant)

    cursor.execute(update_query, data)
    conn.commit()

    return jsonify(message="Argent modifiée avec succès.", type="success")


@app.route('/ajouter_m', methods=['POST'])
def ajouter_mot():
    mot = request.form.get('mot')
    prix = request.form.get('prix')

    insert_query = "INSERT INTO mots_interdit (mot, prix) VALUES (%s, %s)"
    data = (mot, prix)

    cursor.execute(insert_query, data)
    conn.commit()

    return jsonify(message="mot ajouté avec succès.", type="success")


@app.route('/supprimer_m/<int:id_mot>', methods=['POST'])
def supprimer_mot(id_mot):
    delete_query = "DELETE FROM mots_interdit WHERE id = %s"
    data = (id_mot,)

    cursor.execute(delete_query, data)
    conn.commit()

    return jsonify(message="mot supprimé avec succès.", type="success")


@app.route('/authentification', methods=['POST'])
def authentification():
    utilisateur = request.form.get('utilisateur')
    mdp = request.form.get('mdp')

    query = "SELECT pwd FROM id_connexion WHERE utilisateur = %s"
    cursor.execute(query, (utilisateur,))
    result = cursor.fetchone()

    if result:
        # Vérifier si le mot de passe fourni correspond au hachage stocké
        if bcrypt_sha256.verify(mdp, result['pwd']):
            return jsonify(message="Authentification réussie.", type="success")
        else:
            return jsonify(message="Authentification échouée.", type="error")
    else:
        return jsonify(message="Utilisateur non trouvé.", type="error")


app.run(debug=False, host='0.0.0.0', port=80)
