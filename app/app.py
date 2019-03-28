from flask import Flask
import config


@app.route('/kpi')
def kpi():
    return "kpi"

if __name__ == '__main__':
    app.run()