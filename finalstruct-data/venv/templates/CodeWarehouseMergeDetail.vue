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
.branchtitlegreen {
  float: left;
  background-color: #dfffdf;
  color: green;
  font-size: 14px;
  width: 60px;
  text-align: center;
  margin-right: 10px;
}
.branchtitleblue {
    border-radius:5px;
  float: left;
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
      <h2>test1</h2>
      <div class="branchtitlegreen">可合并</div>
      <div style="float: left;">
        <div class="branchtitleblue">test1</div>
        <Icon style="float:left" type="ios-arrow-round-forward" />
        <div class="branchtitleblue">master</div>
      </div>
      <Divider />
    </div>
    <!--选择合并源和目标-->

    <!--填写合并内容-->
    <div class="branchtext">
      <div>
        <div style="font-size:20px;margin:10px">标题</div>
        <Input
          v-model="value"
          type="textarea"
          style="width: 100%;height:"
          icon="ios-browsers-outline"
        />
      </div>
      <div>
        <div style="font-size:20px;margin:10px">摘要</div>
        <div style="height:100%;">
          <i-editor v-model="content" style="height:100%;"></i-editor>
        </div>
      </div>
      <Button style="margin:10px" type="success">合并分支</Button>
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
  methods: {}
};
</script>
