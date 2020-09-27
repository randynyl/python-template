import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)


@app.route('/contact_trace', methods=['POST'])
def evaluateContactTrace():
    data = request.get_json(force = True)
    logging.info("data sent for evaluation {}".format(data))
    print(data)
    result = [""]
    primary_cluster = {}
    # inputValue = data.get("input");
    data["cluster"].append(data["origin"])
    list_of_names = [data["infected"]]
    while list_of_names[-1] != data["origin"]:
        infectedGenome = list_of_names[-1]["genome"]
        numDifferences = 10
        for clusterEntry in data["cluster"]:
            clusterDifferences = getNumberDifferences(infectedGenome, clusterEntry["genome"])
            if clusterDifferences < numDifferences:
                numDifferences = clusterDifferences
                primary_cluster = clusterEntry

        list_of_names.append(primary_cluster)
        data["cluster"].remove(primary_cluster)

    for i in range(len(list_of_names)):
        result[0] += list_of_names[i]["name"]
        if i == len(list_of_names) - 1:
            break
        if isNonSilentMutation(list_of_names[i]["genome"], list_of_names[i + 1]["genome"]):
            result[0] += ("*")
        result[0] += (" -> ")

    print(result)
    return jsonify(result);


def getNumberDifferences(infected_genome, other_genome):
    numberOfDifferences = 0
    for i in range(len(infected_genome)):
        if infected_genome[i] != other_genome[i]:
            numberOfDifferences += 1
    return numberOfDifferences


def isNonSilentMutation(infected_genome, other_genome):
    numberFirstDifferences = 0
    for i in range(len(infected_genome)):
        if infected_genome[i] != other_genome[i]:
            if i % 4 == 0:
                numberFirstDifferences += 1

    if numberFirstDifferences >= 2:
        return True
    else:
        return False
