from server.app import app


if __name__ == '__main__':
    print("Running server")
    app.run(host='0.0.0.0', port="5000", reload=True, debug=True)
