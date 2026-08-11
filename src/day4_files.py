import csv
import json
from pathlib import Path

# import class dari materi day 3
from day3_oop import Transaction, TransactionManager


class FileHandler:
    """Calss khusus untuk menangani Operasi I/O"""

    @staticmethod
    def load_transactions_from_json(file_path: Path) -> list[Transaction]:
        """Membaca file JSON dan mengubahknya menjadi list objek Transaction"""
        if not file_path.exists():
            print(f"Error: File {file_path} tidak ditemukan")
            return []

        with open(file_path, mode="r", encoding="utf-8") as file:
            raw_data = json.load(file)

        transaction = []

        for item in raw_data:
            tx = Transaction(
                tx_id=item["tx_id"],
                product=item["product"],
                category=item["category"],
                amount=float(item["amount"]),
                status=item["status"],
            )
            transaction.append(tx)

        return transaction

    @staticmethod
    def export_valid_transactions_to_csv(
        transactions: list[Transaction], output_path: Path
    ) -> None:
        """Mengeksport list objek Transaction yang valid ke dalam file csv"""
        if not transactions:
            print("Tidak ada data transaksi valid untuk dieksport")
            return

        fieldnames = ["tx_id", "product", "category", "amount", "status"]

        with open(output_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for tx in transactions:
                writer.writerow(
                    {
                        "tx_id": tx.tx_id,
                        "product": tx.product,
                        "category": tx.category,
                        "amount": tx.amount,
                        "status": tx.status,
                    }
                )
        print(f"Berhasil mengeksport {len(transactions)} data ke {output_path}")


if __name__ == "__main__":
    data_dir = Path("data")
    json_input_file = data_dir / "transactions.json"
    csv_output_file = data_dir / "valid_transaction.csv"

    print("Membaca data dari file JSON... ")
    loaded_txs = FileHandler.load_transactions_from_json(json_input_file)

    manager = TransactionManager()
    for tx in loaded_txs:
        manager.add_transaction(tx)

    valid_txs = manager.get_valid_transactions()

    print("\n==========================================")
    print("📊 LAPORAN PENGOLAHAN FILE DATA")
    print("==========================================")
    print(f"Total Transaksi Input : {len(loaded_txs)}")
    print(f"Total Transaksi Valid : {len(valid_txs)}")
    print(f"Total Pendapatan Valid: Rp {manager.calculate_total_revenue():,.2f}")
    print("==========================================\n")

    print("💾 Mengeksport hasil ke CSV...")
    FileHandler.export_valid_transactions_to_csv(valid_txs, csv_output_file)
