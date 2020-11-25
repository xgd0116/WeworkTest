# 基础镜像
FROM python:3.8.6

# 维护人员
MAINTAINER xuguodong

# 工作文件夹
WORKDIR .

ADD . .

# 安装所需的包
RUN pip install -r requirements.txt

RUN rm -rf allure_results/*

# 执行
CMD ["pytest", "testcase/test_user.py", "-v", "--alluredir", "allure-results"]