import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)


@app.route('/intelligent-farming', methods=['POST'])
def evaluateGMO():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    # inputValue = data.get("input");
    for sequenceEntry in data["list"]:
        sequenceEntry["geneSequence"] = rearrangeInput(sequenceEntry["geneSequence"])
    return jsonify(data);


def rearrangeInput(sequence):
    rearrangedSequence = ""
    num_of_a = 0
    num_of_c = 0
    num_of_g = 0
    num_of_t = 0
    for character in sequence:
        if character == 'A':
            num_of_a += 1
        elif character == 'C':
            num_of_c += 1
        elif character == 'G':
            num_of_g += 1
        elif character == 'T':
            num_of_t += 1

    while num_of_a >= 1 and num_of_c >= 1 and num_of_g >= 1 and num_of_t >= 1:
        rearrangedSequence += "ACGT"
        num_of_a -= 1
        num_of_c -= 1
        num_of_g -= 1
        num_of_t -= 1

    while num_of_a >= 2:
        rearrangedSequence += "AA"
        num_of_a -= 2
        if num_of_g > 0:
            rearrangedSequence += "G"
            num_of_g -= 1
            continue
        if num_of_t > 0:
            rearrangedSequence += "T"
            num_of_t -= 1
            continue
        if num_of_c >= 2:
            rearrangedSequence += "CC"
            num_of_c -= 2
            continue
        break

    while num_of_g > 0:
        rearrangedSequence += "G"
        num_of_g -= 1

    while num_of_t > 0:
        rearrangedSequence += "T"
        num_of_t -= 1

    while num_of_c > 0:
        rearrangedSequence += "C"
        num_of_c -= 1

    while num_of_a > 0:
        rearrangedSequence += "A"
        num_of_a -= 1

    return rearrangedSequence





