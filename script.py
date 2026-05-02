import pandas as pd

big_file = r"D:\MERGE_SMART METER DATA\AGRA_66.csv"
consumer_file = r"D:\MERGE_SMART METER DATA\mar-2026_gmr_smart_meter consumers.xlsx"

# columns
big_col = "METER_NUMBER"
small_col = "Meter_No_2"

# small file load
consumers = pd.read_excel(consumer_file, dtype=str)

# clean + set
consumer_set = set(consumers[small_col].str.strip())

found = set()

# big file chunk me read
for chunk in pd.read_csv(big_file, chunksize=100000, dtype=str):
    
    chunk[big_col] = chunk[big_col].str.strip()
    
    matched = chunk[chunk[big_col].isin(consumer_set)]
    
    found.update(matched[big_col])

# results
found_list = list(found)
not_found_list = list(consumer_set - found)

print(f"Total consumers: {len(consumer_set)}")
print(f"Found: {len(found_list)}")
print(f"Not Found: {len(not_found_list)}")

# save outputs
pd.DataFrame({small_col: found_list}).to_csv(
    r"D:\MERGE_SMART METER DATA\found_consumers.csv", index=False
)

pd.DataFrame({small_col: not_found_list}).to_csv(
    r"D:\MERGE_SMART METER DATA\not_found_consumers.csv", index=False
)

print("Done! Found & Not Found dono files ban gayi.")

 
