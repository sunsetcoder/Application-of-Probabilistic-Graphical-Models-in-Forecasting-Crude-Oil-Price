"""Regime Detection"""
import utils

df_pickled_path = "./data/data.pkl"
data = utils.load_df_pickled(df_pickled_path)

train_data, valid_data, test_data = utils.split_df(
    data, train_set_ratio=0.8, test_set_ratio=0.1, valid_set_ratio=0.1
)

column_label = 'WTISPLC' # Spot Crude Oil Price: West Texas Intermediate
price = train_data[column_label]

if __name__ == "__main__":
    pass
