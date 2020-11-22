# 基础镜像
FROM python:3.8.6

# 维护人员
MAINTAINER xuguodong

# 工作文件夹
WORKDIR .

ADD . .

# 安装所需的包
CMD pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

# 执行
CMD ["pytest", "-q", "--alluredir","allure-results"]
