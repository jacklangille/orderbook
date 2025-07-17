import numpy as np


class LimitOrderBook:
    def __init__(self, n: int):
        self.n = n
        self.X = np.zeros(n + 1, dtype=int)

    def set_order_book(self, X_values):
        """Set the order book state X(t)"""
        assert len(X_values) == self.n
        self.X[1:] = X_values

    def ask_price(self):
        """Compute p_A(t)

        This is the 'far touch' — the lowest price at which someone is willing to sell.
        It's the best ask price.
        """
        # The far touch refers to the best ask (lowest price someone is willing to sell at)
        ask_prices = [p for p in range(1, self.n + 1) if self.X[p] > 0]
        return min(ask_prices) if ask_prices else self.n + 1

    def bid_price(self):
        """Compute p_B(t)

        This is the 'near touch' — the highest price at which someone is willing to buy.
        It's the best bid price.
        """
        # The near touch refers to the best bid (highest price someone is willing to buy at)
        bid_prices = [p for p in range(1, self.n + 1) if self.X[p] < 0]
        return max(bid_prices) if bid_prices else 0

    def mid_price_and_spread(self):
        pA = self.ask_price()
        pB = self.bid_price()
        pM = (pA + pB) / 2
        s = pA - pB
        return pM, s

    def Q_B(self):
        """Compute Q^B_i(t): buy depth at distance i from ask"""
        pA = self.ask_price()
        QB = np.zeros(self.n)
        for i in range(1, min(pA, self.n)):
            QB[i] = self.X[pA - i] if 1 <= pA - i <= self.n else 0
        return QB

    def Q_A(self):
        """Compute Q^A_i(t): sell depth at distance i from bid"""
        pB = self.bid_price()
        QA = np.zeros(self.n)
        for i in range(1, self.n - pB):
            if 1 <= pB + i <= self.n:
                QA[i] = self.X[pB + i]
        return QA

    def plot_ascii_orderbook(self):
        print("ORDER BOOK\n----------")
        print("TOP OF BOOK (HIGH PRICE)")
        for p in range(self.n, 0, -1):
            volume = self.X[p]
            if volume > 0:
                bar = "<" * volume
            elif volume < 0:
                bar = ">" * abs(volume)
            else:
                bar = ""
            print(f"{p:2d}: {bar}")
        print("BOTTOM OF BOOK (LOW PRICE)")
