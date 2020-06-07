<style scoped>
.git {
  margin-left: 2%;
  margin-top: 20px;
  width: 95%;
  height: 100%;
}
.filetitle {
  font-size: 14px;
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
      <Col>
        <!-- <ButtonGroup>
          <Button class="button" @click="modal1 = true">新建文件</Button>
          新建文件弹窗
          <Modal v-model="modal1" title="新建文件" @on-ok="ok" @on-cancel="cancel">
            <Input v-model="value11">
              <span slot="prepend">.mvn/wrapper/</span>
            </Input>
          </Modal>
          上传文件弹窗
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
        </ButtonGroup>-->
        <!-- 下载路径选择与生成复制 -->
        <Select v-model="modelroad" placeholder="clone" style="width:70px" @on-change="chooseroad">
          <Option v-for="item in roadList" :value="item.value" :key="item.value">{{ item.label }}</Option>
        </Select>
        <Input
          v-model="roadvalue"
          style="width: 310px"
        >
          <Icon type="ios-browsers-outline" slot="prefix" />
        </Input>
      </Col>
    </Row>

    <!--分隔符 -->
    <div style="height:20px"></div>
    <!--文件目录表格 -->
    <List border size="small">
      <ListItem style="background-color:#d7e7f2;">
        <div style="width:100%;height:20px">
          <Avatar style="float:left;color: #f56a00;background-color: #fde3cf" size="small">{{this.$route.params.userID}}</Avatar>
          <div
            style="font-size:14px;margin-left:10px;float:left;height:33px;position:relative;top:50%;transform:translateY(-30%)"
          >目录</div>
          <div
            style="font-size:14px;color:grey;float:right;height:100%;position:relative;top:50%;transform:translateY(-42%)"
          >最后提交时间</div>
        </div>
      </ListItem>

      <!-- 返回上层 -->
      <ListItem v-if="this.back == 'true'">
        <Row type="flex" justify="space-between" class="code-row-bg">
          <Col span="8">
            <Icon type="md-arrow-back" style="float:left" size="18" @click="gofather" />
          </Col>
        </Row>
      </ListItem>
      <ListItem v-for="(file,index) in filelist" :key="index">
        <Row type="flex" justify="space-between" class="code-row-bg">
          <Col span="8">
            <div v-if="file.type == 'blob'">
              <Icon type="ios-document-outline" style="float:left" size="18" />
              <div class="filetitle" style="float:left" @click="getcontent(file.path)">{{file.name}}</div>
            </div>
            <div v-else>
              <Icon type="ios-albums" style="float:left" size="18" />
              <div class="filetitle" style="float:left" @click="gosub">{{file.name}}</div>
            </div>
          </Col>
          <Col span="8">
            <div class="filetitle">{{file.commit_message}}</div>
          </Col>
          <Col span="8">
            <div class="filetitle" style="text-align:right">{{file.commit_date}}</div>
          </Col>
        </Row>
      </ListItem>
    </List>
    <!--分隔符 -->
    <div style="height:20px"></div>
    <!--readme文件内容 -->
    <List border size="small" v-if="this.back == 'false'">
      <ListItem style="background-color:#d7e7f2;">
        <div style="width:100%;height:20px">{{this.filedetail.file_name}}</div>
      </ListItem>
      <ListItem>
        <div style="width:100%;height:100%">
          <i-editor v-model="content" :autosize="{minRows: 20,maxRows: 20}"></i-editor>
        </div>
      </ListItem>
    </List>
  </div>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      projectname:" ",
      filelist: [],
      filedetail: [],
      filedetailtable: [],
      content: "",
      roadvalue: "",
      back: "false",
      roadList:[
        {
          value:"ssh",
          label:"ssh"
        },
        {
          value:"http",
          label:"http"
        }
      ]
    };
  },
  methods: {

    chooseroad(value){
      axios
        .get("/project/name", {
          params: {
            itemid: this.$route.params.itemID
          },
          headers: { "Access-Control-Allow-Origin": "*" }
        })
        .then(res => {
          this.pojectname = res.data;
          console.log(this.pojectname);
          if (value == 'ssh')
          {
            var roadname="git@192.168.0.134:zyh/";
            roadname+= res.data;
            roadname+=".git";
            this.roadvalue=roadname;
          }else if(value == 'http')
          {
            var roadname="http://192.168.0.134:8081/zyh/";
            roadname+= res.data;
            roadname+=".git";
            this.roadvalue=roadname;
          }
        })
        .catch(err => {
          console.error(err);
        });
      
    },
    gosub() {
      this.back = "true";
      axios
        .get("/project/filesubtree", {
          params: {
            itemid: this.$route.params.itemID
          },
          headers: { "Access-Control-Allow-Origin": "*" }
        })
        .then(res => {
          this.filelist = res.data;
          console.log(res.data);
        })
        .catch(err => {
          console.error(err);
        });
    },
    gofather() {
      this.back = "false";
      axios
        .get("/project/filetree", {
          params: {
            itemid: this.$route.params.itemID
          },
          headers: { "Access-Control-Allow-Origin": "*" }
        })
        .then(res => {
          this.filelist = res.data;
          getcontent("README.md");
          console.log(res.data);
        })
        .catch(err => {
          console.error(err);
        });
    },
    getcontent(path) {
      axios
        .get("/project/filecontent", {
          params: {
            itemid: this.$route.params.itemID,
            filepath: path
          },
          headers: { "Access-Control-Allow-Origin": "*" }
        })
        .then(res => {
          this.filedetailtable = res.data;
          this.filedetail = this.filedetailtable[path];
          this.content = atob(this.filedetail.content);
          console.log(res.data);
          console.log(this.filedetail);
        })
        .catch(err => {
          console.error(err);
        });
    }
  },
  created() {
    axios
      .get("/project/filecontent", {
        params: {
          itemid: this.$route.params.itemID,
          filepath: "README.md"
        },
        headers: { "Access-Control-Allow-Origin": "*" }
      })
      .then(res => {
        this.filedetailtable = res.data;
        this.filedetail = this.filedetailtable["README.md"];
        this.content = atob(this.filedetail.content);
        console.log(res.data);
        console.log(this.filedetail);
      })
      .catch(err => {
        console.error(err);
      });
  },
  beforeCreate() {
    axios
      .get("/project/filetree", {
        params: {
          itemid: this.$route.params.itemID
        },
        headers: { "Access-Control-Allow-Origin": "*" }
      })
      .then(res => {
        this.filelist = res.data;
        console.log(res.data);
      })
      .catch(err => {
        console.error(err);
      });
  }
};
</script>