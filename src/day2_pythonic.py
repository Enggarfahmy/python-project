from collections import defaultdict


def clean_transactions(data: list[dict]) -> list[dict]:
    """Mengambil hanya transaksi yang sukses menggunakan list comprehension."""
    successful_data = [tx for tx in data if tx["status"] == "SUCCESS"]
    return successful_data


def calculate_category_totals(data: list[dict]) -> dict[str, float]:
    totals = defaultdict(float)

    for tx in data:
        category = tx["category"]
        amount = tx["amount"]
        totals[category] += amount

    return dict(totals)


def print_report(category_totals: dict[str, float]) -> None:
    """Menampilkan laporan ke terminal menggunakan enumerate."""
    print("\n==========================================")
    print("📊 LAPORAN PENJUALAN PER KATEGORI")
    print("==========================================")

    items = list(category_totals.items())

    for nomor, (kategori, total_uang) in enumerate(items, start=1):
        print(f"{nomor}. Kategori: {kategori:<12} | Total: Rp. {total_uang:,.2f} ")

    print("==========================================\n")


# RAW DATA
raw_data_sales = [
    {
        "id": 1,
        "product": "Laptop Pro",
        "category": "elektronik",
        "amount": 15000000,
        "status": "SUCCESS",
    },
    {
        "id": 2,
        "product": "Mouse Wireless",
        "category": "elektronik",
        "amount": 250000,
        "status": "SUCCESS",
    },
    {
        "id": 3,
        "product": "Kopi Arabika",
        "category": "minuman",
        "amount": 50000,
        "status": "FAILED",
    },
    {
        "id": 4,
        "product": "Laptop Pro",
        "category": "elektronik",
        "amount": 15000000,
        "status": "SUCCESS",
    },
    {
        "id": 5,
        "product": "Kaos Polos",
        "category": "pakaian",
        "amount": 100000,
        "status": "SUCCESS",
    },
]


if __name__ == "__main__":
    valid_data = clean_transactions(raw_data_sales)
    # print(valid_data)

    totals = calculate_category_totals(valid_data)

    print_report(totals)
