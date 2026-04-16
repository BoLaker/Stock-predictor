import model as m
import preprocessing as p
import Data_manager as d
import evaluate as e

model = m.linearRegressionGD()

d.save_to_disk(d.get_stock_data("INVE-B.ST", "2020-01-01", "2026-04-01"), "data.csv")
df = d.load_from_disk("data.csv")

x,y = p.create_matrix_target(df, window_size=5)

split = int(len(x)*0.8)

x_train_raw,x_test_raw= x[:split],x[split:]
y_train, y_test = y[:split], y[split:]

x_train,x_test, mean, std = p.standardize_data(x_train_raw,x_test_raw)


model.fit(x_train,y_train)
predictions = model.predict(x_test)


e.plot_data([model.cost_history],["Training Loss"], "Modellens inlärning", "Epochs", "MSE Cost" )
e.plot_data(
    [y_test, predictions], 
    ["Verklighet", "Modellens Gissning"], 
    "Investor AB - Prediktion vs Verklighet", 
    "Dagar", 
    "Pris (Skalat)"
)