# 用于从数据库获取数据
from config import db


# 城市需求模块
class Ceshicitycount(db.Model):
    __tablename__ = "ceshi_city_count"
    city = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Chanpincitycount(db.Model):
    __tablename__ = "chanpin_city_count"
    city = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Houduancitycount(db.Model):
    __tablename__ = "houduan_city_count"
    city = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Qianduancitycount(db.Model):
    __tablename__ = "qianduan_city_count"
    city = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Shejicitycount(db.Model):
    __tablename__ = "sheji_city_count"
    city = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Yidongcitycount(db.Model):
    __tablename__ = "yidong_city_count"
    city = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Yunweicitycount(db.Model):
    __tablename__ = "yunwei_city_count"
    city = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Total7citycount(db.Model):
    __tablename__ = "total_7_city_count"
    city = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Ccitycount(db.Model):
    __tablename__ = "c_city_count"
    city = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Gocitycount(db.Model):
    __tablename__ = "go_city_count"
    city = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Javacitycount(db.Model):
    __tablename__ = "java_city_count"
    city = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Phpcitycount(db.Model):
    __tablename__ = "php_city_count"
    city = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Pythoncitycount(db.Model):
    __tablename__ = "python_city_count"
    city = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Rubycitycount(db.Model):
    __tablename__ = "ruby_city_count"
    city = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


# 公司模块
class Ceshicompany_count(db.Model):
    __tablename__ = "ceshi_company_count"
    company = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Chanpincompanycount(db.Model):
    __tablename__ = "chanpin_company_count"
    company = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Houduancompanycount(db.Model):
    __tablename__ = "houduan_company_count"
    company = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Qianduancompanycount(db.Model):
    __tablename__ = "qianduan_company_count"
    company = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Shejicompanycount(db.Model):
    __tablename__ = "sheji_company_count"
    company = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Yidongcompanycount(db.Model):
    __tablename__ = "yidong_company_count"
    company = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Yunweicompanycount(db.Model):
    __tablename__ = "yunwei_company_count"
    company = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Total7companycount(db.Model):
    __tablename__ = "total_7_company_count"
    cpmpany = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Ccompanycount(db.Model):
    __tablename__ = "c_company_count"
    company = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Gocompanycount(db.Model):
    __tablename__ = "go_company_count"
    company = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Javacompanycount(db.Model):
    __tablename__ = "java_company_count"
    company = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Phpcompanycount(db.Model):
    __tablename__ = "php_company_count"
    company = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Pythoncompanycount(db.Model):
    __tablename__ = "python_company_count"
    company = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Rubycompanycount(db.Model):
    __tablename__ = "ruby_company_count"
    company = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


# 学历要求模块
class Ceshieducationcount(db.Model):
    __tablename__ = "ceshi_education_count"
    education = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Chanpineducationcount(db.Model):
    __tablename__ = "chanpin_education_count"
    education = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Houduaneducationcount(db.Model):
    __tablename__ = "houduan_education_count"
    education = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Qianduaneducationcount(db.Model):
    __tablename__ = "qianduan_education_count"
    education = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Shejieducationcount(db.Model):
    __tablename__ = "sheji_education_count"
    education = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Yidongeducationcount(db.Model):
    __tablename__ = "yidong_education_count"
    education = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Yunweieducationcount(db.Model):
    __tablename__ = "yunwei_education_count"
    education = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Total7educationcount(db.Model):
    __tablename__ = "total_7_education_count"
    education = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Ceducationcount(db.Model):
    __tablename__ = "c_education_count"
    education = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Goeducationcount(db.Model):
    __tablename__ = "go_education_count"
    education = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Javaeducationcount(db.Model):
    __tablename__ = "java_education_count"
    education = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Phpeducationcount(db.Model):
    __tablename__ = "php_education_count"
    education = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Pythoneducationcount(db.Model):
    __tablename__ = "python_education_count"
    education = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Rubyeducationcount(db.Model):
    __tablename__ = "ruby_education_count"
    education = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


# 岗位数量模块
class Ceshijobcount(db.Model):
    __tablename__ = "ceshi_job_count"
    job = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Chanpinjobcount(db.Model):
    __tablename__ = "chanpin_job_count"
    job = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Houduanjobcount(db.Model):
    __tablename__ = "houduan_job_count"
    job = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Qianduanjobcount(db.Model):
    __tablename__ = "qianduan_job_count"
    job = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Shejijobcount(db.Model):
    __tablename__ = "sheji_job_count"
    job = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Yidongjobcount(db.Model):
    __tablename__ = "yidong_job_count"
    job = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Yunweijobcount(db.Model):
    __tablename__ = "yunwei_job_count"
    job = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Total7jobcount(db.Model):
    __tablename__ = "total_7_job_count"
    job = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Cjobcount(db.Model):
    __tablename__ = "c_job_count"
    job = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Gojobcount(db.Model):
    __tablename__ = "go_job_count"
    job = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Javajobcount(db.Model):
    __tablename__ = "java_job_count"
    job = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Phpjobcount(db.Model):
    __tablename__ = "php_job_count"
    job = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Pythonjobcount(db.Model):
    __tablename__ = "python_job_count"
    job = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Rubyjobcount(db.Model):
    __tablename__ = "ruby_job_count"
    job = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


# 岗位薪水模块
class Ceshisalarycount(db.Model):
    __tablename__ = "ceshi_salary_count"
    job = db.Column(db.TEXT)
    salary_sum = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Chanpinsalarycount(db.Model):
    __tablename__ = "chanpin_salary_count"
    job = db.Column(db.TEXT)
    salary_sum = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Houduansalarycount(db.Model):
    __tablename__ = "houduan_salary_count"
    job = db.Column(db.TEXT)
    salary_sum = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Qianduansalarycount(db.Model):
    __tablename__ = "qianduan_salary_count"
    job = db.Column(db.TEXT)
    salary_sum = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Shejisalarycount(db.Model):
    __tablename__ = "sheji_salary_count"
    job = db.Column(db.TEXT)
    salary_sum = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Yidongsalarycount(db.Model):
    __tablename__ = "yidong_salary_count"
    job = db.Column(db.TEXT)
    salary_sum = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Yunweisalarycount(db.Model):
    __tablename__ = "yunwei_salary_count"
    job = db.Column(db.TEXT)
    salary_sum = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Total7salarycount(db.Model):
    __tablename__ = "total_7_salary_count"
    job = db.Column(db.TEXT)
    salary_sum = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Csalarycount(db.Model):
    __tablename__ = "c_salary_count"
    job = db.Column(db.TEXT)
    salary_sum = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Gosalarycount(db.Model):
    __tablename__ = "go_salary_count"
    job = db.Column(db.TEXT)
    salary_sum = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Javasalarycount(db.Model):
    __tablename__ = "java_salary_count"
    job = db.Column(db.TEXT)
    salary_sum = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Php_alarycount(db.Model):
    __tablename__ = "php_salary_count"
    job = db.Column(db.TEXT)
    salary_sum = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Pythonsalarycount(db.Model):
    __tablename__ = "python_salary_count"
    job = db.Column(db.TEXT)
    salary_sum = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Rubysalarycount(db.Model):
    __tablename__ = "ruby_salary_count"
    job = db.Column(db.TEXT)
    salary_sum = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


# 工作经验模块
class Ceshiworkexperiencecount(db.Model):
    __tablename__ = "ceshi_workexperience_count"
    workExperience = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Chanpinworkexperiencecount(db.Model):
    __tablename__ = "chanpin_workexperience_count"
    workExperience = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Houduanworkexperiencecount(db.Model):
    __tablename__ = "houduan_workexperience_count"
    workExperience = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Qianduanworkexperiencecount(db.Model):
    __tablename__ = "qianduan_workexperience_count"
    workExperience = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Shejiworkexperiencecount(db.Model):
    __tablename__ = "sheji_workexperience_count"
    workExperience = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Yidongworkexperiencecount(db.Model):
    __tablename__ = "yidong_workexperience_count"
    workExperience = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Yunweiworkexperiencecount(db.Model):
    __tablename__ = "yunwei_workexperience_count"
    workExperience = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Total7workexperiencecount(db.Model):
    __tablename__ = "total_7_workexperience_count"
    workExperience = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Cworkexperiencecount(db.Model):
    __tablename__ = "c_workexperience_count"
    workExperience = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Goworkexperiencecount(db.Model):
    __tablename__ = "go_workexperience_count"
    workExperience = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Javaworkexperiencecount(db.Model):
    __tablename__ = "java_workexperience_count"
    workExperience = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Phpworkexperiencecount(db.Model):
    __tablename__ = "php_workexperience_count"
    workExperience = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Pythonworkexperiencecount(db.Model):
    __tablename__ = "python_workexperience_count"
    workExperience = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class Rubyworkexperiencecount(db.Model):
    __tablename__ = "ruby_workexperience_count"
    workExperience = db.Column(db.TEXT)
    count = db.Column(db.BIGINT)
    id = db.Column(db.BIGINT, primary_key=True)


class JobsAvgSalary(db.Model):
    __tablename__ = "jobs_avgsalary"
    job = db.Column(db.TEXT)
    avgSalary = db.Column(db.FLOAT)
    id = db.Column(db.BIGINT, primary_key=True)


class LanguageProp(db.Model):
    __tablename__ = "lang_avgsalary"
    language = db.Column(db.TEXT)
    count = db.Column(db.FLOAT)
    id = db.Column(db.BIGINT, primary_key=True)

class Total7Salary(db.Model):
    __tablename__ = "total_7_city_salary_count"
    city = db.Column(db.TEXT)
    salary_sum = db.Column(db.FLOAT)
    id = db.Column(db.BIGINT, primary_key=True)