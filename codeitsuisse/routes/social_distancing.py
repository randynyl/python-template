import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)


@app.route('/social_distancing', methods=['POST'])
def evaluateSocialDistancing():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    # inputValue = data.get("input");
    result = {"answers": {}}
    for key, value in data["tests"].items():
        result["answers"][key] = findNumWays(value["people"], value["seats"], value["spaces"])

    logging.info("My result :{}".format(result))
    return jsonify(result);


def findNumWays(numPeople, numSeats, numSpaces):
    numSeatsFor1 = numSeats
    placeHolderPeople = numPeople
    while placeHolderPeople != 1:
        numSeatsFor1 -= numSpaces + 1
        if numSeatsFor1 < 0:
            return 0
        placeHolderPeople -= 1

    numWays = 0
    for i in range(1, numSeatsFor1 + 1):
        numerator = 1
        denominator = 1
        for j in range(numPeople-1):
            numerator *= i + j
            denominator *= numPeople - j - 1
        numWays += numerator // denominator

    return numWays







# seats = 6
# seatarray = [0]*seats
# ppl = 3
# space = 1
# combilist = []
# curcombi = []
# pplcount = 0
# for w in range(0,seats):
#     for s in range(w, seats, space+1):
#         if pplcount <= ppl:
#             seatarray[s] = 1
#         else:
#             break
#         pplcount += 1
#     if seatarray.count(1) == ppl:
#         combilist.append(seatarray)
#     seatarray = [0]*seats
#     pplcount = 0
# print(len(combilist))
#
# spare = seats - ppl
# pplarray = [1]*ppl







            

    
            


