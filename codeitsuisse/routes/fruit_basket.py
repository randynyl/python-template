import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)


@app.route('/fruitbasket', methods=['POST'])
def evaluateBasket():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    # inputValue = data.get("input");
    quantities = []
    for key, value in data.items():
        quantities.append(value)
    estimate = findTotalWeight(quantities[0], quantities[1], quantities[2])
    result = "{}".format(estimate)
    logging.info("My result :{}".format(result))
    return result;


def findTotalWeight(qty1, qty2, qty3):
    weight1 = 50
    weight2 = 50
    weight3 = 50
    total_weight = (qty1 * weight1) + (qty2 * weight2) + (qty3 * weight3)
    return total_weight


