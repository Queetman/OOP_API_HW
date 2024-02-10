from pathlib import Path

# открытие файла
def open_file(file_path, enc):
  arr =[]
  with open(file_path, encoding=enc) as f:
    for line in f:
      arr.append(line)
  return arr


'''
Необходимо объединить их в один по следующим правилам:

Содержимое исходных файлов в результирующем файле должно быть отсортировано по количеству строк в них (то есть первым нужно записать файл с наименьшим количеством строк, а последним - с наибольшим)
Содержимое файла должно предваряться служебной информацией на 2-х строках: имя файла и количество строк в нем
'''

file_path_1 = Path("C:\\Users\\queet\\Dropbox\\Нетология_pyton\\3 ООП и работа с API\\3 Открытие и чтение файла, запись в файл\\ДЗ\\1.txt")
file_path_2 = Path("C:\\Users\\queet\\Dropbox\\Нетология_pyton\\3 ООП и работа с API\\3 Открытие и чтение файла, запись в файл\\ДЗ\\2.txt")
file_path_3 = Path("C:\\Users\\queet\\Dropbox\\Нетология_pyton\\3 ООП и работа с API\\3 Открытие и чтение файла, запись в файл\\ДЗ\\3.txt")
write_path = Path("C:\\Users\\queet\\Dropbox\\Нетология_pyton\\3 ООП и работа с API\\3 Открытие и чтение файла, запись в файл\\ДЗ\\out.txt")



file_1_arr = open_file(file_path_1,'windows-1251')
file_2_arr = open_file(file_path_2,'windows-1251')
file_3_arr = open_file(file_path_3,'UTF-8')

data ={'1.txt': {'length': len(file_1_arr), 'Data':file_1_arr, 'path':file_path_1,},
      '2.txt': {'length': len(file_2_arr), 'Data':file_2_arr, 'path':file_path_2},
      '3.txt': {'length': len(file_3_arr), 'Data':file_3_arr,'path':file_path_3}
      }



   
len_arr =[len(file_1_arr), len(file_2_arr), len(file_3_arr)]
len_arr.sort()


for l in len_arr:
  for file_name, info in data.items():
    if info['length'] ==l:
        with open(write_path, 'a') as f:
            text = f'\n{file_name}\n {l}\n'
            f.write(text)
        for str_tata in info['Data']:
            st = str_tata
            print(st)
            with open(write_path, 'a') as f:
                f.write(st)
            len = info['length']
       



