from flask import Flask, render_template
from modules import convert_to_dict, make_ordinal

app = Flask(__name__)
application = app

# Create a list of dicts from the golfers CSV
golfers_list = convert_to_dict("golfers.csv")

# Create a list of tuples: (Rank, Player Name)
pairs_list = []
for p in golfers_list:
    pairs_list.append((p['Rank'], p['Player']))

# First route: Display the list of golfers
@app.route('/')
def index():
    return render_template('index.html', pairs=pairs_list, the_title="Golfers Index")

# Second route: Display details for a specific golfer
@app.route('/golfers/<num>')
def detail(num):
    try:
        golfers_dict = golfers_list[int(num) - 1]
    except:
        return f"<h1>Invalid value for Rank: {num}</h1>"
    # Use the make_ordinal function to convert the rank to an ordinal (e.g., 1st, 2nd)
    ord = make_ordinal(int(num))
    return render_template('golfers.html', golf=golfers_dict, ord=ord, the_title=golfers_dict['Player'])

# Keep this as is
if __name__ == '__main__':
    app.run(debug=True)