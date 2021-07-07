import webbrowser
import csv
import glob



#准备表格数据
pair_arr=[]
#通配符检索当前文件夹下第一csv文件
file_name = glob.glob(r'./*.csv')[0].replace("csv","html")
print(file_name)
with open(glob.glob(r'./*.csv')[0], "r", encoding='utf-8') as data:
	reader = csv.reader(data)
	for row in reader:
		pair_arr.append(row)

#命名生成的html
GEN_HTML = file_name
#打开文件，准备写入
f = open(GEN_HTML,'w', encoding='utf-8')
 
# 写入HTML界面中
head = """
<html>
<head><style type="text/css">
			/*表格样式*/			
			table {
				width: 90%;
				background: #ccc;
				margin: 10px auto;
				border-collapse: collapse;/*border-collapse:collapse合并内外边距(去除表格单元格默认的2个像素内外边距*/	
			}				
			th,td {
				height: 25px;
				line-height: 25px;
				text-align: center;
				border: 1px solid #ccc;
			}		
			th {
				background: #eee;
				font-weight: normal;
			}		
			tr {
				background: #fff;
			}		
			tr:hover {
				background: #cc0;
			}		
			td a {
				color: #06f;
				text-decoration: none;
			}		
			td a:hover {
				color: #06f;
				text-decoration: underline;
			}
		</style>

</head>
<body>
"""

body_head="""
<table border="1">
<tr>"""

message= head + body_head

for title in pair_arr[0]:
    body_head_title="""
      <th>%s</th>
    """%(title)
    message = message + body_head_title



for i in pair_arr[1:]:
    message = message +"""<tr>"""
    for j in i:
        body_tail="""
          <td>%s</td>
        """%(j)
        message=message+body_tail

#写入文件
f.write(message) 
#关闭文件
f.close()
 
#运行完自动在网页中显示
webbrowser.open(GEN_HTML,new = 1) 
