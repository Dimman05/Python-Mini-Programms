import gzip 
import os

folder = 'C:\\Users\\Dimitris\\Desktop\\books'
book_list = os.listdir(folder)


for i in range(0, len(book_list)):
    try:
        f_in = open(f'{folder}\\{book_list[i]}', 'rb')
        f_out = gzip.open(f'{book_list[i]}.gz', 'wb')
        f_out.writelines(f_in)
        f_out.close()
        f_in.close()
    except Exception:
        pass



new_folder = 'C:\\Users\\Dimitris\\Desktop\\new'
new_list = os.listdir(new_folder)

print(len(book_list))
print(len(new_list))