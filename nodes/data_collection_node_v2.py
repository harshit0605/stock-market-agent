def data_collection_node(state):
    print("...................In data_collection_node node..................")
    stock_price = state["stock_price"]
    news_sentiment = state["news_sentiment"]
    indicators_data = state["indicators_data"]
    print(state.keys())
    rule_results = state["rule_results"]


    return {
        "collected_data" : {
            "stock_price" : stock_price,
            "news_sentiment" : news_sentiment,
            "indicators_data" : indicators_data,
            
        }
    }