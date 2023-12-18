import jenkins


def create_jenkins_jon():
    server = jenkins.Jenkins(
        "http://localhost:8080", username="banhsbao", password="Zoro301120"
    )
    server.create_job(
        name="banhsbao",
        config_xml="""<?xml version='1.1' encoding='UTF-8'?>
    <project>
    <actions/>
    <description>My Jenkins Project</description>
    <keepDependencies>false</keepDependencies>
    <properties/>
    <scm class="hudson.scm.NullSCM"/>
    <canRoam>true</canRoam>
    <disabled>false</disabled>
    <blockBuildWhenUpstreamBuilding>false</blockBuildWhenUpstreamBuilding>
    <triggers/>
    <concurrentBuild>false</concurrentBuild>
    <builders>
        <hudson.tasks.Shell>
        <command>echo "Hello, Jenkins!"</command>
        </hudson.tasks.Shell>
    </builders>
    <publishers/>
    <buildWrappers/>
    </project>
""",
    )


create_jenkins_jon()
