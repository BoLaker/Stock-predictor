import yfinance as yf
import matplotlib.pyplot as plt

data = yf.download("INVE-B.ST", start="2020-01-01")

plt.plot( data.index,data["Close"]["INVE-B.ST"])


plt.title("Stock price since 2020-01-01")
plt.xlabel("Date")
plt.ylabel("Close price")
plt.grid(True)

plt.show()

