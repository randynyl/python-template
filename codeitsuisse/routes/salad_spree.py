import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)


@app.route('/salad-spree', methods=['POST'])
def evaluateSaladSpree():
    data = request.get_json()
    print(data)
    logging.info("data sent for evaluation {}".format(data))
    # inputValue = data.get("input");
    result = {}
    result["result"] = findTotalPrice(data["number_of_salads"], data["salad_prices_street_map"])

    logging.info("My result :{}".format(result))
    return jsonify(result);


def findTotalPrice(minConsec, mapArr):
    lowest_sum = 100001
    for street in mapArr:
        available_consec_stores = 0
        for store_index in range(len(street)):
            if street[store_index] == "X":
                available_consec_stores = 0;
                continue
            else:
                available_consec_stores += 1
                if available_consec_stores >= minConsec:
                    street_price_sum = 0
                    for i in range(minConsec):
                        street_price_sum += int(street[store_index - i])
                    if street_price_sum < lowest_sum:
                        lowest_sum = street_price_sum

    if lowest_sum == 100001:
        return 0
    else:
        return lowest_sum


