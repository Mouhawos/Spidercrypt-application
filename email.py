from flask import Flask, request, render_template_string
from flask_mail import Mail, Message
from urllib.parse import unquote
from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

app = Flask(__name__)

# Configuration de Flask-Mail en utilisant les variables d'environnement
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS') == 'True'
app.config['MAIL_USE_SSL'] = os.getenv('MAIL_USE_SSL') == 'True'
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = unquote(os.getenv('MAIL_PASSWORD'))  # Décoder le mot de passe encodé

mail = Mail(app)

@app.route('/send_email', methods=['POST'])
def send_email():
    name = request.form['firstName']
    email = request.form['email']
    company_name = request.form['companyName']
    company_size = request.form['companySize']
    industry = request.form['industry']
    customization_needs = request.form['customizationNeeds']
    budget = request.form['budget']
    additional_info = request.form['additionalInfo']

    msg = Message('New Contact Form Submission', 
                  sender=email, 
                  recipients=[os.getenv('MAIL_USERNAME')])

    msg.body = f"""
    Name: {name}
    Professional email address: {email}
    Company Name: {company_name}
    Size of the company: {company_size}
    Activity area: {industry}
    Customization Needs: {customization_needs}
    Planned budget: {budget}
    Additional Info: {additional_info}
    """

    try:
        mail.send(msg)
        return "Thank you for contacting us!"
    except Exception as e:
        return str(e)

@app.route('/')
def index():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="styles.css">
        <link rel="stylesheet" href="contact.css">
        <title>Contact us</title>
    </head>
    <body>
        <header class="header transparent">
            <nav>
                <div class="logo-container">
                    <img src="logo.png" alt="spider">
                </div>
                <ul>
                    <li><a href="index.html">Home</a></li>
                    <li><a href="https://spidercrypt.gitbook.io/spidercrypt-cybersecurity-apis-documentation">Documentation APIs</a></li>
                    <li><a href="https://spidercrypt.gitbook.io/white-paper/">White Paper</a></li>
                    <li><a href="contact.html">Contact</a></li>
                    <li><a href="https://large-emu-10.accounts.dev/sign-up" id="signUpLink">Sign Up</a></li>             
                </ul>
            </nav>
        </header>
        <main>
            <section class="contact-form">
                <h2>Contact us for personalized web security solutions </h2>
                <form id="contactForm" action="/send_email" method="post">
                    <label for="firstName">Name :</label>
                    <input type="text" id="firstName" name="firstName" required>
                    <label for="email">Professional email address :</label>
                    <input type="email" id="email" name="email" required>
                    <label for="companyName">Company Name :</label>
                    <input type="text" id="companyName" name="companyName">
                    <label for="companySize">Size of the company :</label>
                    <select id="companySize" name="companySize">
                        <option value="1-10">1-10 employees</option>
                        <option value="11-50">11-50 employees</option>
                        <option value="51-200">51-200 employees</option>
                    </select>
                    <label for="industry">Activity area :</label>
                    <input type="text" id="industry" name="industry">
                    <label for="customizationNeeds">Customization Needs :</label>
                    <textarea id="customizationNeeds" name="customizationNeeds" rows="4" required></textarea>
                    <label for="budget">Planned budget :</label>
                    <input type="text" id="budget" name="budget">
                    <label for="additionalInfo">Something to add ?</label>
                    <textarea id="additionalInfo" name="additionalInfo" rows="4"></textarea>
                    <button type="submit">Send</button>
                </form>
            </section>
        </main>
        <footer>
            <nav>
                <ul>
                    <li><a href="#">Privacy Policy</a></li>
                    <li><a href="#">Terms of Use</a></li>
                    <li><a href="#">Support</a></li>
                </ul>
            </nav>
            <div class="social-icons">
                <a href="https://www.linkedin.com/company/spidercrypt/?viewAsMember=true" target="_blank"><img src="linkedin.png" alt="Linkedin"></a>
                <a href="#" target="_blank"><img src="X.png" alt="Twitter"></a>
                <a href="#" target="_blank"><img src="instagram.png" alt="Instagram"></a>
            </div>
            <p>&copy; 2024 Spidercrypt. All rights reserved.</p>
        </footer>
    </body>
    </html>
    """)

if __name__ == '__main__':
    app.run(debug=True)
