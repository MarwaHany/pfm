from rest_api.app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=5000)