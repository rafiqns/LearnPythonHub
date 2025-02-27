
from app import db
from models import Chapter, SubChapter, Content
from sqlalchemy.exc import SQLAlchemyError

# Cek apakah chapter Python Data Types sudah ada
def add_python_data_types():
    try:
        # Cek apakah chapter sudah ada
        chapter = Chapter.query.filter_by(title="Python Data Types").first()
        
        if not chapter:
            # Jika belum ada, buat chapter baru
            chapter = Chapter(
                title="Python Data Types",
                description="Pelajari berbagai tipe data di Python dan cara menggunakannya",
                order=2,  # Sesuaikan dengan urutan yang diinginkan
                is_pro=False
            )
            db.session.add(chapter)
            db.session.commit()
            print(f"Chapter 'Python Data Types' berhasil dibuat dengan ID: {chapter.id}")
        else:
            print(f"Chapter 'Python Data Types' sudah ada dengan ID: {chapter.id}")
        
        # Tambahkan subchapter
        subchapters = [
            {
                "title": "Tipe Data Dasar",
                "order": 1,
                "contents": [
                    {
                        "content_type": "text",
                        "content": """
                        <h3>Tipe Data Dasar di Python</h3>
                        <p>Python memiliki beberapa tipe data dasar:</p>
                        <ul>
                            <li><strong>Integer (int)</strong>: Bilangan bulat seperti 1, 100, -10</li>
                            <li><strong>Float</strong>: Bilangan desimal seperti 3.14, -0.001</li>
                            <li><strong>String (str)</strong>: Teks yang diapit oleh tanda kutip seperti "Hello" atau 'Python'</li>
                            <li><strong>Boolean (bool)</strong>: Nilai kebenaran True atau False</li>
                        </ul>
                        <h4>Contoh penggunaan:</h4>
                        <pre><code>
# Integer
angka = 10
print(type(angka))  # Output: &lt;class 'int'&gt;

# Float
pi = 3.14
print(type(pi))  # Output: &lt;class 'float'&gt;

# String
nama = "Python"
print(type(nama))  # Output: &lt;class 'str'&gt;

# Boolean
status = True
print(type(status))  # Output: &lt;class 'bool'&gt;
                        </code></pre>
                        """,
                        "order": 1
                    }
                ]
            },
            {
                "title": "List dan Tuple",
                "order": 2,
                "contents": [
                    {
                        "content_type": "text",
                        "content": """
                        <h3>List dan Tuple di Python</h3>
                        <p>List dan tuple adalah tipe data yang digunakan untuk menyimpan kumpulan nilai.</p>
                        
                        <h4>List</h4>
                        <p>List adalah kumpulan item yang terurut dan bisa diubah (mutable). List dibuat dengan tanda kurung siku [].</p>
                        <pre><code>
# Membuat list
buah = ["apel", "jeruk", "mangga"]
print(buah)  # Output: ['apel', 'jeruk', 'mangga']

# Mengakses elemen list
print(buah[0])  # Output: apel

# Mengubah elemen list
buah[1] = "anggur"
print(buah)  # Output: ['apel', 'anggur', 'mangga']

# Menambah elemen list
buah.append("pisang")
print(buah)  # Output: ['apel', 'anggur', 'mangga', 'pisang']
                        </code></pre>
                        
                        <h4>Tuple</h4>
                        <p>Tuple adalah kumpulan item yang terurut dan tidak bisa diubah (immutable). Tuple dibuat dengan tanda kurung ().</p>
                        <pre><code>
# Membuat tuple
koordinat = (10, 20)
print(koordinat)  # Output: (10, 20)

# Mengakses elemen tuple
print(koordinat[0])  # Output: 10

# Tuple tidak bisa diubah
# koordinat[0] = 15  # Ini akan error

# Tuple dengan satu elemen
satu_item = (5,)  # Perhatikan koma setelah angka
print(type(satu_item))  # Output: &lt;class 'tuple'&gt;
                        </code></pre>
                        """,
                        "order": 1
                    }
                ]
            },
            {
                "title": "Dictionary dan Set",
                "order": 3,
                "contents": [
                    {
                        "content_type": "text",
                        "content": """
                        <h3>Dictionary dan Set di Python</h3>
                        
                        <h4>Dictionary</h4>
                        <p>Dictionary adalah kumpulan pasangan key-value yang tidak terurut. Dictionary dibuat dengan tanda kurung kurawal {} dan pasangan key:value.</p>
                        <pre><code>
# Membuat dictionary
siswa = {
    "nama": "Budi",
    "umur": 17,
    "kelas": "XII IPA"
}
print(siswa)  # Output: {'nama': 'Budi', 'umur': 17, 'kelas': 'XII IPA'}

# Mengakses nilai dengan key
print(siswa["nama"])  # Output: Budi

# Mengubah nilai
siswa["umur"] = 18
print(siswa)  # Output: {'nama': 'Budi', 'umur': 18, 'kelas': 'XII IPA'}

# Menambah pasangan key-value baru
siswa["alamat"] = "Jakarta"
print(siswa)  # Output: {'nama': 'Budi', 'umur': 18, 'kelas': 'XII IPA', 'alamat': 'Jakarta'}

# Menghapus pasangan key-value
del siswa["kelas"]
print(siswa)  # Output: {'nama': 'Budi', 'umur': 18, 'alamat': 'Jakarta'}
                        </code></pre>
                        
                        <h4>Set</h4>
                        <p>Set adalah kumpulan item yang tidak terurut dan tidak memiliki duplikat. Set dibuat dengan tanda kurung kurawal {} atau fungsi set().</p>
                        <pre><code>
# Membuat set
warna = {"merah", "hijau", "biru"}
print(warna)  # Output: {'merah', 'hijau', 'biru'} (urutan bisa berbeda)

# Set tidak memiliki duplikat
angka = {1, 2, 2, 3, 3, 3}
print(angka)  # Output: {1, 2, 3}

# Menambah item ke set
warna.add("kuning")
print(warna)  # Output: {'merah', 'hijau', 'biru', 'kuning'} (urutan bisa berbeda)

# Operasi pada set
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union (gabungan)
print(set1 | set2)  # Output: {1, 2, 3, 4, 5}

# Intersection (irisan)
print(set1 & set2)  # Output: {3}

# Difference (selisih)
print(set1 - set2)  # Output: {1, 2}
                        </code></pre>
                        """,
                        "order": 1
                    }
                ]
            },
            {
                "title": "Konversi Tipe Data",
                "order": 4,
                "contents": [
                    {
                        "content_type": "text",
                        "content": """
                        <h3>Konversi Tipe Data di Python</h3>
                        <p>Python memungkinkan konversi antar tipe data dengan menggunakan fungsi bawaan.</p>
                        
                        <h4>Konversi ke Integer</h4>
                        <pre><code>
# String ke integer
angka_str = "10"
angka_int = int(angka_str)
print(angka_int)  # Output: 10
print(type(angka_int))  # Output: &lt;class 'int'&gt;

# Float ke integer
angka_float = 10.7
angka_int = int(angka_float)
print(angka_int)  # Output: 10 (desimal dipotong, bukan dibulatkan)
                        </code></pre>
                        
                        <h4>Konversi ke Float</h4>
                        <pre><code>
# String ke float
angka_str = "3.14"
angka_float = float(angka_str)
print(angka_float)  # Output: 3.14
print(type(angka_float))  # Output: &lt;class 'float'&gt;

# Integer ke float
angka_int = 5
angka_float = float(angka_int)
print(angka_float)  # Output: 5.0
                        </code></pre>
                        
                        <h4>Konversi ke String</h4>
                        <pre><code>
# Integer ke string
angka = 42
angka_str = str(angka)
print(angka_str)  # Output: "42"
print(type(angka_str))  # Output: &lt;class 'str'&gt;

# Float ke string
pi = 3.14159
pi_str = str(pi)
print(pi_str)  # Output: "3.14159"
                        </code></pre>
                        
                        <h4>Konversi ke List, Tuple, dan Set</h4>
                        <pre><code>
# String ke list/tuple/set
text = "Python"
print(list(text))  # Output: ['P', 'y', 't', 'h', 'o', 'n']
print(tuple(text))  # Output: ('P', 'y', 't', 'h', 'o', 'n')
print(set(text))  # Output: {'P', 'y', 't', 'h', 'o', 'n'}

# Konversi antar list, tuple, dan set
my_list = [1, 2, 3, 3]
print(tuple(my_list))  # Output: (1, 2, 3, 3)
print(set(my_list))  # Output: {1, 2, 3}
                        </code></pre>
                        """,
                        "order": 1
                    },
                    {
                        "content_type": "video",
                        "content": "https://www.youtube.com/embed/gCCVsvgR2KU",
                        "order": 2
                    }
                ]
            },
            {
                "title": "Latihan dan Quiz",
                "order": 5,
                "contents": [
                    {
                        "content_type": "text",
                        "content": """
                        <h3>Latihan Tipe Data Python</h3>
                        <p>Cobalah latihan berikut untuk meningkatkan pemahaman Anda tentang tipe data Python:</p>
                        
                        <h4>Latihan 1: Konversi Suhu</h4>
                        <p>Buatlah program untuk mengkonversi suhu dari Celsius ke Fahrenheit menggunakan rumus: F = (C × 9/5) + 32</p>
                        <pre><code>
# Kode untuk konversi suhu
celsius = float(input("Masukkan suhu dalam Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} derajat Celsius = {fahrenheit} derajat Fahrenheit")
                        </code></pre>
                        
                        <h4>Latihan 2: Manipulasi List</h4>
                        <p>Buatlah program yang meminta input 5 angka dari pengguna dan menyimpannya dalam list. Kemudian, tampilkan:</p>
                        <ul>
                            <li>Angka terbesar</li>
                            <li>Angka terkecil</li>
                            <li>Jumlah semua angka</li>
                            <li>Rata-rata</li>
                        </ul>
                        <pre><code>
# Kode untuk manipulasi list
angka = []

for i in range(5):
    nilai = float(input(f"Masukkan angka ke-{i+1}: "))
    angka.append(nilai)

print(f"List angka: {angka}")
print(f"Angka terbesar: {max(angka)}")
print(f"Angka terkecil: {min(angka)}")
print(f"Jumlah semua angka: {sum(angka)}")
print(f"Rata-rata: {sum(angka)/len(angka)}")
                        </code></pre>
                        
                        <h4>Quiz</h4>
                        <p>Jawablah pertanyaan berikut:</p>
                        <ol>
                            <li>Apa hasil dari <code>type(3.14)</code>?</li>
                            <li>Apa yang akan ditampilkan oleh kode berikut?
                            <pre><code>x = [1, 2, 3]
y = x
y.append(4)
print(x)</code></pre></li>
                            <li>Bagaimana cara membuat tuple yang hanya berisi satu elemen?</li>
                            <li>Apa perbedaan utama antara list dan tuple?</li>
                            <li>Apa output dari kode berikut?
                            <pre><code>set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)</code></pre></li>
                        </ol>
                        
                        <h4>Jawaban Quiz</h4>
                        <ol>
                            <li><code>&lt;class 'float'&gt;</code></li>
                            <li><code>[1, 2, 3, 4]</code> (karena list bersifat mutable, perubahan pada y juga mempengaruhi x)</li>
                            <li>Dengan menambahkan koma setelah elemen, contoh: <code>(5,)</code></li>
                            <li>List bersifat mutable (dapat diubah setelah dibuat), sedangkan tuple bersifat immutable (tidak dapat diubah setelah dibuat)</li>
                            <li><code>{1, 2, 3, 4, 5}</code> (union/gabungan dari dua set)</li>
                        </ol>
                        """,
                        "order": 1
                    }
                ]
            }
        ]
        
        # Tambahkan semua subchapter dan konten
        for subchapter_data in subchapters:
            # Cek apakah subchapter sudah ada
            subchapter = SubChapter.query.filter_by(
                chapter_id=chapter.id, 
                title=subchapter_data["title"]
            ).first()
            
            if not subchapter:
                subchapter = SubChapter(
                    chapter_id=chapter.id,
                    title=subchapter_data["title"],
                    order=subchapter_data["order"]
                )
                db.session.add(subchapter)
                db.session.commit()
                print(f"  Subchapter '{subchapter_data['title']}' berhasil dibuat")
            else:
                print(f"  Subchapter '{subchapter_data['title']}' sudah ada")
            
            # Tambahkan konten
            for content_data in subchapter_data["contents"]:
                # Cek apakah konten sudah ada
                content = Content.query.filter_by(
                    subchapter_id=subchapter.id,
                    content_type=content_data["content_type"],
                    order=content_data["order"]
                ).first()
                
                if not content:
                    content = Content(
                        subchapter_id=subchapter.id,
                        content_type=content_data["content_type"],
                        content=content_data["content"],
                        order=content_data["order"]
                    )
                    db.session.add(content)
                    print(f"    Konten '{content_data['content_type']}' (order: {content_data['order']}) berhasil ditambahkan")
                else:
                    content.content = content_data["content"]
                    print(f"    Konten '{content_data['content_type']}' (order: {content_data['order']}) diperbarui")
            
        db.session.commit()
        print("Semua konten Python Data Types berhasil ditambahkan!")
        return True
    
    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"Error: {str(e)}")
        return False

if __name__ == "__main__":
    from app import create_app
    app = create_app()
    with app.app_context():
        add_python_data_types()
