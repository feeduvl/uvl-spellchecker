from flask import Flask, Response, json, jsonify, request

from main.behavior.Spellchecker import Spellchecker
from main.tooling.Logger import logging_setup

# from flask_cors import CORS


logger = logging_setup(__name__)

app = Flask(__name__)
# cors only for local testing
# cors = CORS(app)


class ComponentSpellcheckerRestConnectorProvider():
    """
        Description: Entrypoint for calling the SpellcheckerService.
    """

    @app.route("/hitec/spellchecker/run", methods=["POST"])
    def do_spellchecking() -> Response:  # type: ignore
        app.logger.debug("/hitec/spellchecker/run called")

        content = json.loads(request.data.decode("utf-8"))

        spellchecker = Spellchecker()
        resultMessage = spellchecker.startSpellchecking(content)

        result = dict()
        result.update({"message": resultMessage})
        app.logger.info(result)

        return jsonify(result)

    @app.route("/hitec/spellchecker/status", methods=["GET"])
    def get_status() -> Response:  # type: ignore
        try:
            app.logger.info("Status requested")
            status = {
                "status": "operational",
            }
        except Exception as e:
            status = {"status": "not_operational", "error": str(e)}

        return jsonify(status)

    if __name__ == "__main__":
        app.run(debug=False, host="0.0.0.0", port=9699)
