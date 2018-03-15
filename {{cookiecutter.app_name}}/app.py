import connexion

app = connexion.App(__name__)
app.add_api('swagger.yml')

# added to prevent bug with jsonify and sorted keys
app.app.config['JSON_SORT_KEYS'] = False

if __name__ == "__main__":
    app.run(port=8080)
