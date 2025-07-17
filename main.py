from lob.limitorderbook import LimitOrderBook

if __name__ == "__main__":
    lob = LimitOrderBook(n=11)

    lob.set_order_book([-9, -8, -5, -3, 0, 2, 4, 4, 5, 6, 7])
    print("Ask price:", lob.ask_price())
    print("Bid price:", lob.bid_price())
    print("Mid price and spread:", lob.mid_price_and_spread())
    print("Q^B (buy depth):", lob.Q_B())  # This is depth at each distance from the ask
    print("Q^A (sell depth):", lob.Q_A())  # This is depth at each distance from the bid

    lob.plot_ascii_orderbook()
