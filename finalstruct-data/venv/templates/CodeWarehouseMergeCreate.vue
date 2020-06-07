<style scoped>
.selectlist {
  margin-top: 10px;
  margin-bottom: 10px;
  text-align: center;
}
.selecttitle {
  float: left;
  height: 35px;
  line-height: 35px;
}
.code-row-bg {
  height: 35px;
  line-height: 35px;
}
.a {
  text-decoration: none;
  color: #000;
}
.titletext {
  margin-left: 2.5%;
  margin-right: 1.5%;
  margin-top: 10px;
  margin-bottom: 10px;
}
.mergetext {
  width: 96%;
  height: 100%;
  margin-left: 2.5%;
  margin-right: 1.5%;
  border: 1px solid #d9d9d9;
  padding: 1%;
}
.alerttext {
}
.button {
  font-size: 12px;
  margin-top: 10px;
}
</style>
<template>
  <div>
    <div class="titletext">
      <h2>新建合并请求</h2>请选择合并请求的源分支和目标分支，并查看提交记录和文件改动
      <br />合并之后目标分支将会包括源分支的改动内容
    </div>
    <!--选择合并源和目标-->
    <div class="selectlist">
      <Row type="flex" justify="start" align="middle" class="code-row-bg">
        <Col span="10" offset="1">
          <div class="selecttitle">源分支</div>
          <Select v-model="modelbranch" style="width:450px" placeholder="全部分支">
            <Option
              v-for="item in branchList"
              :value="item.value"
              :key="item.value"
            >{{ item.label }}</Option>
          </Select>
        </Col>

        <Col span="2">>>合并到>></Col>
        <Col span="10" offset="1">
          <div class="selecttitle">目标分支</div>
          <Select v-model="modelpeople" style="width:450px" placeholder="全部成员">
            <Option
              v-for="item in peopleList"
              :value="item.value"
              :key="item.value"
            >{{ item.label }}</Option>
          </Select>
        </Col>
      </Row>
    </div>
    <!--填写合并内容-->
    <div class="mergetext">
      <div class="alerttext">
        <Alert type="warning" show-icon>
          无法合并
          <template slot="desc">没有修改内容</template>
        </Alert>
      </div>
      <div>
        <div style="font-size:20px;margin:10px">标题</div>
        <Input v-model="value" placeholder="请输入合并请求标题" style="width: 100%" />
      </div>
      <div>
        <div style="font-size:20px;margin:10px">描述</div>
        <div style="border: 0.5px solid #d9d9d9;height:100%;">
          <i-editor v-model="content" style="height:100%;"></i-editor>
        </div>
      </div>
      <Button class="button" type="primary" disabled>新建合并请求</Button>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      modelstate: "",
      branchList: [
        {
          value: "master",
          label: "master"
        },
        {
          value: "test1",
          label: "test1"
        },
        {
          value: "test2",
          label: "test2"
        }
      ],
      modelbranch: "",
      peopleList: [
        {
          value: "master",
          label: "master"
        },
        {
          value: "test1",
          label: "test1"
        },
        {
          value: "test2",
          label: "test2"
        }
      ],
      modelpeople: "",
      select: "up",
      content: ""
    };
  },
  methods: {
    changetodown: function() {
      this.select = "down";
      this.$forceUpdate();
    },
    changetoup: function() {
      this.select = "up";
      this.$forceUpdate();
    }
  }
};
</script>
