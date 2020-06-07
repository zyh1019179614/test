<style scoped>
.itemstate {
  background-color: white;
  height: 100vh;
  overflow-y: hidden;
  width: 100%;
}
.timeline {
  margin-left: 8%;
  margin-top: 20px;
}
.subtitle {
  margin-left: 7%;
  margin-top: 20px;
  font-size: 20px;
  font-weight: bold;
}
.time {
  font-size: 14px;
  margin-left: 10%;
}
.content {
  font-size: 14px;
}
.subcontent {
  font-size: 12px;
  color: grey;
}
</style>
<template>
  <div class="itemstate">
    <div class="subtitle">项目标题</div>
    <div class="timeline">
      <Timeline>
        <TimelineItem color="blue">
          <Row type="flex" justify="start" align="middle" class="code-row-bg">
            <Col span="3">
              <p class="time">2020.3.1-11:03</p>
            </Col>
            <Col span="1">
              <Avatar style="color: #f56a00;background-color: #fde3cf">U</Avatar>
            </Col>
            <Col span="18">
              <div class="content">持续集成：示例任务 ，任务：1 构建成功</div>
              <div class="subcontent">构建代码仓库：coding-demo，构建版本：[8654243]</div>
            </Col>
          </Row>
        </TimelineItem>
        <TimelineItem color="green">
          <Row type="flex" justify="start" align="middle" class="code-row-bg">
            <Col span="3">
              <p class="time">2020.3.1-11:03</p>
            </Col>
            <Col span="1">
              <Avatar>助手</Avatar>
            </Col>
            <Col span="18">
              <div class="content">项目助手 在制品库仓库 coding-demo 的镜像 coding-demo 中推送了新版本 latest</div>
              <div class="subcontent">\</div>
            </Col>
          </Row>
        </TimelineItem>
        <TimelineItem color="green">
          <Row type="flex" justify="start" align="middle" class="code-row-bg">
            <Col span="3">
              <p class="time">2020.2.29-16:59</p>
            </Col>
            <Col span="1">
<Avatar>助手</Avatar>            </Col>
            <Col span="18">
              <div
                class="content"
              >项目助手 在制品库仓库 coding-demo 的镜像 coding-demo 中推送了新版本865424305518277b6b5873420a7bc8a647bc7af7</div>
              <div class="subcontent">\</div>
            </Col>
          </Row>
        </TimelineItem>
        <TimelineItem color="green">
          <Row type="flex" justify="start" align="middle" class="code-row-bg">
            <Col span="3">
              <p class="time">2020.2.29-16:55</p>
            </Col>
            <Col span="1">
<Avatar>助手</Avatar>            </Col>
            <Col span="18">
              <div class="content">项目助手 在制品库仓库 coding-demo 中创建了制品库镜像 coding-demo
              </div>
              <div class="subcontent">\</div>
            </Col>
          </Row>
        </TimelineItem>
        <TimelineItem color="green"><Row type="flex" justify="start" align="middle" class="code-row-bg">
            <Col span="3">
              <p class="time">2020.2.29-16:54</p>
            </Col>
            <Col span="1">
              <Avatar style="color: #f56a00;background-color: #fde3cf">U</Avatar>
            </Col>
            <Col span="18">
              <div class="content">主账号 创建了代码仓库 coding-demo 的合并请求
              </div>
              <div class="subcontent">test</div>
            </Col>
          </Row>
        </TimelineItem>
        <TimelineItem color="green"><Row type="flex" justify="start" align="middle" class="code-row-bg"><Col span="3">
              <p class="time">2020.2.29-16:53</p>
            </Col>
            <Col span="1">
              <Avatar style="color: #f56a00;background-color: #fde3cf">U</Avatar>
            </Col>
            <Col span="18">
              <div class="content">主账号 创建了任务
              </div>
              <div class="subcontent">#16-[示例任务]-增加邮件邀请成员弹窗并完成邀请成员交互功能</div>
            </Col>
          </Row></TimelineItem></TimelineItem>
        <TimelineItem color="green">
           <Row type="flex" justify="start" align="middle" class="code-row-bg">
            <Col span="3">
              <p class="time">2020.2.29-16:53</p>
            </Col>
            <Col span="1">
              <Avatar style="color: #f56a00;background-color: #fde3cf">U</Avatar>
            </Col>
            <Col span="18">
              <div class="content">主账号 创建了任务
              </div>
              <div class="subcontent">#15-[示例任务]-增加批量发送邀请邮件接口</div>
            </Col>
          </Row>
        </TimelineItem>
        <TimelineItem color="green">
           <Row type="flex" justify="start" align="middle" class="code-row-bg">
            <Col span="3">
              <p class="time">2020.2.29-16:52</p>
            </Col>
            <Col span="1">
              <Avatar style="color: #f56a00;background-color: #fde3cf">U</Avatar>
            </Col>
            <Col span="18">
              <div class="content">主账号 创建了新需求
              </div>
              <div class="subcontent">#14-[示例需求]-通过访问邀请链接可注册成为团队成员</div>
            </Col>
          </Row>
        </TimelineItem>
        <TimelineItem color="green">
          <Row type="flex" justify="start" align="middle" class="code-row-bg">
            <Col span="3">
              <p class="time">2020.2.29-16:50</p>
            </Col>
            <Col span="1">
              <Avatar style="color: #f56a00;background-color: #fde3cf">U</Avatar>
            </Col>
            <Col span="18">
              <div class="content">主账号 创建了新需求
              </div>
              <div class="subcontent">#13-[示例需求]-在成员管理模块中可批量发送邀请成员邮件</div>
            </Col>
          </Row>
        </TimelineItem>
        <TimelineItem color="green">
          <Row type="flex" justify="start" align="middle" class="code-row-bg">
            <Col span="3">
              <p class="time">2020.2.26-13:22</p>
            </Col>
            <Col span="1">
              <Avatar style="color: #f56a00;background-color: #fde3cf">U</Avatar>
            </Col>
            <Col span="18">
              <div class="content">主账号 创建了新需求
              </div>
              <div class="subcontent">#12-增加邮件邀请成员弹窗并完成邀请成员交互功能</div>
            </Col>
          </Row>
        </TimelineItem>
        <TimelineItem color="green">略</TimelineItem>
        <TimelineItem color="green">略</TimelineItem>
        <TimelineItem color="green">略</TimelineItem>
      </Timeline>
    </div>
  </div>
</template>
<script>
export default {};
</script>
