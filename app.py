from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Application Docker</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background: linear-gradient(135deg, #1d4ed8, #0f172a);
                    color: white;
                    text-align: center;
                    padding-top: 100px;
                }
                .card {
                    width: 70%;
                    margin: auto;
                    background: rgba(255,255,255,0.12);
                    padding: 30px;
                    border-radius: 20px;
                }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>Bonjour à tous</h1>
                <p>Ceci est une simple application conteneurisée avec Docker par TON_NOM.</p>
            </div>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
