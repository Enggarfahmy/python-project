from pathlib import Path
import pandas as pd


class PandasDataProcessor:
    """Class untuk mengolah dan menganalisis data transaksi menggukanan library Pandas"""

    def __init__(self, file_path: Path) -> None:
        self.file_path = file_path
        self.df: pd.DataFrame = pd.DataFrame()

    def load_data(self) -> None:
        """Load data JSON jadi Data Frame Pandas"""
        if not self.file_path.exists():
            print(f"File {self.file_path} Not Found")
            return

        self.df = pd.read_json(self.file_path)
        print("Data loaded to Data Frame successfully")

    def filter_valid_transactions(self) -> pd.DataFrame:
        """FIletr data transaksi yang sukse dan arnya > 0"""
        valid_df = self.df[(self.df["status"] == "SUCCESS") & (self.df["amount"] > 0)]
        return valid_df

    def get_revenue_by_category(self, valid_df: pd.DataFrame) -> pd.Series:
        return valid_df.groupby("category")["amount"].sum()

    def export_to_csv(self, df_to_export: pd.DataFrame, output_path: Path) -> None:
        df_to_export.to_csv(output_path, index=False)
        print(f"Data exported to {output_path} Successfully")


if __name__ == "__main__":
    # Path file
    data_dir = Path("data")
    json_input = data_dir / "sales_day5.json"
    csv_output = data_dir / "pandas_valid_sales.csv"

    # Instalasi
    processor = PandasDataProcessor(json_input)
    processor.load_data()

    # Tampilkan Tampilan Data Asli (Pandas DataFrame)
    print("\n--- 3 Baris Pertama Raw Data ---")
    print(processor.df.head(3))

    # Filter Transaksi yang Valid
    valid_sales_df = processor.filter_valid_transactions()
    # Analisis & Ringkasan Data
    total_revenue = valid_sales_df["amount"].sum()
    revenue_by_cat = processor.get_revenue_by_category(valid_sales_df)

    print("\n==========================================")
    print("📊 LAPORAN ANALISIS DATA (PANDAS)")
    print("==========================================")
    print(f"Total Transaksi Masuk : {len(processor.df)}")
    print(f"Total Transaksi Valid : {len(valid_sales_df)}")
    print(f"Total Pendapatan Valid: Rp {total_revenue:,.2f}")
    print("\n--- 💰 Pendapatan Per Kategori ---")
    print(revenue_by_cat)
    print("==========================================\n")

    # 5. Eksport Hasil ke CSV
    processor.export_to_csv(valid_sales_df, csv_output)
