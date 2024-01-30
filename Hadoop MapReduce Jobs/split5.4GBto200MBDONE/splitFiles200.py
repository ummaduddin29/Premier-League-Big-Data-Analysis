import os
import csv

input_file = r"C:\Users\Ummad\Downloads\archive\male_players.csv"
output_folder = r"C:\Users\Ummad\Downloads\archive\split_files"

max_file_size = 200 * 1024 * 1024 

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

with open(input_file, 'r', encoding='utf-8') as infile:
    reader = csv.reader(infile)
    header_row = next(reader)  
    
    output_file = None
    writer = None
    
    row_count = 0
    file_count = 0
    for row in reader:
        row_count += 1
        
        if output_file is None or output_file.tell() >= max_file_size:
            if output_file is not None:
                output_file.close()
                print(f"Finished writing {os.path.basename(output_file.name)}")
            
            file_count += 1
            output_file_path = os.path.join(output_folder, f"split_file_{file_count}.csv")
            output_file = open(output_file_path, 'w', newline='', encoding='utf-8')
            writer = csv.writer(output_file)
            writer.writerow(header_row)
            print(f"Starting to write {os.path.basename(output_file.name)}")
        
        writer.writerow(row)
    
    if output_file is not None:
        output_file.close()
        print(f"Finished writing {os.path.basename(output_file.name)}")
    
    print(f"Processed {row_count} rows and wrote {file_count} output files.")

print("File split successfully!")
