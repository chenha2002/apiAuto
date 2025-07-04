pipeline {
    agent any

    environment {
        PYTHONPATH = "/var/jenkins_home/workspace/apiAuto"  # 设置项目根目录为Python路径
    }

    stages {
        stage('Test') {
            steps {
                sh '''
                    source /usr/local/src/py3.12/bin/activate  # 激活Python环境
                    pytest tests/  # 运行测试
                '''
            }
        }
    }
}
#