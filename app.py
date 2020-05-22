import os
from notion.client import NotionClient
from flask import Flask
from flask import request


app = Flask(__name__)


def createNotionTask(token, collectionURL, content):
    # notion
    client = NotionClient(token)
    cv = client.get_collection_view(collectionURL, collection=None, force_refresh=True)
    #adding force_refresh seems to all the added row to be updated
    row = cv.collection.add_row()
    row.title = content


@app.route('/slack', methods=['GET'])
def slack():
    #changing for slack paths
    name = request.args.get('name')
    token_v2 = os.environ.get("TOKEN")
    url = os.environ.get("URL")
    createNotionTask(token_v2, url, name)
    return f'added {name} to Notion'


if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
