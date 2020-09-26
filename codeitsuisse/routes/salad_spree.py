import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)


@app.route('/salad-spree', methods=['POST'])
def evaluateSaladSpree():
    data = request.get_json();
    logging.info("data sent for evaluation {}".format(data))
    # inputValue = data.get("input");
    result = []

    for test_case in data:
        result.append(findTotalPrice(test_case["number_of_salads"], test_case["salad_prices_street_map"]))

    logging.info("My result :{}".format(result))
    return json.dumps(result);


def findTotalPrice(minConsec, mapArr):
    lowest_sum = 100001
    for street in mapArr:
        available_consec_stores = 0
        for store_index in range(street.len):
            if street[store_index] == "X":
                available_consec_stores = 0;
                continue
            else:
                available_consec_stores += 1
                if available_consec_stores >= minConsec:
                    street_price_sum = 0
                    for i in range(minConsec):
                        street_price_sum += street[store_index - i]
                        if street_price_sum < lowest_sum:
                            lowest_sum = street_price_sum

    if lowest_sum == 100001:
        return 0
    else:
        return lowest_sum


