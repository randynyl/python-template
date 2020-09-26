import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)


@app.route('/clean_floor', methods=['POST'])
def evaluateCleanFloor():

    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    # inputValue = data.get("input");
    result = {"answers": {}}
    for key, value in data["tests"].items():
        result["answers"][key] = cleanFloor(value["floor"])

    logging.info("My result :{}".format(result))
    return jsonify(result);


def cleanFloor(floorArr):
    current_floor = 0
    number_of_moves = 0
    zeroList = [0] * len(floorArr)
    while floorArr != zeroList:
        current_floor += chooseDirectionToGo(floorArr, current_floor)
        if floorArr[current_floor] == 0:
            floorArr[current_floor] += 1
        else:
            floorArr[current_floor] -= 1
        number_of_moves += 1

    return number_of_moves


def chooseDirectionToGo(floorArr, currentFloor):
    if currentFloor == 0:
        return 1
    elif currentFloor == len(floorArr)-1:
        return -1
    elif floorArr[currentFloor + 1] > floorArr[currentFloor - 1]:
        return 1
    elif floorArr[currentFloor + 1] < floorArr[currentFloor - 1]:
        return -1
    else:
        max_dirt = 0
        floor_num = -1
        for i in range(len(floorArr)):
            if floorArr[i] > max_dirt and i != currentFloor:
                max_dirt = floorArr[i]
                floor_num = i
        if floor_num < currentFloor:
            return -1
        elif floor_num > currentFloor:
            return 1

