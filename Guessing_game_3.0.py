from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def guessing_game():
    """
    A guessing game implemented using flask, where the app tries to guess the number picked by the user from the range
    of 0 to 1000. Required imports from flask: Flask, request render_template
    :return: render_template
    """
    if request.method == "GET":
        # setting limit values and guess to "" and passing them to the GET form
        min = 0
        max = 1000
        guess = ""
        # rendering the initial html
        return render_template("guessing_game.html", min=min, max=max, guess=guess)
    else:
        # setting success indicator to False, getting the limit values from the initial html and making the first guess
        success = False
        min = int(request.form.get("min"))
        max = int(request.form.get("max"))
        guess = round((((int(request.form["max"])) - int(request.form["min"])) / 2) + int(request.form["min"]))
        # depending on the accuracy of the first guess, the player indicates whether it was too high, too low or
        # accurate
        if request.form.get("indicator") == "too_high":
            # if computer's guess was too high, setting the max to the value of computer's guess
            max = guess
        elif request.form.get("indicator") == "too_low":
            # is computer's guess was too low, setting the min to the value of computer's guess
            min = guess
        elif request.form.get("indicator") == "success":
            success = True
        # making the guess based on the player's call on the accurace of computer's guess
        guess = round(((max - min) / 2) + min)
        # rendering the html and passing the arguments through
        return render_template("guessing_game.html", min=min, max=max, guess=guess, success=success)



if __name__ == "__main__":
    app.run()