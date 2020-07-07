from flask import Blueprint, jsonify

# Blueprint:蓝图，用来创建一个模块

dataprovider = Blueprint('dataprovider', __name__)
#

@dataprovider.route('/get_jobNeeds', endpoint='get_jobneeds')
def get_jobNeeds():
    data = ['4567', '2323', '4034', '2452', '2312', '3333']
    return jsonify(data)


@dataprovider.route('/get_jobSalary', endpoint='get_jobSalary')
def get_jobSalary():
    data = ['11309', '13456', '10424', '12232', '14232', '13333']
    return jsonify(data)


@dataprovider.route('/get_languageNeeds', endpoint='get_languageNeeds')
def get_languageNeeds():
    data = {}
    data["xlabel"] = ['Java', 'PHP', 'Python', 'C/C++', 'GO', 'ruby']
    data["series_data"] = [
        {"name": 'Java', "value": 1},
        {"value": 3, "name": 'Python'},
        {"value": 2, "name": 'PHP'},
        {"value": 2, "name": 'C/C++'},
        {"value": 1, "name": 'GO'},
        {"value": 1, "name": 'ruby'},
    ]

    return jsonify(data)


@dataprovider.route('/get_degreeNeeds', endpoint='get_degreeNeeds')
def get_degreeNeeds():
    data = {}
    data["xlabel"] = ['大专', '本科', '硕士', '博士', '其他']
    data["series_data"] = [
        {"value": 1, "name": '大专'},
        {"value": 4, "name": '本科'},
        {"value": 2, "name": '硕士'},
        {"value": 2, "name": '博士'},
        {"value": 1, "name": '其他'},
    ]
    return jsonify(data)


@dataprovider.route('/get_expNeeds', endpoint='get_expNeeds')
def get_expNeeds():
    data = {}
    data["xlabel"] = ['0', '1年经验', '2年经验', '3-4年经验', '5-7年经验', '8-9年经验', '10年以上经验']
    data["series_data"] = [
        {"value": 1, "name": '0'},
        {"value": 2, "name": '1年经验'},
        {"value": 2, "name": '2年经验'},
        {"value": 2, "name": '3-4年经验'},
        {"value": 1, "name": '5-7年经验'},
        {"value": 1, "name": '8-9年经验'},
        {"value": 1, "name": '10年以上经验'},
    ]
    return jsonify(data)


@dataprovider.route('/get_citySalary', endpoint='get_citySalary')
def get_citySalary():
    data = {}
    data["xlabel"] = ['北京', '上海', '广州', '深圳', '杭州', '重庆', '成都', '武汉', '南京', '长沙', '苏州', '西安']
    data["series_data"] = [12345, 14567, 13456, 15643, 11234, 10293, 12034, 11768, 12003, 10345, 12133, 11456]
    return jsonify(data)


@dataprovider.route('/get_coSalary', endpoint='get_coSalary')
def get_coSalary():
    data = {}
    data["xlabel"] = ['百度', '阿里', '腾讯', '美团', '滴滴', '字节跳动']
    data["series_data"] = [12345, 14567, 13456, 12643, 11234, 14034]
    return jsonify(data)


@dataprovider.route('/get_TotalNum', endpoint='get_TotalNum')
def get_TotalNum():
    data = {}
    data["allNeeds"] = 3495932
    data["allSalary"] = 12030
    return jsonify(data)
