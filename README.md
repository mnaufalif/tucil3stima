# Tucil 3 Stima: 13519066, 13519088
Update 4 April
- Pindah ke jupyter
- Load map, init node lewat load txt, display graph beres (kalo ada waktu, init node lewat mapclick bakal coba buat)
- Tinggal algo A* nya

Specification:
- Input file berupa 2 buah txt : 1. Koor(namadaerah) yang berisi daftar latitude, longitude dan nama persimpangan. 2. Adj(namadaerah) berisi representasi adjacency matrix daerah
- Main program diletakkan pada .ipnyb dengan kode pendukung lainnya pada .py
- Main program pada .ipnyb di-run satu per satu sesuai blok In[]

Requirement:
- python v3 ke atas + anaconda dan jupyter dengan versi yang sama
- Telah terpasang folium, branca, jinja2 dan requests. Dapat diperiksa dengan `conda  list` pada anaconda prompt.
- Lengkapi jika ada dari keempat library tersebut yang belum terpasang

  folium : `pip3 install folium` (di cmd) atau `conda install -c conda-forge folium` (di anaconda prompt), 
  branca : `pip3 install branca`, 
  jinja2: `pip3 install jinja2`, 
  requests: `pip3 install requests`

Jika loading sangat lama saat di run, restart dan reopen jupyter
