import logging
import json
import csv
from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)


@app.route('/pre-tick', methods=['POST'])
def evaluatePreTick():
    data = request.get_data()
    decoded_data = data.decode("utf-8")
    print(data.decode("utf-8"))
    data_list = decoded_data.split(",|\r\n\r\n")
    data_list = data_list[5:len(data_list)]
    print(data_list)
    logging.info("data sent for evaluation {}".format(data))
    # inputValue = data.get("input");
    logging.info("My result :{}".format(data))
    return data;


# def findNumWays(numPeople, numSeats, numSpaces):








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







            

    
            


