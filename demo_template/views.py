import sys
import json
from flask import Flask, Blueprint, render_template, request
from .models import recieve
import argparse

view = Flask(__name__,  static_url_path='/demo_sakata/static', static_folder='static')
view.add_url_rule('/static/<filename>', 'static')

@view.route("/bert_tsubaki_test/demo.html", methods=['GET'])
def demo_tamba():
    return render_template('demo_top.html')

@view.route("/bert_tsubaki_test/post", methods=['POST'])
def callback():
    if request.method == 'POST':
        query_dict = dict(request.get_json(force=True))
        data = []
        query = query_dict["text"]
        data = recieve(query)
        return json.dumps(data, sort_keys=True, indent=4)

def main(args):
    view.run(host="0.0.0.0",port=12131)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    main(args)
