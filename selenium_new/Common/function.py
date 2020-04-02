import os, configparser


# 获取项目路径
def project_path():
    return os.path.split(os.path.realpath(__file__))[0].split('C')[0]


# 返回config.ini文件中的testUrl
def config_url():
    config = configparser.ConfigParser()
    config.read(project_path()+"config.ini")
    return config.get('testUrl', 'url')


if __name__ == '__main__':
    print("项目路径是："+project_path())
    print("被测系统url是："+config_url())