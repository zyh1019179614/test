<style scoped>
.git {
  margin-left: 2%;
  margin-top: 20px;
  width: 95%;
  height: 100%;
}
.filetitle {
  font-size: 13px;
  margin-left: 1%;
}
.code-row-bg {
  width: 100%;
}
.button {
  font-size: 12px;
}
</style>
<template>
  <div class="git">
    <!--分支选择框 -->

    <Row>
      <!-- 分支选择 -->
      <Col span="4" style="padding-right:10px">
        <Select v-model="modelbranch" filterable placeholder="master">
          <Option v-for="item in branchList" :value="item.value" :key="item.value">{{ item.label }}</Option>
        </Select>
      </Col>
      <Col span="4">
        <Button type="primary" class="button" :to="{name: 'mergecreate'}">新建合并请求</Button>
      </Col>
      <Col span="11" offset="5">
        <ButtonGroup>
          <Button class="button" @click="modal1 = true">新建文件</Button>
          <!--新建文件弹窗-->
          <Modal v-model="modal1" title="新建文件" @on-ok="ok" @on-cancel="cancel">
            <Input v-model="value11">
              <span slot="prepend">.mvn/wrapper/</span>
            </Input>
          </Modal>
          <!--上传文件弹窗-->
          <Button class="button" @click="modal2 = true">上传文件</Button>
          <Modal v-model="modal2" title="上传文件" @on-ok="ok" @on-cancel="cancel">
            <Upload multiple type="drag" action="//jsonplaceholder.typicode.com/posts/">
              <div style="padding: 20px 0">
                <Icon type="ios-cloud-upload" size="52" style="color: #3399ff"></Icon>
                <p>Click or drag files here to upload</p>
              </div>
            </Upload>
          </Modal>
          <Button class="button">查找文件</Button>
        </ButtonGroup>
        <!-- 下载路径选择与生成复制 -->
        <Select v-model="modelroad" placeholder="ssh" style="width:60px">
          <Option v-for="item in roadList" :value="item.value" :key="item.value">{{ item.label }}</Option>
        </Select>
        <Input
          v-model="roadvalue"
          placeholder="git@e.coding.net:Zyhtooooooop/coding-demo.git"
          style="width: 250px"
        >
          <Icon type="ios-browsers-outline" slot="suffix" />
        </Input>
      </Col>
    </Row>

    <!--分隔符 -->
    <div style="height:20px"></div>
    <!--文件目录表格 -->
    <List border size="small">
      <ListItem style="background-color:#d7e7f2;">
        <div style="width:100%;height:20px">
          <Avatar style="float:left;color: #f56a00;background-color: #fde3cf" size="small">U</Avatar>
          <div
            style="font-size:14px;margin-left:10px;float:left;height:33px;position:relative;top:50%;transform:translateY(-30%)"
          >主账号</div>
          <div
            style="font-size:12px;color:grey;margin-left:7px;float:left;height:100%;position:relative;top:50%;transform:translateY(-42%)"
          >初始化 demo 项目</div>
          <div
            style="font-size:12px;color:grey;float:right;height:100%;position:relative;top:50%;transform:translateY(-42%)"
          >最后提交 8654243055</div>
        </div>
      </ListItem>
      <!-- <ListItem>
        <Row type="flex" justify="space-between" class="code-row-bg">
          <Col span="8">
            <div>
              <Icon type="ios-folder-open-outline" style="float:left" size="18" />
              <div class="filetitle" style="float:left">.mvn/wrapper</div>
            </div>
          </Col>
          <Col span="8">
            <div class="filetitle">初始化demo项目</div>
          </Col>
          <Col span="8">
            <div class="filetitle" style="text-align:right">1个月前</div>
          </Col>
        </Row>
      </ListItem>
      <ListItem>
        <Row type="flex" justify="space-between" class="code-row-bg">
          <Col span="8">
            <div>
              <Icon type="ios-folder-open-outline" style="float:left" size="18" />
              <div class="filetitle" style="float:left">src</div>
            </div>
          </Col>
          <Col span="8">
            <div class="filetitle">初始化demo项目</div>
          </Col>
          <Col span="8">
            <div class="filetitle" style="text-align:right">1个月前</div>
          </Col>
        </Row>
      </ListItem>
      <ListItem>
        <Row type="flex" justify="space-between" class="code-row-bg">
          <Col span="8">
            <div>
              <Icon type="ios-document-outline" style="float:left" size="18"/>
              <div class="filetitle" style="float:left">.gitignore</div>
            </div>
          </Col>
          <Col span="8">
            <div class="filetitle">初始化demo项目</div>
          </Col>
          <Col span="8">
            <div class="filetitle" style="text-align:right">1个月前</div>
          </Col>
        </Row>
      </ListItem>
      <ListItem>
        <Row type="flex" justify="space-between" class="code-row-bg">
          <Col span="8">
            <div>
              <Icon type="ios-document-outline" style="float:left" size="18"/>
              <div class="filetitle" style="float:left">Dockerfile</div>
            </div>
          </Col>
          <Col span="8">
            <div class="filetitle">初始化demo项目</div>
          </Col>
          <Col span="8">
            <div class="filetitle" style="text-align:right">1个月前</div>
          </Col>
        </Row>
      </ListItem>
      <ListItem>
        <Row type="flex" justify="space-between" class="code-row-bg">
          <Col span="8">
            <div>
              <Icon type="ios-document-outline" style="float:left" size="18"/>
              <div class="filetitle" style="float:left">Jenkinsfile</div>
            </div>
          </Col>
          <Col span="8">
            <div class="filetitle">初始化demo项目</div>
          </Col>
          <Col span="8">
            <div class="filetitle" style="text-align:right">1个月前</div>
          </Col>
        </Row>
      </ListItem>
      <ListItem><Row type="flex" justify="space-between" class="code-row-bg">
          <Col span="8">
            <div>
              <Icon type="ios-paper-outline" style="float:left" size="18"/>
              <div class="filetitle" style="float:left">README.md</div>
            </div>
          </Col>
          <Col span="8">
            <div class="filetitle">初始化demo项目</div>
          </Col>
          <Col span="8">
            <div class="filetitle" style="text-align:right">1个月前</div>
          </Col>
        </Row></ListItem>
      <ListItem><Row type="flex" justify="space-between" class="code-row-bg">
          <Col span="8">
            <div>
              <Icon type="ios-document-outline" style="float:left" size="18"/>
              <div class="filetitle" style="float:left">mvnw</div>
            </div>
          </Col>
          <Col span="8">
            <div class="filetitle">初始化demo项目</div>
          </Col>
          <Col span="8">
            <div class="filetitle" style="text-align:right">1个月前</div>
          </Col>
        </Row></ListItem>
      <ListItem><Row type="flex" justify="space-between" class="code-row-bg"> 
          <Col span="8">
            <div>
              <Icon type="ios-document-outline" style="float:left" size="18"/>
              <div class="filetitle" style="float:left">mvnw.cmd</div>
            </div>
          </Col>
          <Col span="8">
            <div class="filetitle">初始化demo项目</div>
          </Col>
          <Col span="8">
            <div class="filetitle" style="text-align:right">1个月前</div>
          </Col>
      </Row></ListItem>-->
      <ListItem>
        <Row type="flex" justify="space-between" class="code-row-bg">
          <Col span="8">
            <Icon type="md-arrow-back" style="float:left" size="18" />
          </Col>
        </Row>
      </ListItem>
      <ListItem>
        <Row type="flex" justify="space-between" class="code-row-bg">
          <Col span="8">
            <div>
              <Icon type="ios-document-outline" style="float:left" size="18" />
              <div class="filetitle" style="float:left">MavenWrapperDownloader.java</div>
            </div>
          </Col>
          <Col span="8">
            <div class="filetitle">初始化demo项目</div>
          </Col>
          <Col span="8">
            <div class="filetitle" style="text-align:right">1个月前</div>
          </Col>
        </Row>
      </ListItem>
      <ListItem>
        <Row type="flex" justify="space-between" class="code-row-bg">
          <Col span="8">
            <div>
              <Icon type="ios-document-outline" style="float:left" size="18" />
              <div class="filetitle" style="float:left">maven-wrapper.jar</div>
            </div>
          </Col>
          <Col span="8">
            <div class="filetitle">初始化demo项目</div>
          </Col>
          <Col span="8">
            <div class="filetitle" style="text-align:right">1个月前</div>
          </Col>
        </Row>
      </ListItem>
      <ListItem>
        <Row type="flex" justify="space-between" class="code-row-bg">
          <Col span="8">
            <div>
              <Icon type="ios-document-outline" style="float:left" size="18" />
              <div class="filetitle" style="float:left">maven-wrapper.properties</div>
            </div>
          </Col>
          <Col span="8">
            <div class="filetitle">初始化demo项目</div>
          </Col>
          <Col span="8">
            <div class="filetitle" style="text-align:right">1个月前</div>
          </Col>
        </Row>
      </ListItem>
      <ListItem>
        <Row type="flex" justify="space-between" class="code-row-bg">
          <Col span="8">
            <div>
              <Icon type="ios-document-outline" style="float:left" size="18" />
              <div class="filetitle" style="float:left">TIM截图20200105123319.png</div>
            </div>
          </Col>
          <Col span="8">
            <div class="filetitle">\</div>
          </Col>
          <Col span="8">
            <div class="filetitle" style="text-align:right">1分钟前</div>
          </Col>
        </Row>
      </ListItem>
    </List>
    <!--分隔符 -->
    <div style="height:20px"></div>
    <!--readme文件内容 -->
    <!-- <List border size="small">
      <ListItem style="background-color:#d7e7f2;">
        <div style="width:100%;height:20px">README.md</div>
      </ListItem>
      <ListItem>
        <div style="width:100%;height:100%">
         <i-editor v-model="content"></i-editor>
        </div>
      </ListItem>
    </List>-->
  </div>
</template>
<script>
export default {
  data() {
    return {
      modal1: false,
      modal2: false,
      branchList: [
        {
          value: "master",
          label: "master"
        },
        {
          value: "branch1",
          label: "branch1"
        },
        {
          value: "branch2",
          label: "branch2"
        }
      ],
      modelbranch: "",
      roadList: [
        {
          value: "ssh",
          label: "ssh"
        },
        {
          value: "https",
          label: "https"
        }
      ],
      modelroad: "",
      content: ""
    };
  },
  methods: {
    ok() {
      this.$Message.info("Clicked ok");
    },
    cancel() {
      this.$Message.info("Clicked cancel");
    }
  }
};
</script>