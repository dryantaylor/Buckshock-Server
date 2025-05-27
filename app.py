from flask import Flask, render_template, request, jsonify, abort
import json
app = Flask(__name__)

triggered = False
trigger_level = 0
mode=None
@app.route("/")
def index():
    global triggered, trigger_level,mode
    if triggered:
        triggered = False
        prev_shock_time = trigger_level
        trigger_level = 0
        prev_mode = mode
        mode=None

        return prev_mode.lower()[0]+str(prev_shock_time) + "\r"

    return "n0\r"


@app.route("/trigger")
def trigger():

    global triggered, trigger_level,mode
    triggered = True
    trigger_level = request.args.get("level")
    mode = request.args.get("mode")
    if (mode.lower() in ["shock","vibe","beep"]
            and int(trigger_level) > 0):
        return {"triggered": triggered,
                "level": trigger_level,
                "mode": mode}


if __name__ == "__main__":
    #find correct host with ipconfig
    app.run(host="192.168.1.153")
