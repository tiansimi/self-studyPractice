__author__ = '努力学习 不要让自己失望'
import json

fd = open("./duo.txt", "r")
data = fd.read()
dict_data = json.loads(data)
print(type(dict_data))
question_detail = dict_data["args"]["questions"]
# print(question_detail)
fw = open('./777.txt', "w+", encoding="utf-8")
i = 1
for k in question_detail:
    # print(question_detail[k]["questionid"])
    question_detail[k]["questionid"] = i
    fw.write(str(question_detail[k]["questionid"]))
    fw.write("、")
    q = question_detail[k]["question"]
    q = str(q).replace("<p>", "")
    q = str(q).replace("</p>", "")
    fw.write(q)
    fw.write("\n")
    select = str(question_detail[k]["questionselect"])
    select = select.replace("&lt;p&gt;", "")
    select = select.replace("&lt;/p&gt;", "")
    fw.write(select)
    fw.write("\n")
    fw.write("答案：" + str(question_detail[k]["questionanswer"]))
    fw.write("\n")
    i += 1

fw.close()
fd.close()
