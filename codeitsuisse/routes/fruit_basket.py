import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)


@app.route('/fruitbasket', methods=['POST'])
def evaluateBasket():
    data = request.get_data()
    logging.info("data sent for evaluation {}".format(data))
    # inputValue = data.get("input");
    data_dictionary = eval(data)
    quantities = []
    for key, value in data_dictionary.items():
        logging.info("QUANTITY OF", key, "IS", value)
        quantities.append(value)
    estimate = findTotalWeight(quantities[0], quantities[1], quantities[2])
    result = "{}".format(estimate)
    logging.info("My result :{}".format(result))
    return result;


def findTotalWeight(qty1, qty2, qty3):
    weight1 = 18
    weight2 = 80
    weight3 = 25
    total_weight = (qty1 * weight1) + (qty2 * weight2) + (qty3 * weight3)
    return total_weight


