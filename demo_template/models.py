
def recieve(query):
    data = []
    for rank in range(7):
        rank += 1
        data.append(
                {
                    "rank" : str(rank),
                    "title" : "こんにちは",
                    "data" : "ちは",
                    "score" : 10,
                    }
                )
    return data
