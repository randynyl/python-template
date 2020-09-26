import logging
import json

from flask import request, jsonify;

from codeitsuisse import app;

logger = logging.getLogger(__name__)


@app.route('/olympiad-of-babylon', methods=['POST'])
def evaluateOlympiad():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    # inputValue = data.get("input");
    result = {"optimalNumberOfBooks": findOptimalNumOfBooks(data["books"], data["days"])}
    logging.info("My result :{}".format(result))
    return jsonify(result);


def findOptimalNumOfBooks(book_list, day_list):
    total_time = 0
    for time in day_list:
        total_time += time
    max_books = 0
    book_time = 0
    book_list.sort()
    for i in range(len(book_list)):
        book_time += book_list[i]
        max_books += 1
        if book_time >= total_time:
            break
    new_book_list = book_list[0:max_books]
    all_books_read = []
    for time in day_list:
        leftover_time = time
        for i in range(len(new_book_list)):
            day_read_time = new_book_list[i]
            day_books_read = [new_book_list[i]]
            for j in range(len(new_book_list)-1, i-1):
                if day_read_time + new_book_list[j] > leftover_time:
                    continue
                day_read_time += new_book_list[j]
                day_books_read.append(new_book_list[j])
            if time - day_read_time < leftover_time:
                all_books_read.extend(day_books_read)
                leftover_time = time - day_read_time
            else:
                continue
        for book in all_books_read:
            if book in new_book_list:
                new_book_list.remove(book)

    return max_books - len(new_book_list)

















            

    
            


