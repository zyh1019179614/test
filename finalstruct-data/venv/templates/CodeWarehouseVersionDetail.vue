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
.branchtext {
  height: 100%;
  margin-left: 2.5%;
  margin-right: 1.5%;
}
.branchtitle {
  background-color: #bad6f1;
  color: #5280e9;
  font-size: 14px;
  width: 60px;
  text-align: center;
}
.button {
  font-size: 12px;
  margin-top: 10px;
}
</style>
<template>
  <div>
    <div class="titletext">
      <h2>V1.0.0</h2>
      <div class="branchtitle">已发布</div>
      <Divider />
    </div>
    <!--选择合并源和目标-->

    <!--填写合并内容-->
    <div class="branchtext">
      <div>
        <div style="font-size:20px;margin:10px">标题</div>
        <Input v-model="value" type="textarea" style="width: 100%;height:" icon="ios-browsers-outline"/>
      </div>
      <div>
        <div style="font-size:20px;margin:10px">摘要</div>
        <div style="height:100%;">
          <i-editor v-model="content" style="height:100%;"></i-editor>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      value:
        "版本可以帮助你在某个节点将代码打包发布，它是基于 Git tag 的，每一个版本对应一个标签。你可以选择某个分支的最新代码发布一个版本。在发布版本时，我们推荐你使用语义化版本。版本号规则如下：",
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
      content: ""
    };
  },
  methods: {
  }
};
</script>
