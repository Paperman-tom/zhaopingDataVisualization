# 用于返回数据
import json

from flask import Blueprint

from db_model.models import *

data_provider = Blueprint("data_provider", __name__)


# 访问实例：http://127.0.0.1:5000/data/get_jobs_avgSalary就可得到职位平均工资的数据，要访问其他数据以此类推

# 职位平均工资
@data_provider.route("/get_jobs_avgSalary", endpoint="get_jobs_avgSalary")
def get_jobs_avgSalary():
    dic = {}
    dic["xData"] = []
    # 平均工资
    dic["yData"] = []
    data = db.session.query(JobsAvgSalary).all()
    # 岗位名称
    dic["xData"] = ["测试", "产品", "后端开发", "前端开发", "设计", "移动开发", "运行维护"]

    def build_dic(item):
        dic["yData"].append(item.avgSalary)

    [build_dic(i) for i in data]

    return json.dumps(dic)


# 语言需求比例
@data_provider.route("/get_language_proportion", endpoint="get_language_proportion")
def get_language_proportion():
    dic = {}
    a = []
    # 语言名称
    dic["xData"] = []
    # 需求比例
    dic["yData"] = []
    data = db.session.query(LanguageProp).all()

    def func(item):
        a.append(item.count)

    [func(i) for i in data]
    val = sum(a)

    def build_dic(item):
        dic["xData"].append(item.language)
        dic1 = {}
        dic1["name"] = item.language
        dic1["value"] = (item.count / val) * 100
        dic["yData"].append(dic1)

    [build_dic(i) for i in data]

    return json.dumps(dic)


# 职位需求
@data_provider.route("/get_jobs_demand", endpoint="get_jobs_demand")
def get_jobs_demand():
    dic = {}
    # 职位名称
    dic["xData"] = []
    # 需求
    dic["yData"] = []
    data1 = db.session.query(Ceshijobcount).all()
    data2 = db.session.query(Chanpinjobcount).all()
    data3 = db.session.query(Houduanjobcount).all()
    data4 = db.session.query(Qianduanjobcount).all()
    data5 = db.session.query(Shejijobcount).all()
    data6 = db.session.query(Yidongjobcount).all()
    data7 = db.session.query(Yunweijobcount).all()

    dic["xData"] = ["测试", "产品", "后端开发", "前端开发", "设计", "移动开发", "运行维护"]

    def build_dic(item):
        dic["yData"].append(item.count)

    [build_dic(i) for i in data1]
    [build_dic(i) for i in data2]
    [build_dic(i) for i in data3]
    [build_dic(i) for i in data4]
    [build_dic(i) for i in data5]
    [build_dic(i) for i in data6]
    [build_dic(i) for i in data7]

    return json.dumps(dic)


# 城市岗位需求
@data_provider.route("/get_city_demand", endpoint="get_city_demand")
def get_city_demand():
    dic = {}
    a = []
    # 城市
    dic["xData"] = []
    # 工作数量
    dic["yData"] = []
    data = db.session.query(Total7citycount).all()

    def build_dic(item):
        dic["xData"].append(item.city)
        dic1 = {}
        dic1["name"] = item.city
        dic1["value"] = item.count
        dic["yData"].append(dic1)

    [build_dic(i) for i in data]

    return json.dumps(dic)


# 重要城市平均工资
@data_provider.route("/get_city_avgSalary", endpoint="get_city_avgSalary")
def get_city_avgSalary():
    dic = {}
    a = []
    # 城市名称
    dic["xData"] = []
    # 平均工资 单位万/年
    dic["yData"] = []
    data1 = db.session.query(Total7Salary).order_by(Total7Salary.salary_sum.desc()).all()
    data2 = db.session.query(Total7citycount).all()
    lst1 = []
    lst2 = []

    def build_dic(item):
        def func(item2):
            if item2.city == item.city:
                if item.city is None or item.salary_sum is None:
                    pass
                else:
                    lst1.append(item.city)
                    a = item.salary_sum / item2.count
                    lst2.append(a)
            pass

        [func(j) for j in data2]

    [build_dic(i) for i in data1]
    for i in range(15):
        dic["xData"].append(lst1[i])
        dic["yData"].append(lst2[i])
    for i in range(len(dic["yData"])):
        for j in range(len(dic["yData"])):
            if dic["yData"][i] > dic["yData"][j]:
                val1 = dic["yData"][j]
                val2 = dic["xData"][j]
                dic["yData"][j] = dic["yData"][i]
                dic["xData"][j] = dic["xData"][i]
                dic["yData"][i] = val1
                dic["xData"][i] = val2

    return json.dumps(dic)


# 经验需求
@data_provider.route("/get_experience_demand", endpoint="get_experience_demand")
def get_experience_demand():
    dic = {}
    a = []
    # 工作经历要求
    dic["xData"] = []
    # 需求比例
    dic["yData"] = []
    data = db.session.query(Total7workexperiencecount).all()

    def func(item):
        a.append(item.count)

    [func(i) for i in data]
    val = sum(a)

    def build_dic(item):
        dic["xData"].append(item.workExperience)
        dic1 = {}
        dic1["name"] = item.workExperience
        dic1["value"] = (item.count / val) * 100
        dic["yData"].append(dic1)

    [build_dic(i) for i in data]
    return json.dumps(dic)


# 学历需求
@data_provider.route("/get_education_demand", endpoint="get_education_demand")
def get_education_demand():
    dic = {}
    a = []
    # 学历要求
    dic["xData"] = []
    # 需求比例
    dic["yData"] = []
    data = db.session.query(Total7educationcount).all()

    def func(item):
        a.append(item.count)

    [func(i) for i in data]
    val = sum(a)

    def build_dic(item):
        dic1 = {}
        dic1["name"] = item.education
        dic1["value"] = (item.count / val) * 100
        dic["xData"].append(item.education)
        dic["yData"].append(dic1)

    [build_dic(i) for i in data]
    return json.dumps(dic)


# 公司提供岗位数量
@data_provider.route("/get_company_demand", endpoint="get_company_demand")
def get_company_demand():
    dic = {}
    # 公司名称
    dic["xData"] = []
    # 工作数量
    dic["yData"] = []
    lst1 = []
    lst2 = []
    data = db.session.query(Total7companycount).order_by(Total7companycount.count.desc()).all()

    def build_dic(item):
        lst1.append(item.cpmpany)
        lst2.append(item.count)

    [build_dic(i) for i in data]
    for i in range(15):
        dic["xData"].append(lst1[i])
        dic["yData"].append(lst2[i])

    return json.dumps(dic)


# 所有工作平均工资与岗位数
@data_provider.route("/get_enitre_avgSalary", endpoint="get_enitre_avgSalary")
def get_enitre_avgSalary():
    dic = {}
    a = []
    # 所有工作
    dic["xData"] = []
    # 所有工作平均工资 单位万/年
    dic["yData"] = []
    # 互联网工作工作数量
    dic["zData"] = []
    data1 = db.session.query(Total7salarycount).all()
    data2 = db.session.query(Total7jobcount).all()
    dic["xData"] = ["所有工作平均工资"]

    def build_dic(item):
        a.append(item.salary_sum)

        def func(item):
            dic["yData"].append(int(a[0] / item.count))
            dic["zData"].append(item.count)

        [func(j) for j in data2]

    [build_dic(i) for i in data1]

    return json.dumps(dic)
