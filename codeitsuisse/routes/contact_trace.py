import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)


@app.route('/contact_trace', methods=['POST'])
def evaluateContactTrace():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    result = []
    numDifferences = 10
    primary_cluster = {}
    infectedName = data["infected"]["name"]
    infectedGenome = data["infected"]["genome"]
    originName = data["origin"]["name"]
    originGenome = data["origin"]["genome"]
    # inputValue = data.get("input");
    for clusterEntry in range(len(data["cluster"])):
        clusterDifferences = getNumberDifferences(infectedGenome, clusterEntry["genomee"])
        if clusterDifferences < numDifferences:
            primary_cluster = clusterEntry



    if getNumberDifferences(infectedGenome, originGenome) < numDifferences:
        if isNonSilentMutation(infectedGenome, originGenome):
            result.append(infectedName + "* -> " + originName)
        else:
            result.append(infectedName + " -> " + originName)


    else:
        if isNonSilentMutation(infectedGenome, clusterEntry["genome"]):
            result.append(infectedName + "* -> " + primary_cluster["name"])
        else:
            result.append(infectedName + " -> " + primary_cluster["name"])

        if getNumberDifferences(primary_cluster["genome"], originGenome) == 0:
            result.append(result[0].replace(primary_cluster, originGenome))
        else:
            if isNonSilentMutation(primary_cluster["genome"], originGenome):
                result[0] += ("* -> " + originName)
            else:
                result[0] += (" -> " + originName)

    return result;


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



