import customtkinter
import crawel_data

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500*350")
root.title("新闻爬取软件")
demo = crawel_data.crawel_data()


def login():
    demo.requests_(entry1.get(),entry2.get())
    demo.get_brower(demo.reflist,entry3.get())
    entry1.delete(0,len(entry1.get()))
    entry2.delete(0, len(entry2.get()))
    demo.reflist=[]
    demo.data = {
        'newsNumber': '999999999',
        'pageSize': '20',
        'pageIndex': '1',
        'subChannelNumber': '0',
        'NewsSiteJson':'[{"paramenterlist":[{"ApplcationName":"https://cqyt.eip.cnpc/sites/d1cyc/news","ColumnEnName":"tzgg"}]}]'
        }


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20,padx=60,fill="both",expand=True)

label = customtkinter.CTkLabel(master=frame,text="爬虫系统")
label.pack(pady=12,padx=10)

entry1 = customtkinter.CTkEntry(master=frame,placeholder_text="关键词")
entry1.pack(pady=12,padx=10)

entry2 = customtkinter.CTkEntry(master=frame,placeholder_text="页数")
entry2.pack(pady=12,padx=10)

entry3 = customtkinter.CTkEntry(master=frame,placeholder_text="浏览器驱动路径")
entry3.pack(pady=12,padx=10)

button = customtkinter.CTkButton(master=frame,text="查询",command=login)
button.pack(pady=12,padx=10)



'''
checkbox = customtkinter.CTkCheckBox(master=frame,text="记住账号")
checkbox.pack(pady=12,padx=10)
'''
root.mainloop()