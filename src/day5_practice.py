from pathlib import Path

import pandas as pd

file_path = Path("data") / "bookstore_sales.json"
df = pd.read_json(file_path)

print("=== 📌 PREVIEW DATA ASLI ===")
print(df.head())
print("\n" + "=" * 40 + "\n")

df["total_price"] = df["price"] * df["qty"]

paid_df = df[df["payment_status"] == "PAID"]

print("=== 📌 PREVIEW DATA DENGAN KOLOM BARU (total_price) ===")
print(df.head())
print(paid_df)

print("Analisis")
print("Total Pendapatan dari Transaksi yang Dibayar: Rp", paid_df["total_price"].sum())
print("Pendapatan per Kategori Produk")
print(paid_df.groupby("category")["total_price"].sum())
print("Pendapatan per Kota pemesanan")
print(paid_df.groupby("customer_city")["total_price"].sum())

# Export data ke CSV
output_path = Path("data") / "paid_sales.csv"
paid_df.to_csv(output_path, index=False)
print(f"Data berhasil diekspor ke {output_path}")
