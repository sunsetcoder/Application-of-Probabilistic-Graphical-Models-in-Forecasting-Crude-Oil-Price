import pandas as pd

import eia

import utils
import api_keys

if __name__ == "__main__":
    eia_api = eia.API(api_keys.eia)
    time_series_label = "TOTAL.COEXPUS.M"  # (C)rude (O)il (E)xport - (M)onthly
    eia_data = pd.DataFrame(eia_api.data_by_series(series=time_series_label))
    utils.clean_EIA_series(eia_data, column_label=time_series_label)
    utils.plot_time_series(
        eia_data,
        x_label="Date",
        x_unit="Year",
        y_label="U.S Exports of Crude Oil (Monthly)",
        y_unit="Thousand Barrels Per Day",
        column_name=time_series_label,
    )

    pass
