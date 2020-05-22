import os
from notion.client import NotionClient
from flask import Flask
from flask import request
from flask import abort
from flask import jsonify

app = Flask(__name__)

def createNotionTask(token, collectionURL, title, link, author):
    # notion
    client = NotionClient(token)
    cv = client.get_collection_view(collectionURL, collection=None, force_refresh=True)
    #adding force_refresh seems to all the added row to be updated
    row = cv.collection.add_row()
    row.title = title
    row.link = link
    row.added = author



@app.route('/*')
def index():
    #grab security header
    #seczapkey = os.environ.get("ZAPKEY")
    #headzapkey = request.headers['zapkey']
    #if seczapkey == headzapkey
    #    return f'slacknotion'
    #return f'bad day for you'
    abort(403)


@app.route('/slack', methods=['GET'])
def slack():
    #changing for slack paths 
    if  request.headers['zapkey'] != 'kAohdJRHsaQY7YXrkoFzNTHD':
        abort(403)
    else:
        stitle = request.args.get('stitle')
        slink = request.args.get('slink')
        suser = request.args.get('suser')
        token_v2 = os.environ.get("TOKEN")
        url = os.environ.get("URL")
        createNotionTask(token_v2, url, stitle, slink, suser)
        return f'added {stitle} {slink} {suser} to Notion'


if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

