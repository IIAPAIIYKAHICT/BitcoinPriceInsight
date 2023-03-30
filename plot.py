import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt


BTC_Ticker = yf.Ticker("BTC-USD")

BTC_Data = yf.download("BTC-USD", period="1mo", interval="1d")
year_data = yf.download("BTC-USD", period="1y", interval="1d")

plt.rcParams["figure.figsize"] = [9.00, 3.50]
plt.rcParams["figure.autolayout"] = True

fig, (ax1, ax2) = plt.subplots(ncols=2)
fig.subplots_adjust(hspace=0.5, wspace=0.5)

month = sns.lineplot(data=BTC_Data, x="Date", y="Close", ax=ax1).set_title("Last month bitcoin prices")
plt.draw()
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=45)

year = sns.lineplot(data=year_data, x="Date", y="Close", ax=ax2).set_title("Last year bitcoin prices")
plt.draw()
ax2.set_xticklabels(ax1.get_xticklabels(), rotation=45)

plt.show()
