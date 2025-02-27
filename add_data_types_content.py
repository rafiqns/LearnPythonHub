
from app import app, db
from models import Chapter, SubChapter, Content

# Pastikan aplikasi berjalan dalam konteks aplikasi Flask
with app.app_context():
    # Periksa apakah Chapter dengan id=2 ada
    chapter = Chapter.query.get(2)
    
    if not chapter:
        print("Chapter dengan id=2 tidak ditemukan. Membuat chapter baru...")
        chapter = Chapter(
            id=2,
            title="Python Data Types",
            description="Belajar tentang tipe data dalam Python, seperti string, integer, float, list, tuple, dictionary, dan boolean.",
            order=2,
            is_pro=False
        )
        db.session.add(chapter)
        db.session.commit()
        print(f"Chapter baru dibuat dengan id={chapter.id}")
    else:
        print(f"Menggunakan chapter yang sudah ada: {chapter.title}")
    
    # Hapus subchapter lama jika ada (untuk memastikan tidak ada duplikat)
    existing_subchapters = SubChapter.query.filter_by(chapter_id=chapter.id).all()
    for sub in existing_subchapters:
        print(f"Menghapus subchapter lama: {sub.title}")
        Content.query.filter_by(subchapter_id=sub.id).delete()
        db.session.delete(sub)
    db.session.commit()
    
    # Tambahkan subchapter baru
    subchapters_data = [
        {
            "title": "Pengenalan Tipe Data",
            "order": 1,
            "contents": [
                {
                    "content_type": "text",
                    "content": """
                    <h3>Pengenalan Tipe Data di Python</h3>
                    <p>Python memiliki beberapa tipe data bawaan yang dapat Anda gunakan dalam pemrograman sehari-hari:</p>
                    <ul>
                        <li><strong>Numbers</strong>: Integer, Float, Complex Number</li>
                        <li><strong>String</strong>: Teks atau karakter</li>
                        <li><strong>Boolean</strong>: True atau False</li>
                        <li><strong>Sequence Types</strong>: List, Tuple, Range</li>
                        <li><strong>Mapping Type</strong>: Dictionary</li>
                        <li><strong>Set Types</strong>: Set, Frozenset</li>
                        <li><strong>None Type</strong>: Mewakili nilai kosong</li>
                    </ul>
                    <p>Dalam subchapter berikutnya, kita akan mempelajari masing-masing tipe data secara lebih detail.</p>
                    """,
                    "order": 1
                }
            ]
        },
        {
            "title": "Tipe Data Numerik",
            "order": 2,
            "contents": [
                {
                    "content_type": "text",
                    "content": """
                    <h3>Tipe Data Numerik di Python</h3>
                    <p>Python mendukung beberapa tipe data numerik:</p>
                    
                    <h4>1. Integer (int)</h4>
                    <p>Integer adalah bilangan bulat tanpa desimal. Contoh: 10, -5, 0</p>
                    <pre><code>
x = 10
y = -5
z = 0
print(type(x))  # Output: &lt;class 'int'&gt;
                    </code></pre>
                    
                    <h4>2. Float</h4>
                    <p>Float adalah bilangan dengan nilai desimal. Contoh: 10.5, -3.14, 0.0</p>
                    <pre><code>
a = 10.5
b = -3.14
c = 0.0
print(type(a))  # Output: &lt;class 'float'&gt;
                    </code></pre>
                    
                    <h4>3. Complex</h4>
                    <p>Complex number terdiri dari bagian real dan imaginer. Contoh: 2+3j</p>
                    <pre><code>
d = 2 + 3j
print(type(d))  # Output: &lt;class 'complex'&gt;
print(d.real)   # Output: 2.0
print(d.imag)   # Output: 3.0
                    </code></pre>
                    
                    <h4>Operasi Numerik</h4>
                    <p>Python mendukung operasi aritmatika dasar:</p>
                    <pre><code>
# Penjumlahan
print(10 + 5)      # Output: 15

# Pengurangan
print(10 - 5)      # Output: 5

# Perkalian
print(10 * 5)      # Output: 50

# Pembagian (hasilnya selalu float)
print(10 / 5)      # Output: 2.0

# Pembagian dengan hasil integer
print(10 // 3)     # Output: 3

# Modulo (sisa pembagian)
print(10 % 3)      # Output: 1

# Pangkat
print(2 ** 3)      # Output: 8
                    </code></pre>
                    """,
                    "order": 1
                }
            ]
        },
        {
            "title": "String",
            "order": 3,
            "contents": [
                {
                    "content_type": "text",
                    "content": """
                    <h3>Tipe Data String di Python</h3>
                    <p>String adalah urutan karakter yang dikelilingi oleh tanda kutip (tunggal, ganda, atau tiga tanda kutip).</p>
                    
                    <h4>Mendefinisikan String</h4>
                    <pre><code>
s1 = 'Hello'               # Kutip tunggal
s2 = "World"               # Kutip ganda
s3 = '''This is a          # Tiga kutip (bisa multi-baris)
multiline string'''
                    </code></pre>
                    
                    <h4>Akses Karakter dalam String</h4>
                    <p>String dapat diakses dengan menggunakan indexing (dimulai dari 0):</p>
                    <pre><code>
s = "Python"
print(s[0])       # Output: P
print(s[1])       # Output: y
print(s[-1])      # Output: n (indeks negatif dimulai dari belakang)
                    </code></pre>
                    
                    <h4>Slicing String</h4>
                    <p>Anda dapat mengambil sebagian string dengan slicing:</p>
                    <pre><code>
s = "Python Programming"
print(s[0:6])     # Output: Python
print(s[7:])      # Output: Programming
print(s[:6])      # Output: Python
print(s[::2])     # Output: Pto rgamn (setiap karakter kedua)
                    </code></pre>
                    
                    <h4>Metode String</h4>
                    <p>Python menyediakan banyak metode built-in untuk memanipulasi string:</p>
                    <pre><code>
s = "python programming"

# Mengubah ke huruf besar/kecil
print(s.upper())          # PYTHON PROGRAMMING
print(s.lower())          # python programming
print(s.capitalize())     # Python programming
print(s.title())          # Python Programming

# Mencari dan mengganti
print(s.find("pro"))      # 7 (indeks dimana "pro" ditemukan)
print(s.replace("python", "Java"))  # Java programming

# Pemisahan dan penggabungan
words = s.split()         # ['python', 'programming']
print(" ".join(words))    # python programming

# Pengecekan
print("python" in s)      # True
print(s.startswith("py")) # True
print(s.endswith("ing"))  # True
print(s.isalpha())        # False (karena ada spasi)
print("Python".isalpha()) # True
print("123".isdigit())    # True
                    </code></pre>
                    
                    <h4>Formatted Strings</h4>
                    <p>Python menyediakan beberapa cara untuk memformat string:</p>
                    <pre><code>
name = "Alice"
age = 25

# Menggunakan format()
print("Nama: {}, Umur: {}".format(name, age))

# f-strings (Python 3.6+)
print(f"Nama: {name}, Umur: {age}")

# Formatting angka
pi = 3.14159
print(f"Nilai pi hingga 2 desimal: {pi:.2f}")  # 3.14
                    </code></pre>
                    """,
                    "order": 1
                }
            ]
        },
        {
            "title": "List dan Tuple",
            "order": 4,
            "contents": [
                {
                    "content_type": "text",
                    "content": """
                    <h3>Tipe Data List dan Tuple di Python</h3>
                    
                    <h4>List</h4>
                    <p>List adalah koleksi elemen yang terurut dan dapat diubah (mutable). List dibuat dengan kurung siku [].</p>
                    
                    <h5>Membuat List</h5>
                    <pre><code>
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
empty_list = []
                    </code></pre>
                    
                    <h5>Akses Element List</h5>
                    <pre><code>
fruits = ["apple", "banana", "cherry"]
print(fruits[0])       # apple
print(fruits[-1])      # cherry
print(fruits[1:3])     # ['banana', 'cherry']
                    </code></pre>
                    
                    <h5>Memodifikasi List</h5>
                    <pre><code>
fruits = ["apple", "banana", "cherry"]

# Mengubah elemen
fruits[0] = "orange"
print(fruits)          # ['orange', 'banana', 'cherry']

# Menambah elemen
fruits.append("kiwi")
print(fruits)          # ['orange', 'banana', 'cherry', 'kiwi']

fruits.insert(1, "mango")
print(fruits)          # ['orange', 'mango', 'banana', 'cherry', 'kiwi']

# Menghapus elemen
fruits.remove("banana")
print(fruits)          # ['orange', 'mango', 'cherry', 'kiwi']

popped = fruits.pop()  # Menghapus dan mengembalikan elemen terakhir
print(popped)          # kiwi
print(fruits)          # ['orange', 'mango', 'cherry']

del fruits[0]          # Menghapus elemen dengan indeks
print(fruits)          # ['mango', 'cherry']
                    </code></pre>
                    
                    <h5>Metode List</h5>
                    <pre><code>
numbers = [3, 1, 4, 1, 5, 9, 2]

# Mengurutkan
numbers.sort()
print(numbers)         # [1, 1, 2, 3, 4, 5, 9]

# Membalik
numbers.reverse()
print(numbers)         # [9, 5, 4, 3, 2, 1, 1]

# Menghitung jumlah elemen
print(numbers.count(1))  # 2

# Mencari indeks
print(numbers.index(5))  # 1

# Menggabungkan list
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)              # [1, 2, 3, 4, 5, 6]
                    </code></pre>
                    
                    <h4>Tuple</h4>
                    <p>Tuple adalah koleksi elemen yang terurut tetapi tidak dapat diubah (immutable). Tuple dibuat dengan kurung bulat ().</p>
                    
                    <h5>Membuat Tuple</h5>
                    <pre><code>
fruits = ("apple", "banana", "cherry")
numbers = (1, 2, 3, 4, 5)
mixed = (1, "hello", 3.14, True)
single_item = (1,)    # Perhatikan koma untuk tuple dengan satu elemen
empty_tuple = ()
                    </code></pre>
                    
                    <h5>Akses Element Tuple</h5>
                    <pre><code>
fruits = ("apple", "banana", "cherry")
print(fruits[0])       # apple
print(fruits[-1])      # cherry
print(fruits[1:3])     # ('banana', 'cherry')
                    </code></pre>
                    
                    <h5>Tuple Tidak Dapat Diubah</h5>
                    <pre><code>
fruits = ("apple", "banana", "cherry")
# fruits[0] = "orange"  # Ini akan menghasilkan error TypeError
                    </code></pre>
                    
                    <h5>Metode Tuple</h5>
                    <pre><code>
numbers = (3, 1, 4, 1, 5, 9, 2)

# Menghitung jumlah elemen
print(numbers.count(1))  # 2

# Mencari indeks
print(numbers.index(5))  # 4
                    </code></pre>
                    
                    <h5>Tuple vs List</h5>
                    <p>Kapan sebaiknya menggunakan tuple dibandingkan list:</p>
                    <ul>
                        <li>Tuple digunakan untuk kumpulan data yang tidak perlu diubah (immutable)</li>
                        <li>Tuple memiliki performa lebih cepat daripada list</li>
                        <li>Tuple dapat digunakan sebagai key dalam dictionary, list tidak bisa</li>
                        <li>Tuple lebih aman dari perubahan yang tidak diinginkan</li>
                    </ul>
                    """,
                    "order": 1
                }
            ]
        },
        {
            "title": "Dictionary dan Set",
            "order": 5,
            "contents": [
                {
                    "content_type": "text",
                    "content": """
                    <h3>Tipe Data Dictionary dan Set di Python</h3>
                    
                    <h4>Dictionary</h4>
                    <p>Dictionary adalah koleksi pasangan key-value yang tidak berurutan, dapat diubah, dan tidak mengizinkan duplikat. Dictionary dibuat dengan kurung kurawal {} dan memiliki key dan value yang dipisahkan oleh titik dua (:).</p>
                    
                    <h5>Membuat Dictionary</h5>
                    <pre><code>
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

empty_dict = {}
another_dict = dict(name="Alice", age=25, city="Boston")
                    </code></pre>
                    
                    <h5>Akses Nilai dalam Dictionary</h5>
                    <pre><code>
person = {"name": "John", "age": 30, "city": "New York"}

print(person["name"])       # John
print(person.get("age"))    # 30
print(person.get("email", "Not found"))  # Not found (default value jika key tidak ada)
                    </code></pre>
                    
                    <h5>Memodifikasi Dictionary</h5>
                    <pre><code>
person = {"name": "John", "age": 30, "city": "New York"}

# Mengubah nilai
person["age"] = 31
print(person)              # {'name': 'John', 'age': 31, 'city': 'New York'}

# Menambah item baru
person["email"] = "john@example.com"
print(person)              # {'name': 'John', 'age': 31, 'city': 'New York', 'email': 'john@example.com'}

# Menghapus item
removed = person.pop("city")
print(removed)             # New York
print(person)              # {'name': 'John', 'age': 31, 'email': 'john@example.com'}

del person["age"]
print(person)              # {'name': 'John', 'email': 'john@example.com'}
                    </code></pre>
                    
                    <h5>Metode Dictionary</h5>
                    <pre><code>
person = {"name": "John", "age": 30, "city": "New York"}

# Mendapatkan semua key
print(person.keys())        # dict_keys(['name', 'age', 'city'])

# Mendapatkan semua value
print(person.values())      # dict_values(['John', 30, 'New York'])

# Mendapatkan semua pasangan key-value
print(person.items())       # dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])

# Update dictionary
person.update({"age": 32, "job": "Developer"})
print(person)               # {'name': 'John', 'age': 32, 'city': 'New York', 'job': 'Developer'}

# Clear dictionary
person.clear()
print(person)               # {}
                    </code></pre>
                    
                    <h5>Iterasi pada Dictionary</h5>
                    <pre><code>
person = {"name": "John", "age": 30, "city": "New York"}

# Iterasi pada key
for key in person:
    print(key, ":", person[key])

# Iterasi pada key-value pairs
for key, value in person.items():
    print(key, ":", value)
                    </code></pre>
                    
                    <h4>Set</h4>
                    <p>Set adalah koleksi elemen yang tidak berurutan, tidak memiliki indeks, dan tidak mengizinkan duplikat. Set dibuat dengan kurung kurawal {} atau fungsi set().</p>
                    
                    <h5>Membuat Set</h5>
                    <pre><code>
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}
mixed_set = {1, "hello", 3.14, True}
empty_set = set()  # Tidak bisa menggunakan {} karena itu akan menjadi dictionary kosong
                    </code></pre>
                    
                    <h5>Karakteristik Set</h5>
                    <pre><code>
# Set tidak mengizinkan duplikat
numbers = {1, 2, 2, 3, 3, 4}
print(numbers)       # {1, 2, 3, 4}

# Set tidak memiliki urutan tertentu
print({3, 1, 4, 2})  # Mungkin tampil sebagai {1, 2, 3, 4} atau urutan lain
                    </code></pre>
                    
                    <h5>Operasi pada Set</h5>
                    <pre><code>
fruits = {"apple", "banana", "cherry"}

# Menambah item
fruits.add("orange")
print(fruits)  # {'orange', 'banana', 'apple', 'cherry'}

# Menambah beberapa item
fruits.update(["mango", "grapes"])
print(fruits)  # {'orange', 'mango', 'cherry', 'banana', 'grapes', 'apple'}

# Menghapus item
fruits.remove("banana")  # Akan error jika item tidak ada
fruits.discard("kiwi")   # Tidak akan error jika item tidak ada
print(fruits)  # {'orange', 'mango', 'cherry', 'grapes', 'apple'}

# Menghapus dan mengembalikan item
popped = fruits.pop()  # Menghapus dan mengembalikan item acak
print(popped)          # Item yang dihapus (acak)
print(fruits)          # Set setelah pop
                    </code></pre>
                    
                    <h5>Operasi Matematika pada Set</h5>
                    <pre><code>
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Union (Gabungan)
print(A | B)        # {1, 2, 3, 4, 5, 6, 7, 8}
print(A.union(B))   # {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection (Irisan)
print(A & B)        # {4, 5}
print(A.intersection(B))  # {4, 5}

# Difference (Selisih)
print(A - B)        # {1, 2, 3}
print(A.difference(B))  # {1, 2, 3}

# Symmetric Difference (Selisih Simetris)
print(A ^ B)        # {1, 2, 3, 6, 7, 8}
print(A.symmetric_difference(B))  # {1, 2, 3, 6, 7, 8}

# Subset (Himpunan Bagian)
C = {1, 2}
print(C.issubset(A))  # True
print(C <= A)         # True

# Superset (Himpunan yang Memuat)
print(A.issuperset(C))  # True
print(A >= C)           # True
                    </code></pre>
                    """,
                    "order": 1
                }
            ]
        },
        {
            "title": "Boolean dan None",
            "order": 6,
            "contents": [
                {
                    "content_type": "text",
                    "content": """
                    <h3>Tipe Data Boolean dan None di Python</h3>
                    
                    <h4>Boolean</h4>
                    <p>Boolean adalah tipe data yang hanya memiliki dua nilai: True dan False. Boolean sering digunakan dalam kondisional dan ekspresi logis.</p>
                    
                    <h5>Nilai Boolean</h5>
                    <pre><code>
x = True
y = False

print(type(x))      # <class 'bool'>
                    </code></pre>
                    
                    <h5>Operasi Perbandingan</h5>
                    <p>Operasi perbandingan menghasilkan nilai boolean:</p>
                    <pre><code>
x = 5
y = 10

print(x == y)      # False (Apakah x sama dengan y?)
print(x != y)      # True (Apakah x tidak sama dengan y?)
print(x < y)       # True (Apakah x kurang dari y?)
print(x > y)       # False (Apakah x lebih dari y?)
print(x <= y)      # True (Apakah x kurang dari atau sama dengan y?)
print(x >= y)      # False (Apakah x lebih dari atau sama dengan y?)
                    </code></pre>
                    
                    <h5>Operasi Logika</h5>
                    <p>Python mendukung operasi logika dasar:</p>
                    <pre><code>
x = True
y = False

print(x and y)     # False (True hanya jika keduanya True)
print(x or y)      # True (True jika salah satu atau keduanya True)
print(not x)       # False (Membalikkan nilai boolean)
                    </code></pre>
                    
                    <h5>Penggunaan dalam Kondisional</h5>
                    <pre><code>
age = 20

if age >= 18:
    print("Dewasa")  # Kondisi ini akan dijalankan karena age >= 18 adalah True
else:
    print("Belum dewasa")
                    </code></pre>
                    
                    <h5>Nilai Truthy dan Falsy</h5>
                    <p>Di Python, hampir semua nilai dievaluasi sebagai True kecuali yang berikut:</p>
                    <ul>
                        <li>False</li>
                        <li>None</li>
                        <li>Integer 0 (0)</li>
                        <li>Float 0 (0.0)</li>
                        <li>String kosong ("")</li>
                        <li>List kosong ([])</li>
                        <li>Tuple kosong (())</li>
                        <li>Dictionary kosong ({})</li>
                        <li>Set kosong (set())</li>
                    </ul>
                    
                    <pre><code>
# Nilai yang dievaluasi sebagai False:
print(bool(False))   # False
print(bool(None))    # False
print(bool(0))       # False
print(bool(""))      # False
print(bool([]))      # False
print(bool({}))      # False

# Nilai yang dievaluasi sebagai True:
print(bool(True))    # True
print(bool(1))       # True
print(bool(-1))      # True
print(bool("text"))  # True
print(bool([0]))     # True
print(bool({"key": "value"}))  # True
                    </code></pre>
                    
                    <h4>None Type</h4>
                    <p>None adalah nilai khusus yang mewakili ketiadaan nilai atau objek kosong. None sering digunakan untuk menginisialisasi variabel.</p>
                    
                    <h5>Menggunakan None</h5>
                    <pre><code>
x = None
print(type(x))      # <class 'NoneType'>
print(x)            # None
                    </code></pre>
                    
                    <h5>Memeriksa None</h5>
                    <p>Gunakan operator is untuk memeriksa apakah suatu variabel adalah None:</p>
                    <pre><code>
x = None

# Cara yang benar untuk memeriksa None
if x is None:
    print("x adalah None")

# Cara yang benar untuk memeriksa bukan None
if x is not None:
    print("x bukan None")

# Jangan gunakan == untuk memeriksa None
# if x == None:  # Tidak disarankan
#     print("x adalah None")
                    </code></pre>
                    
                    <h5>Penggunaan None</h5>
                    <p>None sering digunakan dalam skenario berikut:</p>
                    <ol>
                        <li>Nilai default untuk parameter fungsi</li>
                        <li>Nilai pengembalian fungsi ketika tidak ada nilai yang perlu dikembalikan</li>
                        <li>Menandai variabel yang belum diinisialisasi dengan nilai tertentu</li>
                    </ol>
                    
                    <pre><code>
# None sebagai nilai default parameter
def greet(name=None):
    if name is None:
        name = "Guest"
    return f"Hello, {name}!"

print(greet())          # Hello, Guest!
print(greet("Alice"))   # Hello, Alice!

# None sebagai nilai pengembalian
def find_value(data, key):
    if key in data:
        return data[key]
    return None

result = find_value({"a": 1, "b": 2}, "c")
if result is None:
    print("Kunci tidak ditemukan")
                    </code></pre>
                    """,
                    "order": 1
                }
            ]
        },
        {
            "title": "Type Conversion",
            "order": 7,
            "contents": [
                {
                    "content_type": "text",
                    "content": """
                    <h3>Konversi Tipe Data di Python</h3>
                    <p>Python menyediakan beberapa fungsi bawaan untuk mengkonversi satu tipe data ke tipe data lainnya.</p>
                    
                    <h4>Konversi ke Integer</h4>
                    <p>Menggunakan fungsi int() untuk mengkonversi ke tipe data integer:</p>
                    <pre><code>
# String ke integer
print(int("10"))       # 10
print(int("0xFF", 16)) # 255 (hexadecimal)
print(int("101", 2))   # 5 (binary)

# Float ke integer (memotong desimal)
print(int(10.8))       # 10
print(int(-10.8))      # -10

# Boolean ke integer
print(int(True))       # 1
print(int(False))      # 0

# Error case
# print(int("Hello"))  # ValueError: invalid literal for int()
                    </code></pre>
                    
                    <h4>Konversi ke Float</h4>
                    <p>Menggunakan fungsi float() untuk mengkonversi ke tipe data float:</p>
                    <pre><code>
# String ke float
print(float("10.5"))   # 10.5
print(float("10"))     # 10.0
print(float("-1.23"))  # -1.23
print(float("1e3"))    # 1000.0

# Integer ke float
print(float(10))       # 10.0

# Boolean ke float
print(float(True))     # 1.0
print(float(False))    # 0.0

# Error case
# print(float("Hello"))  # ValueError: could not convert string to float
                    </code></pre>
                    
                    <h4>Konversi ke String</h4>
                    <p>Menggunakan fungsi str() untuk mengkonversi ke tipe data string:</p>
                    <pre><code>
# Number ke string
print(str(10))         # "10"
print(str(10.5))       # "10.5"

# Boolean ke string
print(str(True))       # "True"
print(str(False))      # "False"

# List ke string
print(str([1, 2, 3]))  # "[1, 2, 3]"

# Dictionary ke string
print(str({"a": 1}))   # "{'a': 1}"
                    </code></pre>
                    
                    <h4>Konversi ke Boolean</h4>
                    <p>Menggunakan fungsi bool() untuk mengkonversi ke tipe data boolean:</p>
                    <pre><code>
# Number ke boolean
print(bool(1))         # True
print(bool(0))         # False
print(bool(10))        # True
print(bool(-1))        # True

# String ke boolean
print(bool(""))        # False (string kosong)
print(bool("Hello"))   # True (string tidak kosong)

# List/Tuple/Dictionary/Set ke boolean
print(bool([]))        # False (list kosong)
print(bool([1, 2]))    # True (list tidak kosong)
print(bool({}))        # False (dictionary kosong)
print(bool({1, 2}))    # True (set tidak kosong)
                    </code></pre>
                    
                    <h4>Konversi ke List, Tuple, dan Set</h4>
                    <p>Mengkonversi tipe data iterable ke list, tuple, atau set:</p>
                    <pre><code>
# String ke list, tuple, set
s = "hello"
print(list(s))        # ['h', 'e', 'l', 'l', 'o']
print(tuple(s))       # ('h', 'e', 'l', 'l', 'o')
print(set(s))         # {'h', 'e', 'l', 'o'} (set menghilangkan duplikat)

# Konversi antara list, tuple, dan set
my_list = [1, 2, 3, 2]
print(tuple(my_list))  # (1, 2, 3, 2)
print(set(my_list))    # {1, 2, 3} (menghilangkan duplikat)

my_tuple = (1, 2, 3, 2)
print(list(my_tuple))  # [1, 2, 3, 2]
print(set(my_tuple))   # {1, 2, 3} (menghilangkan duplikat)

my_set = {1, 2, 3}
print(list(my_set))    # [1, 2, 3]
print(tuple(my_set))   # (1, 2, 3)
                    </code></pre>
                    
                    <h4>Konversi ke Dictionary</h4>
                    <p>Mengkonversi pasangan key-value ke dictionary:</p>
                    <pre><code>
# List of tuples (key, value) ke dictionary
items = [("a", 1), ("b", 2), ("c", 3)]
print(dict(items))     # {'a': 1, 'b': 2, 'c': 3}

# Zip dua list ke dictionary
keys = ["a", "b", "c"]
values = [1, 2, 3]
print(dict(zip(keys, values)))  # {'a': 1, 'b': 2, 'c': 3}

# Keyword arguments ke dictionary
print(dict(a=1, b=2, c=3))     # {'a': 1, 'b': 2, 'c': 3}
                    </code></pre>
                    
                    <h4>Praktik yang Disarankan</h4>
                    <ol>
                        <li>Selalu perhatikan kemungkinan error saat melakukan konversi tipe data</li>
                        <li>Gunakan try-except untuk menangani error konversi</li>
                        <li>Verifikasi terlebih dahulu apakah konversi valid</li>
                    </ol>
                    
                    <pre><code>
def safe_int_convert(value):
    try:
        return int(value), True
    except (ValueError, TypeError):
        return None, False

num, success = safe_int_convert("123")
if success:
    print(f"Konversi berhasil: {num}")
else:
    print("Konversi gagal")

num, success = safe_int_convert("abc")
if success:
    print(f"Konversi berhasil: {num}")
else:
    print("Konversi gagal")
                    </code></pre>
                    """,
                    "order": 1
                }
            ]
        },
        {
            "title": "Quiz: Python Data Types",
            "order": 8,
            "contents": [
                {
                    "content_type": "text",
                    "content": """
                    <h3>Quiz: Python Data Types</h3>
                    <p>Uji pemahaman Anda tentang tipe data Python dengan menjawab pertanyaan-pertanyaan berikut.</p>
                    
                    <div class="quiz-container">
                        <div class="quiz-question">
                            <p><strong>1. Manakah dari berikut ini yang tidak termasuk tipe data numerik di Python?</strong></p>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="q1" id="q1_a" value="a">
                                <label class="form-check-label" for="q1_a">Integer</label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="q1" id="q1_b" value="b">
                                <label class="form-check-label" for="q1_b">Float</label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="q1" id="q1_c" value="c">
                                <label class="form-check-label" for="q1_c">Complex</label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="q1" id="q1_d" value="d">
                                <label class="form-check-label" for="q1_d">Array</label>
                            </div>
                            <p class="answer-feedback" id="feedback_q1" style="display: none;">Jawaban yang benar adalah Array. Di Python, Array bukan tipe data bawaan seperti integer, float, dan complex.</p>
                        </div>
                        
                        <div class="quiz-question">
                            <p><strong>2. Manakah cara yang benar untuk membuat set kosong di Python?</strong></p>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="q2" id="q2_a" value="a">
                                <label class="form-check-label" for="q2_a">empty_set = {}</label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="q2" id="q2_b" value="b">
                                <label class="form-check-label" for="q2_b">empty_set = set()</label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="q2" id="q2_c" value="c">
                                <label class="form-check-label" for="q2_c">empty_set = [ ]</label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="q2" id="q2_d" value="d">
                                <label class="form-check-label" for="q2_d">empty_set = ( )</label>
                            </div>
                            <p class="answer-feedback" id="feedback_q2" style="display: none;">Jawaban yang benar adalah empty_set = set(). Notasi {} menciptakan dictionary kosong, bukan set kosong.</p>
                        </div>
                        
                        <div class="quiz-question">
                            <p><strong>3. Apa output dari kode berikut? <code>print(bool(""), bool("False"), bool(0), bool([0]))</code></strong></p>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="q3" id="q3_a" value="a">
                                <label class="form-check-label" for="q3_a">False False False False</label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="q3" id="q3_b" value="b">
                                <label class="form-check-label" for="q3_b">False True False True</label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="q3" id="q3_c" value="c">
                                <label class="form-check-label" for="q3_c">False False False True</label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="q3" id="q3_d" value="d">
                                <label class="form-check-label" for="q3_d">True True False True</label>
                            </div>
                            <p class="answer-feedback" id="feedback_q3" style="display: none;">Jawaban yang benar adalah False True False True. String kosong dan angka 0 dievaluasi sebagai False, tetapi string "False" adalah string tidak kosong (True) dan list [0] bukan list kosong (True).</p>
                        </div>
                        
                        <div class="quiz-question">
                            <p><strong>4. Tipe data mana yang immutable (tidak dapat diubah) di Python?</strong></p>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="q4" id="q4_a" value="a">
                                <label class="form-check-label" for="q4_a">List</label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="q4" id="q4_b" value="b">
                                <label class="form-check-label" for="q4_b">Dictionary</label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="q4" id="q4_c" value="c">
                                <label class="form-check-label" for="q4_c">Set</label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="q4" id="q4_d" value="d">
                                <label class="form-check-label" for="q4_d">Tuple</label>
                            </div>
                            <p class="answer-feedback" id="feedback_q4" style="display: none;">Jawaban yang benar adalah Tuple. Tuple bersifat immutable, sedangkan List, Dictionary, dan Set bersifat mutable (dapat diubah).</p>
                        </div>
                        
                        <div class="quiz-question">
                            <p><strong>5. Apa hasil dari ekspresi berikut? <code>set([1, 2, 3, 3, 2, 1])</code></strong></p>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="q5" id="q5_a" value="a">
                                <label class="form-check-label" for="q5_a">{1, 2, 3, 1, 2, 3}</label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="q5" id="q5_b" value="b">
                                <label class="form-check-label" for="q5_b">{1, 2, 3}</label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="q5" id="q5_c" value="c">
                                <label class="form-check-label" for="q5_c">{3, 2, 1}</label>
                            </div>
                            <div class="form-check">
                                <input class="form-check-input" type="radio" name="q5" id="q5_d" value="d">
                                <label class="form-check-label" for="q5_d">Error</label>
                            </div>
                            <p class="answer-feedback" id="feedback_q5" style="display: none;">Jawaban yang benar adalah {1, 2, 3}. Set menghilangkan semua duplikat. Urutan elemen dalam set tidak dijamin, maka {3, 2, 1} juga dapat menjadi outputnya.</p>
                        </div>
                        
                        <button id="checkAnswers" class="btn btn-primary mt-3">Periksa Jawaban</button>
                        
                        <div id="quizResult" class="mt-3" style="display: none;">
                            <h4>Hasil Quiz</h4>
                            <p>Skor: <span id="score">0</span>/5</p>
                            <div id="explanation" class="alert alert-info"></div>
                        </div>
                    </div>
                    
                    <script>
                    document.getElementById('checkAnswers').addEventListener('click', function() {
                        const correctAnswers = {
                            q1: 'd',
                            q2: 'b',
                            q3: 'b',
                            q4: 'd',
                            q5: 'b'
                        };
                        
                        let score = 0;
                        let explanation = "";
                        
                        // Check each question
                        for (let q in correctAnswers) {
                            const selectedAnswer = document.querySelector(`input[name="${q}"]:checked`);
                            const feedbackElement = document.getElementById(`feedback_${q}`);
                            
                            if (selectedAnswer) {
                                if (selectedAnswer.value === correctAnswers[q]) {
                                    score++;
                                }
                                // Show feedback for each question
                                feedbackElement.style.display = 'block';
                                feedbackElement.classList.add(selectedAnswer.value === correctAnswers[q] ? 'text-success' : 'text-danger');
                            } else {
                                explanation += `<p>Anda belum menjawab pertanyaan ${q.substring(1)}.</p>`;
                                feedbackElement.style.display = 'none';
                            }
                        }
                        
                        // Show results
                        document.getElementById('score').textContent = score;
                        document.getElementById('explanation').innerHTML = explanation;
                        document.getElementById('quizResult').style.display = 'block';
                        
                        // If all answers are correct, mark as completed
                        if (score === 5) {
                            // In a real implementation, this would communicate with the server
                            // to mark this subchapter as completed
                            alert("Selamat! Anda telah berhasil menyelesaikan quiz ini.");
                        }
                    });
                    </script>
                    """,
                    "order": 1
                }
            ]
        }
    ]
    
    # Add subchapters and content
    for subchapter_data in subchapters_data:
        subchapter = SubChapter(
            chapter_id=chapter.id,
            title=subchapter_data["title"],
            order=subchapter_data["order"]
        )
        db.session.add(subchapter)
        db.session.commit()
        print(f"Subchapter ditambahkan: {subchapter.title}")
        
        # Tambahkan konten untuk subchapter ini
        for content_data in subchapter_data["contents"]:
            content = Content(
                subchapter_id=subchapter.id,
                content_type=content_data["content_type"],
                content=content_data["content"],
                order=content_data["order"]
            )
            db.session.add(content)
        
        db.session.commit()
        print(f"  Konten ditambahkan untuk subchapter: {subchapter.title}")
    
    print("Berhasil menambahkan semua data untuk Python Data Types (Chapter ID=2)")
