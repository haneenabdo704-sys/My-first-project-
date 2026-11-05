products = [
    {"name": "Laptop Dell", "price": 25000},
    {"name": "Wireless Mouse", "price": 450},
    {"name": "Mechanical Keyboard", "price": 1200},
    {"name": "Gaming Monitor", "price": 8500},
    {"name": "USB Hub", "price": 250},
]


def quick_sort_products(arr):
  if len(arr) <= 1:
    return arr

  pivot = arr[len(arr) // 2]["price"]

  left = [item for item in arr if item["price"] < pivot]
  middle = [item for item in arr if item["price"] == pivot]
  right = [item for item in arr if item["price"] > pivot]

  return quick_sort_products(left) + middle + quick_sort_products(right)


sorted_products = quick_sort_products(products)

for p in sorted_products:
  print(f"Product: {p['name']} | Price: {p['price']}")
