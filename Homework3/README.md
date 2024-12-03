# Python Applications: Shopping Cart & To-Do List

This repository contains two Python-based applications: a **Shopping Cart System** and a **To-Do List Manager**. Each program demonstrates object-oriented programming (OOP) principles by implementing classes and methods to manage data effectively.

---

## 1. Shopping Cart Application

### Features
- **Add Products:** Users can add products to the cart by specifying the name, price, and quantity.
- **Remove Products:** Users can remove products from the cart.
- **View Cart:** Displays all products in the cart, including their name, quantity, and price.
- **Calculate Total:** Automatically calculates the total cost of all items in the cart.

### Key Components
- **`Urun` Class:**
  - Represents a product with attributes:
    - `urun_adi` (product name)
    - `urun_fiyati` (price)
    - `urun_miktari` (quantity)

- **`Sepet` Class:**
  - Manages the cart's contents and provides methods for:
    - Adding products: `urun_ekle(ad, fiyat, miktar)`
    - Removing products: `urun_cikar(ad)`
    - Viewing the cart: `listele()`
    - Calculating total: `toplam()`

### Example Usage
```python
# Create a cart
sepet = Sepet()
# Add products
sepet.urun_ekle("Apple", 3.0, 5)
sepet.urun_ekle("Orange", 2.5, 10)
# View cart and calculate total
print(sepet.listele())
print("Total:", sepet.toplam())
# Remove a product
sepet.urun_cikar("Apple")
print(sepet.listele())
```

## 2. To-Do List Application

### Features
- **Add Tasks:** Users can add tasks to the list.
- **Mark Tasks as Completed:** Allows marking tasks as completed.
- **View Tasks:** Displays both completed and incomplete tasks separately.
- **Delete Completed Tasks:** Removes all tasks marked as completed.
- **File Persistence:** Saves tasks to a `.txt` file and reloads them when the program restarts.

### Key Components
- **`Görev` Class:**
  - Represents a task with attributes:
    - `görev_adi` (task name)
    - `tamamlanma_durumu` (completion status: `True` or `False`)

- **`GörevYönetici` Class:**
  - Manages the list of tasks with methods for:
    - Adding tasks: `görev_ekle(görev_adi)`
    - Marking tasks as completed: `görev_tamamlama(görev_adi)`
    - Viewing tasks: `görevleri_görüntüle()`
    - Deleting completed tasks: `tamamlananları_sil()`
    - Saving tasks to a file: `dosyaya_kaydet(dosya_adi)`
    - Loading tasks from a file: `dosyadan_yükle(dosya_adi)`

### Example Usage
```python
# Create a task manager
görev_yönetici = GörevYönetici()
# Add tasks
görev_yönetici.görev_ekle("Finish homework")
görev_yönetici.görev_ekle("Clean the house")
# Mark a task as completed
görev_yönetici.görev_tamamlama("Finish homework")
# View tasks
tamamlanmamış_görevler, tamamlanmış_görevler = görev_yönetici.görevleri_görüntüle()
print("Incomplete:", tamamlanmamış_görevler)
print("Completed:", tamamlanmış_görevler)
# Save tasks to a file
görev_yönetici.dosyaya_kaydet("tasks.txt")
# Load tasks from a file
yeni_görev_yönetici = GörevYönetici()
yeni_görev_yönetici.dosyadan_yükle("tasks.txt")
print(yeni_görev_yönetici.görevleri_görüntüle())
```

## Requirements
- Python 3.7 or later

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/shopping-cart-todo.git
   cd shopping-cart-todo
   ```

2. Run the Python files directly:
   ```bash
   python shopping_cart.py
   python todo_list.py
   ```

