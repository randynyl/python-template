import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)


@app.route('/cluster', methods=['POST'])
def evaluateCluster():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    # inputValue = data.get("input");
    result = {}
    result["answer"] = findNumClusters(data)
    logging.info("My result :{}".format(result))
    return jsonify(result);


def findNumClusters(area):
    clusterCount = 0
    for i in range(len(area)):
        for j in range(len(area[0])):
            if area[i][j] == "1":
                spread(area, i, j)
                clusterCount += 1
    return clusterCount


def spread(area, row, col):
    area[row][col] = "2"
    for i in range(row-1, row+2):
        if i < 0 or i > len(area)-1:
            continue
        else:
            for j in range(col-1, col+2):
                if j < 0 or j > len(area[0])-1:
                    continue
                if area[i][j] == "0" or area[i][j] == "1":
                    spread(area, i, j)
                area[i][j] = "2"













            

    
            


