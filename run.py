from app import app

if __name__ == "__main__":
    app.run(host=app.config['app']['host'], \
        port=app.config['app']['port'], \
        debug=app.config['app']['debug'], ssl_context='adhoc')