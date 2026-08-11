class Transaction:
    """Class untuk merepresentasikan 1 data transaksi penjualan"""

    def __init__(
        self,
        tx_id: int,
        product: str,
        category: str,
        amount: int,
        status: str = "SUCCESS",
    ) -> None:
        self.text_id = tx_id
        self.product = product
        self.category = category
        self.amount = amount
        self.status = status

    def is_valid(self) -> bool:
        """Method untuk cek apakah transaksi ini valid & sukses"""
        return self.status == "SUCCESS" and self.amount > 0

    def __repr__(self) -> str:
        """Mengatur tampilan saat objek Transaction di-print."""
        return f"Transaction(id={self.tx_id}, product='{self.product}', amount={self.amount})"


class TransactionManager:
    """Class untuk mengelola kumpulan transaksi (Pembersihan & Perhitungan)"""

    def __init__(self) -> None:
        # Menyimpan List Kosong
        self.transactions: list(Transaction) = []

    def add_transaction(self, tx: Transaction) -> None:
        self.transactions.append(tx)

    def get_valid_transactions(self) -> list[Transaction]:
        return [tx for tx in self.transactions if tx.is_valid()]

    def calculate_total_revenue(self) -> float:
        valid_txs = self.get_valid_transactions()
        return sum(tx.amount for tx in valid_txs)


if __name__ == "__main__":
    manager = TransactionManager()

    t1 = Transaction(1, "Laptop Pro", "elektronik", 15000000.0, "SUCCESS")
    t2 = Transaction(2, "Mouse Wireless", "elektronik", 250000.0, "SUCCESS")
    t3 = Transaction(3, "Kopi Arabika", "minuman", 50000.0, "FAILED")

    manager.add_transaction(t1)
    manager.add_transaction(t2)
    manager.add_transaction(t3)

    # 4. Tampilkan Hasil Rekapitulasi
    print("\n==========================================")
    print("📊 REKAPITULASI TRANSAKSI (BERBASIS OOP)")
    print("==========================================")

    valid_list = manager.get_valid_transactions()
    print(f"Total Transaksi Terdaftar : {len(manager.transactions)}")
    print(f"Total Transaksi Valid     : {len(valid_list)}")
    print(f"Daftar Transaksi Valid    : {valid_list}")
    print(f"Total Pendapatan Valid    : Rp {manager.calculate_total_revenue():,.2f}")

    print("==========================================\n")
