import flask
import pickle
# Use pickle to load in the pre-trained model.
with open(f'model/model.pkl', 'rb') as f:
    model = pickle.load(f)
app = flask.Flask(__name__, template_folder='templates')
@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))
    if flask.request.method == 'POST':
        review = flask.request.form['review']
        #input_variables = pd.DataFrame([[review]],columns=['review'],dtype=string)
        prediction = model.predict([review])
        return flask.render_template('main.html',original_input={'review':review},result=prediction, )
if __name__ == '__main__':
    app.run()