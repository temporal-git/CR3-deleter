# CR3-deleter

### RU ###
Программа служит для ускорения сортировки фотографий для фотоаппаратов Canon.

Программа позволяет автоматически удалять в корзину RAW файлы, для которых нет пары с файлом формата .JPG. 
При наличии .xmp файлов для удаляемых RAW, удаляет и их. Вложенные папки и файлы иных форматов не трогает.

Логика работы: Сьемка ведется в режиме RAW + JPG. Мы получаем папку с файлами двух типов. JPG нужны для быстрого просмотра и удаления плохих файлов, т.е. выступают в роли прокси файлов для быстрого просмотра. Удалив ненужные файлы формата JPG, запускаем программу, выбираем нужную папку, после чего удаляются оставшиеся RAW дубли для удаленных ранее JPG


### ENG ###
This program is designed to speed up photo sorting for Canon cameras.

The program automatically deletes RAW files that don't have a matching .JPG file and puts them in the Recycle Bin. If there are .XMP files for the RAW files being deleted, it also deletes them. Subfolders and files of other formats are not affected.

How it works: Shooting is done in RAW + JPG mode. This results in a folder containing two file types. JPG files are needed for quick viewing and deletion of bad files, acting as proxy files for quick viewing. After deleting unnecessary JPG files, launch the program, select the desired folder, and the remaining RAW duplicates for the previously deleted JPG files are deleted.
