import pandas as pd
import matplotlib.pyplot as plt

# ตัวอย่าง data ตามภาพ A.png และ B.png ทดลอง Get Data จากไฟล์ bookstore.xlsx
# rename column รหัสลูกค้าให้กลายเป็นชื่อ customer และยอดขายเป็น sales
df = pd.DataFrame({'Customer':dataset.customer,'Sales':dataset.sales})

# group ข้อมูลแล้ว sum ยอด sales
result_df = df.groupby('Customer',as_index=False)['Sales'].sum()

# sort ข้อมูลให้เรียงจากมากไปน้อย
result_df.sort_values(by='Sales',ascending=False,inplace=True)

# plotgraph bar chart
plt.bar(result_df['Customer'],result_df['Sales'])
plt.show()