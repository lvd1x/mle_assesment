from flask import Flask, render_template, request, redirect
import model
import controller
import re

app = Flask(__name__)
m = model.ImgModel()

def parse_input(string_token):
    """Parses input string into list of ints/floats as strings"""

    return re.findall(r"[-+]?\d*\.\d+|\d+", string_token)


@app.route('/', methods=['GET', 'POST'])
def index(c=controller.ImgController(m)):

    if request.method == "POST":

        # parses inputs into lists of strings
        img_size_string = parse_input(request.form['imgsize'])
        corners_string = parse_input(request.form['corners'])

        try:
            # if length of either parsed input is incorrect, redirected with no solution
            if (len(img_size_string) != 2) or (len(corners_string) != 8):
                c.clear_solution()
                return redirect('/')
            else:
                c.parse_size(img_size_string)
                c.parse_corners(corners_string)
                c.solve()
                return redirect('/')
        except:
            return "issue processing POST request"
    else: 
        solution = c.get_solution()
        return render_template('index.html', solution=solution)

if __name__ == "__main__":
    app.run(debug=True)